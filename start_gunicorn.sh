#!/bin/bash

# Production deployment script for WritePress Django App with Gunicorn

echo "Starting WritePress deployment..."

# Set environment variables
export DJANGO_SETTINGS_MODULE=writepress.settings
export PORT=${PORT:-8000}
export WEB_CONCURRENCY=${WEB_CONCURRENCY:-3}

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Start Gunicorn server
echo "Starting Gunicorn server..."
if [ -f "gunicorn_config.py" ]; then
    echo "Using gunicorn_config.py configuration file"
    gunicorn writepress.wsgi:application --config gunicorn_config.py
else
    echo "Using inline configuration"
    gunicorn writepress.wsgi:application \
        --bind 0.0.0.0:$PORT \
        --workers $WEB_CONCURRENCY \
        --timeout 120 \
        --access-logfile - \
        --error-logfile - \
        --log-level info
fi
