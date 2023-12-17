# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранение пользователей (в реальном приложении используйте базу данных)
users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка соответствия логина и пароля
    if login in users and users[login] == password:
        # Если успешно, перенаправляем на страницу приветствия
        return redirect(url_for('welcome', username=login))
    else:
        # Если неуспешно, перенаправляем на страницу ошибки
        return redirect(url_for('error'))


@app.route('/welcome/<username>')
def welcome(username):
    return f'Привет, {username}! Добро пожаловать!'


@app.route('/error')
def error():
    return 'Ошибка входа. Пожалуйста, проверьте логин и пароль.'


if __name__ == '__main__':
    app.run(debug=True)
