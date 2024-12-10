requirements.txt: requirements.in
	pip-compile --upgrade -o $@ $^

black:
	python3 -m black --config pyproject.toml .

isort:
	python3 -m isort .

pylint:
	python3 -m pylint --recursive=yes app tests

pytest:
	pytest -n auto --cov --cov-report term --cov-report xml:coverage.xml --junitxml report.xml

db_upgrade:
	docker exec cs-development-app sh -c 'alembic upgrade head'

db_migration:
	docker exec cs-development-app sh -c 'alembic revision --autogenerate -m "$(msg)"'

format: black isort pylint
