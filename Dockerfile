FROM python:3.10-slim

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=hydro.settings
ENV PYTHONPATH=/app:/app/hydro

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
