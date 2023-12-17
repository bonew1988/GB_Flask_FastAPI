from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = calculate(num1, num2, operation)
        return render_template('result1.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
