# Put your app in here.
from flask import Flask,request
from operations import add, sub, mult, div

app = Flask(__name__)
@app.route("/add")
def add_route():
    """add 2 numbers"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = add(a,b)
    return str(answer)

@app.route("/sub")
def substract_route():
    """subtract 2 numbers"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = sub(a,b)
    return str(answer)

@app.route("/mult")
def multiply_route():
    """multiply 2 numbers"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = mult(a,b)
    return str(answer)

@app.route("/div")
def divide_route():
    """divide 2 numbers"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = divide(a, b)
    return str(answer)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
