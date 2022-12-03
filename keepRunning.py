from flask import Flask
from threading import Thread

#Using uptimeRobot to ping the bot every 5 mins to keep it from auto sleeping

app = Flask('')


@app.route('/')
def home():
    return "Live"


def run():
    app.run(host='0.0.0.0', port=8080)


def keepLive():
    t = Thread(target=run)
    t.start()
