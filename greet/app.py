from flask import Flask

@app.route('/welcome')
def say_welcome():
    """Returns a welcome greeting"""

    return "welcome"
@app.route('/welcome/home')
def welcome_home():
    """Returns a welcome home"""

    return "welcome home"
@app.route('welcome/back')
def welcome_back():
    """Returns a welcome back"""

    return "welcome back"
