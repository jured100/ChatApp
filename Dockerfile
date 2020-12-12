FROM python:3.8
ENTRYPOINT ["/bin/bash"]
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
#CMD ["uvicorn", "base.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "3", "--proxy-headers", "--forwarded-allow-ips", "127.0.0.1,0.0.0.0"]
CMD [ "./manage.py", "migrate", "&&", "./manage.py", "runserver", "0.0.0.0:8000" ]
