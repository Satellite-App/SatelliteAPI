# pull official base image
FROM debian:12.2
LABEL org.opencontainers.image.source="https://github.com/Satellite-App/SatelliteAPI"
LABEL org.opencontainers.image.description="Base image for SatelliteAPI services"

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set python environment variables #
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies #
RUN apt-get update && apt-get -y install python3 python3-pip && apt-get clean
