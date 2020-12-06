# Using python 3.8 in Alpine
FROM python:3.8-alpine3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run an update
RUN apk update

# Dependencies for Psycopg2
RUN apk add postgresql-dev gcc python3-dev musl-dev

# Dependencies for uWSGI
RUN apk add python3-dev build-base linux-headers pcre-dev

# Install the dependencies from requirements
RUN pip install -r requirements.txt

# In case bash is needed
#RUN apk add --no-cache bash

# Tell the port number the container should expose
EXPOSE 8083

# Run the command
ENTRYPOINT ["uwsgi", "app.ini"]