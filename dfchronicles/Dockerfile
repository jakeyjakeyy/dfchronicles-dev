FROM python:3.10
COPY . /app/backend
WORKDIR /app/backend
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
CMD ["gunicorn", "--config", "gunicorn_config.py", "backend.wsgi:application"]