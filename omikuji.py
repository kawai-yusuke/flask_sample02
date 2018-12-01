import random

from flask import Flask, render_template

app = Flask(__name__)


def select_random(random_list):
    return random.choice(random_list)

@app.route("/omikuji")
def omikuji():
    return render_template("omikuji.html",omikuji = select_random(["大吉","吉","凶"]))

@app.route("/dice")
def dice():
    return render_template("dice.html",dice = select_random([a for a in range(1, 7)]))

if __name__ == '__main__':
    app.run(debug=True)