#!/bin/bash -x

# Run webserver
gunicorn \
    --log-file '-' \
    --preload \
    --access-logfile '-' \
    --workers=${WEB_CONCURRENCY:-1} \
    --threads=${WEB_CONCURRENCY_THREADS:-1} \
    --bind 0.0.0.0:${PORT:-5000} \
    app.asgi:application \
    -k uvicorn.workers.UvicornWorker
