gendiff:
	uv run gendiff
gendiff-h:
	uv run gendiff -h
check:
	uv run ruff check .
lint-fix:
	uv run ruff check --fix .
install:
	pip install uv