from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index9.html')


@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        response = make_response(redirect(url_for('greeting')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)

        return response


@app.route('/greeting')
def greeting():

    username = request.cookies.get('username')
    return render_template('greeting.html', username=username)


@app.route('/logout')
def logout():

    response = make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
