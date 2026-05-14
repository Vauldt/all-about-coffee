#!/usr/bin/env python3
"""Sync Matthew's Obsidian coffee vault into the MkDocs site.

Steps performed:
    1. Import Markdown and supported assets from the source vault into
       ``docs/coffee`` and ``docs/assets/coffee``.
    2. Slugify folder/file names, convert Obsidian wikilinks/embeds where
       uniquely resolvable, and create lightweight directory index pages.
    3. Clean up cross-page links: rewrite slugified targets, drop the known
       broken ``moc-review-1`` references, and de-link missing local files
       so the site still builds.
    4. Optionally run ``mkdocs build --strict`` and, on success, commit and
       push the updated content.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
COFFEE_DOCS = DOCS / "coffee"
COFFEE_ASSETS = DOCS / "assets" / "coffee"

DEFAULT_VAULT_PATH = Path("/Users/chris/Obsidian Vaults/Coffee/AllAboutCoffee")

ASSET_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".pdf"}

SKIP_DIR_NAMES = {
    ".obsidian",
    ".trash",
    ".git",
    ".claude",
    "TEMPLATES",
    "Templates",
    "templates",
    "10 Daily Journal",
    "Daily Journal",
    "Daily Notes",
    "Inbox",
    "00 Inbox",
    "Private",
    "__pycache__",
}

MD_LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def slugify(value: str, fallback: str = "page") -> str:
    value = value.strip().replace("&", " and ")
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or fallback


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in path.parts)


def unique_path(path: Path, used: set[Path]) -> Path:
    if path not in used:
        used.add(path)
        return path
    stem, suffix, parent = path.stem, path.suffix, path.parent
    i = 2
    while True:
        candidate = parent / f"{stem}-{i}{suffix}"
        if candidate not in used:
            used.add(candidate)
            return candidate
        i += 1


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def title_from_filename(path: Path) -> str:
    title = path.stem.replace("_", " ").replace("-", " ").strip()
    title = re.sub(r"\s+", " ", title)
    return title[:1].upper() + title[1:] if title else "Untitled"


def split_target(raw: str) -> tuple[str, str]:
    if "#" in raw:
        name, anchor = raw.split("#", 1)
        return name.strip(), anchor.strip()
    return raw.strip(), ""


def split_url(url: str) -> tuple[str, str]:
    if "#" in url:
        path, anchor = url.split("#", 1)
        return path, "#" + anchor
    return url, ""


def relative_link(src: Path, dest: Path, anchor: str = "") -> str:
    rel = os.path.relpath(dest, start=src.parent).replace(os.sep, "/")
    if anchor:
        rel += "#" + slugify(anchor)
    return rel


def rel_to(from_file: Path, to_file: Path, anchor: str = "") -> str:
    return os.path.relpath(to_file, start=from_file.parent).replace(os.sep, "/") + anchor


def is_external(url: str) -> bool:
    lower = url.lower()
    return (
        "://" in lower
        or lower.startswith(("mailto:", "tel:", "javascript:"))
        or lower.startswith("#")
        or lower.startswith("{")
    )


def slug_path_from_target(target: str) -> Path:
    p = Path(target)
    parts = list(p.parts)
    new_parts: list[str] = []
    for i, part in enumerate(parts):
        if part in ("..", "."):
            new_parts.append(part)
            continue
        if i == len(parts) - 1 and "." in part:
            stem = Path(part).stem
            suffix = Path(part).suffix.lower()
            new_parts.append(slugify(stem) + suffix)
        else:
            new_parts.append(slugify(part))
    return Path(*new_parts)


def unique(items: list[Path]) -> Path | None:
    dedup = sorted(set(items))
    return dedup[0] if len(dedup) == 1 else None


# ---------------------------------------------------------------------------
# Import step
# ---------------------------------------------------------------------------


def normalize_wikilinks(
    text: str,
    src_dest: Path,
    page_map: dict[str, Path],
    asset_map: dict[str, Path],
) -> str:
    def embedded(match: re.Match[str]) -> str:
        raw = match.group(1).strip()
        name, _anchor = split_target(raw)
        key = Path(name).name.lower()
        alt = Path(name).stem
        if key in asset_map:
            return f"![{alt}]({relative_link(src_dest, asset_map[key])})"
        if name.lower() in page_map:
            return f"[{alt}]({relative_link(src_dest, page_map[name.lower()])})"
        return alt

    def wikilink(match: re.Match[str]) -> str:
        raw = match.group(1).strip()
        if "|" in raw:
            target, label = raw.split("|", 1)
            label = label.strip()
        else:
            target, label = raw, raw
        name, anchor = split_target(target)
        key = name.lower()
        label = label.split("#", 1)[0].strip() or name
        if key in page_map:
            return f"[{label}]({relative_link(src_dest, page_map[key], anchor)})"
        return label

    text = re.sub(r"!\[\[([^\]]+)\]\]", embedded, text)
    text = re.sub(r"\[\[([^\]]+)\]\]", wikilink, text)
    text = re.sub(r"(?m)^tags:\s*$", "tags: []", text)
    return text


def import_vault(vault_path: Path) -> None:
    if not vault_path.exists():
        raise SystemExit(f"Source vault not found: {vault_path}")

    if COFFEE_DOCS.exists():
        shutil.rmtree(COFFEE_DOCS)
    if COFFEE_ASSETS.exists():
        shutil.rmtree(COFFEE_ASSETS)
    COFFEE_DOCS.mkdir(parents=True, exist_ok=True)
    COFFEE_ASSETS.mkdir(parents=True, exist_ok=True)

    md_sources = [
        p for p in vault_path.rglob("*.md")
        if not should_skip(p.relative_to(vault_path))
    ]
    asset_sources = [
        p for p in vault_path.rglob("*")
        if p.is_file()
        and p.suffix.lower() in ASSET_EXTS
        and not should_skip(p.relative_to(vault_path))
    ]

    used_paths: set[Path] = set()
    source_to_dest: dict[Path, Path] = {}
    basename_to_pages: dict[str, list[Path]] = defaultdict(list)
    stem_to_pages: dict[str, list[Path]] = defaultdict(list)

    for src in sorted(md_sources):
        rel = src.relative_to(vault_path)
        slug_parts = [slugify(part) for part in rel.parts[:-1]]
        slug_file = slugify(rel.stem) + ".md"
        dest = unique_path(COFFEE_DOCS.joinpath(*slug_parts, slug_file), used_paths)
        source_to_dest[src] = dest
        basename_to_pages[src.name.lower()].append(dest)
        stem_to_pages[src.stem.lower()].append(dest)

    asset_used: set[Path] = set()
    asset_map: dict[str, Path] = {}
    for src in sorted(asset_sources):
        slug_name = slugify(src.stem) + src.suffix.lower()
        dest = unique_path(COFFEE_ASSETS / slug_name, asset_used)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        asset_map[src.name.lower()] = dest
        asset_map[src.stem.lower()] = dest

    page_map: dict[str, Path] = {}
    for key, values in basename_to_pages.items():
        if len(values) == 1:
            page_map[key] = values[0]
    for key, values in stem_to_pages.items():
        if len(values) == 1:
            page_map[key] = values[0]

    converted = 0
    for src, dest in source_to_dest.items():
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8", errors="replace")
        text = normalize_wikilinks(text, dest, page_map, asset_map)
        if not first_heading(text):
            text = f"# {title_from_filename(src)}\n\n{text.lstrip()}"
        dest.write_text(text, encoding="utf-8")
        converted += 1

    homepage_src = vault_path / "Homepage.md"
    if homepage_src in source_to_dest:
        homepage_dest = source_to_dest[homepage_src]
        index = COFFEE_DOCS / "index.md"
        if homepage_dest.exists():
            index.write_text(homepage_dest.read_text(encoding="utf-8"), encoding="utf-8")
            if homepage_dest != index:
                homepage_dest.unlink()
    elif not (COFFEE_DOCS / "index.md").exists():
        (COFFEE_DOCS / "index.md").write_text(
            "# Coffeepedia\n\n"
            "This section contains the imported coffee vault content.\n\n",
            encoding="utf-8",
        )

    created_indexes = 0
    for directory in sorted([p for p in COFFEE_DOCS.rglob("*") if p.is_dir()]):
        index = directory / "index.md"
        if index.exists():
            continue
        pages = sorted([p for p in directory.iterdir() if p.is_file() and p.suffix == ".md"])
        child_dirs = sorted([p for p in directory.iterdir() if p.is_dir()])
        if not pages and not child_dirs:
            continue
        rel_title = (
            directory.relative_to(COFFEE_DOCS)
            .as_posix()
            .replace("-", " ")
            .replace("/", " / ")
            .title()
        )
        lines = [f"# {rel_title}", ""]
        if child_dirs:
            lines += ["## Sections", ""]
            for child in child_dirs:
                lines.append(f"- [{child.name.replace('-', ' ').title()}]({child.name}/)")
            lines.append("")
        if pages:
            lines += ["## Pages", ""]
            for page in pages:
                if page.name == "index.md":
                    continue
                lines.append(f"- [{title_from_filename(page)}]({page.name})")
            lines.append("")
        index.write_text("\n".join(lines), encoding="utf-8")
        created_indexes += 1

    print(f"  Converted Markdown files: {converted}")
    print(f"  Copied assets:            {len(asset_sources)}")
    print(f"  Created directory indexes: {created_indexes}")


# ---------------------------------------------------------------------------
# Cleanup step
# ---------------------------------------------------------------------------


def build_indexes() -> tuple[dict[str, list[Path]], dict[str, list[Path]], dict[str, Path]]:
    by_stem: dict[str, list[Path]] = {}
    by_name: dict[str, list[Path]] = {}
    by_rel_slug: dict[str, Path] = {}
    for page in COFFEE_DOCS.rglob("*.md"):
        relp = page.relative_to(COFFEE_DOCS)
        by_stem.setdefault(page.stem.lower(), []).append(page)
        by_stem.setdefault(slugify(page.stem), []).append(page)
        by_name.setdefault(page.name.lower(), []).append(page)
        by_name.setdefault(slugify(page.stem) + page.suffix.lower(), []).append(page)
        by_rel_slug[relp.as_posix().lower()] = page
        by_rel_slug[slug_path_from_target(relp.as_posix()).as_posix().lower()] = page
    return by_stem, by_name, by_rel_slug


def resolve_link(
    src: Path,
    url: str,
    by_stem: dict[str, list[Path]],
    by_name: dict[str, list[Path]],
    by_rel_slug: dict[str, Path],
) -> Path | None:
    path_part, _anchor = split_url(url)
    if not path_part:
        return None
    decoded = unquote(path_part).strip().replace("\\", "/")
    if not decoded:
        return None

    raw_candidate = (src.parent / decoded).resolve()
    if raw_candidate.exists() and raw_candidate.is_file() and raw_candidate.suffix == ".md":
        return raw_candidate

    raw_index = (src.parent / decoded / "index.md").resolve()
    if raw_index.exists():
        return raw_index

    slug_candidate = (src.parent / slug_path_from_target(decoded)).resolve()
    if slug_candidate.exists() and slug_candidate.is_file():
        return slug_candidate

    slug_index = (src.parent / slug_path_from_target(decoded) / "index.md").resolve()
    if slug_index.exists():
        return slug_index

    if Path(decoded).name.lower() == "readme.md":
        index_candidate = (src.parent / Path(decoded).parent / "index.md").resolve()
        if index_candidate.exists():
            return index_candidate
        coffee_index = COFFEE_DOCS / "index.md"
        if decoded.startswith("..") and coffee_index.exists():
            return coffee_index

    if Path(decoded).stem.lower() == "homepage":
        return COFFEE_DOCS / "index.md"

    root_slug = slug_path_from_target(decoded)
    if root_slug.as_posix().lower() in by_rel_slug:
        return by_rel_slug[root_slug.as_posix().lower()]

    base = Path(decoded).name
    stem = Path(decoded).stem
    for key in (base.lower(), slugify(stem) + ".md"):
        match = unique(by_name.get(key, []))
        if match:
            return match
    for key in (stem.lower(), slugify(stem)):
        match = unique(by_stem.get(key, []))
        if match:
            return match
    return None


def cleanup_links() -> None:
    by_stem, by_name, by_rel_slug = build_indexes()
    changed_files = 0
    rewritten = 0
    delinked = 0

    for src in sorted(COFFEE_DOCS.rglob("*.md")):
        text = src.read_text(encoding="utf-8", errors="replace")

        def repl(match: re.Match[str]) -> str:
            nonlocal rewritten, delinked
            label = match.group(1)
            url = match.group(2).strip()
            if is_external(url):
                return match.group(0)
            path_part, anchor = split_url(url)

            if "moc-review-1.md" in unquote(path_part).lower():
                delinked += 1
                return label

            resolved = resolve_link(src, url, by_stem, by_name, by_rel_slug)
            if resolved and resolved.exists():
                new = rel_to(src, resolved, anchor)
                if new != url:
                    rewritten += 1
                    return f"[{label}]({new})"
                return match.group(0)

            decoded = unquote(path_part)
            if decoded.lower().endswith(".md") or "/" in decoded:
                delinked += 1
                return label
            return match.group(0)

        new_text = MD_LINK.sub(repl, text)
        if new_text != text:
            src.write_text(new_text, encoding="utf-8")
            changed_files += 1

    print(f"  Files updated:     {changed_files}")
    print(f"  Links rewritten:   {rewritten}")
    print(f"  Links de-linked:   {delinked}")


# ---------------------------------------------------------------------------
# Build / git
# ---------------------------------------------------------------------------


def run_strict_build() -> bool:
    print("Running mkdocs build --strict ...")
    result = subprocess.run(
        ["mkdocs", "build", "--strict"],
        cwd=REPO_ROOT,
        text=True,
    )
    if result.returncode != 0:
        print(f"mkdocs build --strict failed (exit {result.returncode})")
        return False
    print("Strict build passed.")
    return True


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def commit_and_push(message: str) -> None:
    status = git("status", "--porcelain").stdout
    if not status.strip():
        print("No changes to commit.")
        return
    git("add", "docs/coffee", "docs/assets/coffee")
    staged = git("diff", "--cached", "--name-only").stdout
    if not staged.strip():
        print("No staged changes for docs/coffee or docs/assets/coffee.")
        return
    git("commit", "-m", message)
    print(f"Committed: {message}")
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    push = git("push", "origin", branch, check=False)
    if push.returncode != 0:
        print(f"Push failed:\n{push.stderr}")
        sys.exit(push.returncode)
    print(f"Pushed to origin/{branch}.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--vault-path",
        type=Path,
        default=DEFAULT_VAULT_PATH,
        help=f"Source Obsidian vault path (default: {DEFAULT_VAULT_PATH})",
    )
    p.add_argument(
        "--no-build",
        action="store_true",
        help="Skip the mkdocs --strict build step.",
    )
    p.add_argument(
        "--push",
        action="store_true",
        help="Commit and push changes if the strict build succeeds.",
    )
    p.add_argument(
        "--commit-message",
        default="Sync Coffeepedia vault content",
        help="Commit message when --push is used.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Vault source: {args.vault_path}")
    print(f"Site target:  {COFFEE_DOCS.relative_to(REPO_ROOT)}/")
    print()

    print("Importing vault into MkDocs site ...")
    import_vault(args.vault_path)
    print()

    print("Cleaning up local links ...")
    cleanup_links()
    print()

    if args.no_build:
        print("Skipping build (--no-build).")
        if args.push:
            print("--push ignored because --no-build was given.")
        return

    if not run_strict_build():
        sys.exit(1)

    if args.push:
        print()
        commit_and_push(args.commit_message)


if __name__ == "__main__":
    main()
