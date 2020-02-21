import os
from flask import Flask, render_template
from routes import api
from jobs.cron import cron_job

app = Flask(__name__, template_folder='static')

app.register_blueprint(api)

@app.route("/")

def home():
    return render_template("index.html") ###opening index.html on load of application

if __name__ == '__main__':
    run_cron = int(os.environ.get("run_cron_job", 0)) ### getting environment variable to whether run the data load
    cron_job(run_cron) ###running the data load
    app.run()
