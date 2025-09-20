from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    # print to the server console
    print(word)
    # and return it in the browser
    return word

@app.route('/count/<int:n>')
def count(n):
    """
    Display numbers from 0 up to n-1, each on its own line.
    """
    return "\n".join(str(i) for i in range(n)) +"\n"

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    """
    Perform a math operation on two numbers.
    Supported: +, -, *, div, %
    """
    # convert inputs
    try:
        n1 = int(num1)
        n2 = int(num2)
    except ValueError:
        return "Invalid numbers", 400

    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == 'div':
        result = n1 / n2 if n2 != 0 else "Infinity"
    elif operation == '%':
        result = n1 % n2 if n2 != 0 else "Undefined"
    else:
        return f"Invalid operation: {operation}", 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

