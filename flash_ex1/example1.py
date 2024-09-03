from enum import Enum
from random import randint, uniform
from threading import Thread
from time import sleep

from flask import Flask, render_template, request, redirect, url_for
from gpiozero import LEDBoard
from gpiozero.tools import random_values
import RPi.GPIO as GPIO

class TreeState(Enum):
    OFF = 1
    FLICKER = 2
    RANDOM_ON_OFF = 3
    ALL_FLASH = 4
    UP_AND_DOWN = 5
    TERMINATE = 6


def main_loop():
    while True:
        if state == TreeState.TERMINATE:
            tree.off()
            GPIO.cleanup()
            quit()

        if state == TreeState.ALL_FLASH:
            tree.on()
            sleep(1)
            tree.off()
            # to prevent you could set looping state = TreeState.OFF
            # state = TreeState.OFF

        if state == TreeState.RANDOM_ON_OFF:
            tree.off()
            for led in tree:
                s = randint(0,1)
                if s == 1:
                    led.on()
                else:
                    led.off()
            # state = TreeState.OFF

        if state == TreeState.UP_AND_DOWN:
            tree.off()
            order = list(range(1, 25)) + [0] 
            for item in order:
                    tree[item].on()
                    sleep(0.1)
            order.reverse()
            sleep(0.5)
            for item in order:
                    tree[item].off()
                    sleep(0.1)
            # state = TreeState.OFF

        # I have been unable to test this        
        if state == TreeState.FLICKER:
            for led in tree:
                led.source_delay = random.uniform(0.1, 0.9)
                led.source = random_values()
            sleep(1)

        # after a second repeat the loop
        sleep(1)

app = Flask(__name__)
state = TreeState.OFF
GPIO.setmode(GPIO.BCM)
tree = LEDBoard(*range(2, 28), pwm=True)


@app.route("/")
def home2():
    return render_template("home2.html", state=str(state))

# post-redirect-get
@app.route("/setState/<new_state>", methods=["POST"])
def setState(new_state):
    new_state = TreeState[new_state]
    global state
    state = new_state
    return redirect(url_for('home2'))

  
if __name__ == "__main__":
    Thread(name="backgroundLoop", target=main_loop).start()
    app.run(host='0.0.0.0', port=5000, debug=True)