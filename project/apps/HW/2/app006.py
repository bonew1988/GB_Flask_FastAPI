from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def check_age(age):
    try:
        age = int(age)
        if age >= 18:
            return True
        else:
            return False
    except ValueError:
        return False


@app.route('/')
def index():
    return render_template('index3.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        if check_age(age):
            return render_template('result3.html', name=name, age=age)
        else:
            return render_template('error.html', message='Invalid age. You must be 18 or older.')


if __name__ == '__main__':
    app.run(debug=True)
