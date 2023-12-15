from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from faker import Faker

app = Flask(__name__)
fake = Faker()

# Создание базы данных и объявление базового класса
Base = declarative_base()

# Определение модели "Факультет"


class Faculty(Base):
    __tablename__ = 'faculties'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Определение модели "Студент"


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    group = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.id'))
    faculty = relationship('Faculty', back_populates='students')


# Определение обратной связи для модели "Факультет"
Faculty.students = relationship('Student', back_populates='faculty')

# Создание базы данных
# university.db - имя файла базы данных SQLite
engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
session = Session(engine)

# Пример добавления данных в базу данных
faculty1 = Faculty(name='Факультет1')
faculty2 = Faculty(name='Факультет2')

session.add_all([faculty1, faculty2])
session.commit()

# Генерация 25 фейковых студентов
for _ in range(25):
    student = Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=fake.random_int(min=18, max=30),
        gender=fake.random_element(elements=('М', 'Ж')),
        group=fake.random_element(elements=('Группа1', 'Группа2')),
        faculty=fake.random_element(elements=(faculty1, faculty2))
    )
    session.add(student)

session.commit()

# Маршрут для отображения списка студентов с указанием их факультета


@app.route('/')
def get_students_with_faculty():
    students_with_faculty = session.query(Student, Faculty).join(Faculty).all()
    return render_template('students.html', students_with_faculty=students_with_faculty)


# Если файл запускается напрямую, а не импортируется
if __name__ == '__main__':
    app.run(debug=True)
