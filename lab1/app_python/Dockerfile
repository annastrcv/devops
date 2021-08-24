#reference https://runnable.com/docker/python/dockerize-your-flask-application
FROM ubuntu:16.04
MAINTAINER Anna Startseva "anna.startseva.dir@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
COPY ./requirements.txt /myapp/requirements.txt
WORKDIR /myapp
RUN pip install -r requirements.txt
COPY . /myapp
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]



