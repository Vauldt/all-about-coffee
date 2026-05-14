PY ?= python3
VAULT ?= /Users/chris/Obsidian Vaults/Coffee/AllAboutCoffee

.PHONY: help install serve build strict sync sync-no-build sync-push clean

help:
	@echo "Targets:"
	@echo "  install         Install Python dependencies"
	@echo "  serve           mkdocs serve (live reload at http://127.0.0.1:8000)"
	@echo "  build           mkdocs build"
	@echo "  strict          mkdocs build --strict"
	@echo "  sync            Sync vault -> docs/coffee, then strict build"
	@echo "  sync-no-build   Sync vault -> docs/coffee, skip build"
	@echo "  sync-push       Sync vault, strict build, commit, and push"
	@echo "  clean           Remove generated site/ directory"

install:
	$(PY) -m pip install -r requirements.txt

serve:
	mkdocs serve

build:
	mkdocs build

strict:
	mkdocs build --strict

sync:
	$(PY) scripts/sync_coffee_vault.py --vault-path "$(VAULT)"

sync-no-build:
	$(PY) scripts/sync_coffee_vault.py --vault-path "$(VAULT)" --no-build

sync-push:
	$(PY) scripts/sync_coffee_vault.py --vault-path "$(VAULT)" --push

clean:
	rm -rf site
