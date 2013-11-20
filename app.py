from flask import Flask, render_template, redirect, url_for
from sh import totem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play/')
@app.route('/pause/')
def play_pause():
    totem("--play-pause") 
    return redirect(url_for('index'))

@app.route('/volume/up/')
def volume_up():
    totem("--volume-up")
    return redirect(url_for('index'))

@app.route('/volume/down/')
def volume_down():
    totem("--volume-down")
    return redirect(url_for('index'))

@app.route('/fullscreen/')
def fullscreen():
    totem('--fullscreen')
    return redirect(url_for('index'))

@app.route('/seek/backward/')
def backward():
    totem('--seek-bwd')
    return redirect(url_for('index'))

@app.route('/seek/foreward/')
def forward():
    totem('--seek-fwd')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
