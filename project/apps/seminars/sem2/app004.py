# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('word_count.html')


@app.route('/count_words', methods=['POST'])
def count_words():
    text = request.form.get('text')
    word_count = len(text.split())
    return render_template('result.html', word_count=word_count, text=text)


if __name__ == '__main__':
    app.run(debug=True)
