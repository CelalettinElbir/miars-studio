
python manage.py collectstatic --noinput
python manage.py migrate
python -m gunicorn --bind 0.0.0.0:8000 main.wsgi:application --workers 3 