from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from enum import Enum

class State(Enum):
    OFF = 1
    FLICKER = 2
    RANDOM_ON_OFF = 3
    ALL_FLASH = 4
    UP_AND_DOWN = 5
    TERMINATE = 6

def main_loop():
    while True:
        if state == State.TERMINATE:
            print("terminate")
            quit()

        if state == State.ALL_FLASH:
            print("all flash")

app = Flask(__name__)
state = State.OFF

@app.route('/')
def index():
    #return 'Hello world'
    return render_template('index2.html', state=str(state))


@app.route('/cakes')
def cakes():
    #return 'Yummy cakes!'
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    #return 'Hello %s' % name
    return render_template('page.html', name=name)

# post-redirect-get
@app.route("/setState/<new_state>", methods=["POST"])
def setState(new_state):
    new_state = State[new_state]
    global state
    state = new_state
    return redirect(url_for('index'))


   
if __name__ == "__main__":
    Thread(name="backgroundLoop", target=main_loop).start()
    app.run(host='0.0.0.0', port=5000, debug=True)
