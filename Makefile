.PHONY: test test-integration lint format install

test:  ## Run unit tests
	python3 -m pytest tests/ -m "not integration" -v

test-integration:  ## Run integration tests (requires AHREFS_API_KEY)
	python3 -m pytest tests/ -m integration -v

lint:  ## Type-check and lint
	python3 -m mypy src/ahrefs/
	python3 -m ruff check src/ tests/

format:  ## Auto-format
	python3 -m ruff format src/ tests/

install:  ## Install in development mode
	pip install -e ".[dev]"
