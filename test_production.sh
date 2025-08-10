#!/usr/bin/env bash

echo "Testing production configuration locally..."

# Set production environment variables
export DEBUG=False
export SECRET_KEY="test-secret-key-for-production-test"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Check for any issues
echo "Running Django checks..."
python manage.py check --deploy

echo "Production test complete!"
