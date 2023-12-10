from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/about/')
def about():
    return 'That\'s page about company'

@app.route('/contact/')
def contact():
    return 'Our contacts: comp@e-mail.com'



if __name__ == '__main__':
    app.run(debug=True)
