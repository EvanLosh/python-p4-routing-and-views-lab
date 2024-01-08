#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    count_string = ""
    for i in range(int(parameter)):
        count_string += (str(i) + '\n')
    return count_string

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    x = int(str(num1))
    y = int(str(num2))
    if operation == '+':
        return str(x + y)
    if operation == '-':
        return str(x - y)
    if operation == '*':
        return str(x * y)
    if operation == 'div':
        return str(x / y)
    if operation == '%':
        return str(x % y)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
