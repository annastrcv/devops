#reference https://runnable.com/docker/python/dockerize-your-flask-application

FROM python:3.8
MAINTAINER Anna Startseva "anna.startseva.dir@gmail.com"
COPY ./requirements.txt /myapp/requirements.txt
WORKDIR /myapp
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir Flask flask_prometheus_metrics
COPY . /myapp
CMD [ "python", "main.py" ]



