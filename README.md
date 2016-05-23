## Lolzin Quiz

[Django](https://docs.djangoproject.com/en/1.9/intro/tutorial01/) 

[MySQL com Django](http://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql#).

[Postgres](http://stackoverflow.com/questions/17137346/psycopg2-on-amazon-elastic-beanstalk) deveria ser utilizado mas o psycopg incrementa a dificuldade de deploy no Beanstalk

[Para dar deploy no beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

make local = python manage runserver

make clean = limpar .pyc


[Comando collectstatic quando do deploy](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-container.html)

[Arquivos estaticos](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)


[Atualmente rodando aqui](http://workpl0x.elasticbeanstalk.com/)


arquivo .config na pasta .ebextensions:
"

container_commands:
  collectstatic:
    command: "django-admin.py collectstatic --noinput"
option_settings:
  "aws:elasticbeanstalk:application:environment":
    DJANGO_SETTINGS_MODULE: "mysite.settings"
    PYTHONPATH: "/opt/python/current/app/lolzin:$PYTHONPATH"
  "aws:elasticbeanstalk:container:python":
    WSGIPath: "lolzin/mysite/wsgi.py"
  "aws:elasticbeanstalk:container:python:staticfiles":
    "/static/": "static/"	

"
=======
# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
