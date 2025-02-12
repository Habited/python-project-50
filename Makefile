install:
	uv sinc
lint:
	uv run ruff check .
test:
	uv run pytest
lint-fix:
	uv run ruff check --fix .
test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml