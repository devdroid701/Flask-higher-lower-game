from flask import Flask
import random

app = Flask(__name__)


def make_image(function):
    def wrapper():
        text = function()
        return f'<img src={text}>'

    return wrapper


def random_no():
    return random.randint(1, 10)

chosen = 0

@app.route('/')
# @make_image
def welcome():
    global chosen
    chosen= random_no()
    print(chosen)
    return "<h1>Guess a number between 1 and 10</h1><img src=https://media1.tenor.com/images/f498c19076a8f51a7369303c00c1736c/tenor.gif?itemid=5789210>"


# for i in range(11):
@app.route('/<int:guess>')
def guess_checker(guess):
    global chosen

    if guess > 11 or guess < 0:
        return "<h1>Guess a number between the 1 and 10.</h1><br>" \
               "<img src=https://media1.tenor.com/images/3721598372d9890bc5faad05e03a6aeb/tenor.gif?itemid=10535329 width=300>" \
               "<img src=https://media1.tenor.com/images/12b3b5a0fd2ff64136509dea171b1df4/tenor.gif?itemid=11667704>"
    else:

        if guess > chosen:
            return f"<h1>Too high. Try Again</h1><img src=https://media1.tenor.com/images/a5753f3cd199b1a0c991872ccdff2ab1/tenor.gif?itemid=5352486 width=300>"
        elif guess < chosen:
            return f"<h1>Too low. Try Again</h1><img src=https://media1.tenor.com/images/a45356802a4b72bc7522574c5b5f68d0/tenor.gif?itemid=7382237 width=300>"
        elif guess == chosen:
            return f'<h1>You won!!</h1><img src=https://media1.tenor.com/images/c90703197e21fa2d3c0e67b841844cd9/tenor.gif?itemid=8665092 width=300>'