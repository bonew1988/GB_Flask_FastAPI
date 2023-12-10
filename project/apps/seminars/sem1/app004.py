# Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах. Таблица должна содержать следующие
# поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        {'name': 'Ivan', 'family': 'Ivanov', 'age': 24},
        {'name': 'Petr', 'family': 'Petrov', 'age': 34},
        {'name': 'Vlad', 'family': 'Orlov', 'age': 14}
    ]
    return render_template('table.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
