from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.path.join(
    os.path.dirname(__file__), 'templates'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        return render_template('result.html', name=name, phone=phone)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
