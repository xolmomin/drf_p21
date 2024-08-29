# FROM python:3.11-alpine - LINUX uchun
# FROM --platform=linux/amd64 python:3.11-alpine as build  - MAC uchun
FROM python:3.11-alpine as build

WORKDIR /app

COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]