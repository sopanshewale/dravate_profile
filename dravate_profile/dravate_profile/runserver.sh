#!/bin/sh
python manage.py makemigrations
python manage.py makemigrations login
python manage.py migrate
python manage.py migrate login 
python manage.py runserver 0.0.0.0:9191

