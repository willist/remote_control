from flask import Flask, render_template, redirect, url_for, flash
from sh import totem, ErrorReturnCode

from contextlib import contextmanager

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'cheese'


@contextmanager
def hide_errors():
    try:
        yield
    except ErrorReturnCode:
        flash('Oops, I screwed something up.')        


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play/')
@app.route('/pause/')
def play_pause():
    with hide_errors():
        totem("--play-pause") 
    return redirect(url_for('index'))

@app.route('/volume/up/')
def volume_up():
    with hide_errors():
    	totem("--volume-up")
    return redirect(url_for('index'))

@app.route('/volume/down/')
def volume_down():
    with hide_errors():
        totem("--volume-down")
    return redirect(url_for('index'))

@app.route('/fullscreen/')
def fullscreen():
    with hide_errors():
        totem('--fullscreen')
    return redirect(url_for('index'))

@app.route('/seek/backward/')
def backward():
    with hide_errors():
        totem('--seek-bwd')
    return redirect(url_for('index'))

@app.route('/seek/foreward/')
def forward():
    with hide_errors():
        totem('--seek-fwd')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
