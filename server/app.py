#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:num>')
def count(num):
    return "".join(f"{i}\n" for i in range(num))

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        return str(num1 + num2)
    elif op == '-':
        return str(num1 - num2)
    elif op == '*':
        return str(num1 * num2)
    elif op == 'div':
        return str(num1 / num2)
    elif op == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation', 400

if __name__ == '__main__':
    app.run(debug=True)

