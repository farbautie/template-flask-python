#!/bin/bash

if [ ! -f .env ]; then
    echo "The .env file does not exist."
    exit 1
fi

source .env

if [ -z "$FLASK_ENV" ]; then
    echo "The FLASK_ENV environment variable is not set."
    exit 1
fi

if [ "$FLASK_ENV" = "development" ] || [ "$FLASK_ENV" = "debug" ]; then
    echo "Running in development/debug mode with Flask's built-in server..."
    flask run --host=0.0.0.0 --port=8000
else
    # Activate virtual environment
    source env/bin/activate
    echo "Running in production mode with Guvicorn..."
    gunicorn -w 4 --bind :8000  main:app
fi
