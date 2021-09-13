from datetime import datetime
import pytz as pytz
from flask import Flask, render_template
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)


@app.route("/")
def index():
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    return render_template('index.html', time=time)


# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.0.1", app_config="staging")


# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)
