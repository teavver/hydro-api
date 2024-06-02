FROM python:3.10-slim

RUN apt-get update && apt-get install -y

WORKDIR /app/hydro

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy the project files
COPY . /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=hydro.settings
ENV ENV docker

EXPOSE 8000

# Run the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
