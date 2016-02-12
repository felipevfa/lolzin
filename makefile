deploy:
	appcfg.py -A river-tiger-113911 --noauth_local_webserver update app.yaml
local:
	python manage.py runserver 0.0.0.0:8000
clean:
	find . -name "*.pyc" -type f -delete
	find . -name "*.log" -type f -delete
install:
	pip install -r requirements.txt	
static:
	python manage.py collectstatic --no-input
