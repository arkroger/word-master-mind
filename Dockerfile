# base image
FROM python:3.9.4-slim

RUN apt-get update

WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
#CMD ["gunicorn -w 4 "]
CMD gunicorn --workers $WORKERS --threads $THREADS  wordmastermind:app