gendiff:
	uv run gendiff file1.json file2.json
gendiff-h:
	uv run gendiff -h
lint:
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