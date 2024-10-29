# pull official base image
FROM ghcr.io/satellite-app/base_image:latest
LABEL org.opencontainers.image.source="https://github.com/Satellite-App/SatelliteAPI"
LABEL org.opencontainers.image.description="Auth service image"

# copy app
COPY . $APP_HOME/

# install python dependencies
RUN pip install -r $APP_HOME/requirements.txt --break-system-packages

# change to the app user
USER app

# expose port
ENV APP_PORT=8080
EXPOSE $APP_PORT

# run app
CMD python3 main.py
