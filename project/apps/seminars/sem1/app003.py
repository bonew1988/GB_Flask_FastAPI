# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def world():
    return (f'<h1> "My first Page" </h1> <p> "Hell!" </p>')


if __name__ == '__main__':
    app.run(debug=True)
