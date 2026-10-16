PYTHON ?= uv run python
SRC ?= src/main.py

setup:
	uv sync --group dev
	uv run pre-commit install
	uv run pre-commit install --hook-type pre-push
	uv run pre-commit install --hook-type commit-msg

install: setup

test:
	uv run pytest

pytest: test

ruff:
	uv run ruff check .

ruff-fix:
	uv run ruff check . --fix

fix: ruff-fix

format:
	uv run ruff format .

pyright:
	uv run pyright

checks:
	uv run ruff format . --check
	uv run ruff check .
	uv run pyright
	uv run pytest
