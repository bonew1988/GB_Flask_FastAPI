from flask import Flask


app = Flask(__name__)


@app.route('/<int:num1>/<int:num2>/')
def sum_two(num1: int, num2: int):
    return f'{num1} + {num2} = {num1 + num2}'


if __name__ == "__main__":
    app.run(debug=True)
