# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from random import choice, randint
from flask import Flask, render_template
from .models_1 import Faculty, db, Student


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite'
db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    context = {
        'students': students
    }
    return render_template('index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')


@app.cli.command('fill-db')
def fill_db():
    for i in range(5):
        faculty = Faculty(faculty_name=f'Faculty {i + 1}')
        db.session.add(faculty)
        for j in range(3):
            student = Student(
                name=f'Student {j + 1}',
                last_name='Last Name',
                age=randint(18, 30),
                gender=choice([True, False]),
                group='INF-1',
                faculty=faculty
            )
            db.session.add(student)
    db.session.commit()
    print('DB Filled!')


if __name__ == '__main__':
    app.run(debug=True)
