from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'some_secret_key'


@app.route('/')
def index():
    return render_template('index8.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    flash(f'Привет, {name}!')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
