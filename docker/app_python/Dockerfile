FROM python:3.8.6-slim-buster
MAINTAINER "Boon SUI <boonsuli@gmail.com>"
WORKDIR /app

# copy the dependencies file
COPY ./docker/app_python/requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory
COPY app_python /app

# set env variable
ENV FLASK_ENV = "docker"

# run server
CMD [ "python", "manage.py", "runserver" ]
