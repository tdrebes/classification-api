FROM python:3.12.3-slim-bullseye

# copy requirements into image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the dependencies
RUN pip install -r requirements.txt

# copy files to image
COPY . /app

# download models
RUN python /app/download_models.py

CMD [ "gunicorn", "-b", "0.0.0.0:5002", "--timeout=120", "app:app" ]
