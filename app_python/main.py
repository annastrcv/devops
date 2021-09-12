from datetime import datetime
import pytz as pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    time_zone = pytz.timezone("Europe/Moscow")
    time = datetime.now(time_zone).strftime('%H:%M:%S')
    return render_template('index.html', time=time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



