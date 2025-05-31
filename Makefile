install:
	pip install uv
	uv sync 
lint:
	uv run ruff check .
test:
	uv run pytest
lint-fix:
	uv run ruff check --fix .
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml