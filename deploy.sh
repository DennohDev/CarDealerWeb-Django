#!/bin/bash

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn -c gunicorn.conf.py cardealer.wsgi:application 