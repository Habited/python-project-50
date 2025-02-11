gendiff:
	uv run gendiff
gendiff-h:
	uv run gendiff -h
check:
	uv run ruff check .
pytest:
	uv run pytest
lint-fix:
	uv run ruff check --fix .
install:
	pip install uv
test-coverage:
	uv add pytest-cov
	uv run pytest --cov