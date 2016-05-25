migrations:
	python manage.py makemigrations lolzin
	python manage.py migrate
shell:
	python manage.py shell
local:
	python manage.py runserver 0.0.0.0:8000
clean:
	find . -name "*.pyc" -type f -delete
	find . -name "*.log" -type f -delete
install:
	pip install -r requirements.txt	
static:
	python manage.py collectstatic --no-input
