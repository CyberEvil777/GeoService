import os

bind = '0.0.0.0:8000'
workers = os.getenv('GUNICORN_WORKERS', 3)
reload = True
