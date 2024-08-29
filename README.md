# django-spirit-auth
Spirit is a Python based forum built using the Django framework.

## Documentation

Docs can be found at [spirit.readthedocs.io](http://spirit.readthedocs.io/en/latest/)

## Compatibility

* Python 3.8, 3.9, 3.10, and 3.11 (recommended)
* Django 3.2 LTS, and 4.2 LTS
* PostgreSQL (recommended), MySQL, Oracle Database and SQLite

Constrained by "[What Python version can I use with Django?](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)"

## Usage

> New in Spirit 0.5

```
pip install django-spirit
spirit startproject mysite
cd mysite
python manage.py spiritinstall
python manage.py createsuperuser
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

For detailed setup docs, see [spirit.readthedocs.io](http://spirit.readthedocs.io/en/latest/)
