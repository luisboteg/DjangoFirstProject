#Dockerfile
FROM python:3.8.5


EXPOSE 8000

COPY . /app


WORKDIR /app

RUN pip install -r requeriments.txt

RUN chmod +x *

CMD ["python3", "manage.py", "runserver","0.0.0.0:8000","--noreload"]
