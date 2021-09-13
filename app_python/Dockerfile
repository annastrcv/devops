#reference https://runnable.com/docker/python/dockerize-your-flask-application

FROM python:3.8
MAINTAINER Anna Startseva "anna.startseva.dir@gmail.com"
COPY ./requirements.txt /myapp/requirements.txt
WORKDIR /myapp
RUN pip install -r requirements.txt
COPY . /myapp
CMD [ "python", "main.py" ]



