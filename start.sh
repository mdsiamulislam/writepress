#!/bin/bash

# Set the correct working directory
cd "/home/sft/siam vai/"

# Set the project name
PROJECT_NAME="writepress"

echo "Project name: $PROJECT_NAME"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting WritePress deployment...${NC}"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Virtual environment not found!${NC}"
    echo "Please create a virtual environment first:"
    echo "python -m venv venv"
    exit 1
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

cd writepress
# Install requirements if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo -e "${YELLOW}Installing requirements...${NC}"
    pip install -r requirements.txt
else
    echo -e "${YELLOW}requirements.txt not found, installing basic packages...${NC}"
    pip install django gunicorn whitenoise psycopg2-binary python-decouple pillow
fi

# Run database migrations
echo -e "${YELLOW}Running database migrations...${NC}"
python manage.py migrate

# Collect static files
echo -e "${YELLOW}Collecting static files...${NC}"
python manage.py collectstatic --noinput

# Start Gunicorn server
echo -e "${GREEN}Starting Gunicorn server...${NC}"
echo -e "${GREEN}Server will be available at: http://localhost:8000${NC}"
exec gunicorn --bind 0.0.0.0:8000 $PROJECT_NAME.wsgi:application