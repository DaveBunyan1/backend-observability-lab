.PHONY: test lint format typecheck

test:
	python -m pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src