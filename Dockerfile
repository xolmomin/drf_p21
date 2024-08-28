FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]