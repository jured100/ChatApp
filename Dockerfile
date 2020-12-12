FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt \
    python manage.py collectstatic --noinput
EXPOSE 8000
CMD env; python manage.py migrate --noinput; uvicorn base.asgi:application --host 0.0.0.0 --port 8000 --workers 3 --proxy-headers --forwarded-allow-ips 127.0.0.1,0.0.0.0
