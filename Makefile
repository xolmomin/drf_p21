mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

check:
	isort .
	flake8 .

coverage:
	pytest --cov-report html --cov .

build_index:
	python manage.py search_index --rebuild
