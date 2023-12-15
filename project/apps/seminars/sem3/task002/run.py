from app import app, db
from app.models import Author, Book
from faker import Faker
import random

fake = Faker()

# Функция для создания случайных данных и добавления их в базу данных


def generate_fake_data(num_records):
    for _ in range(num_records):
        author = Author(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        db.session.add(author)
        db.session.commit()

        book = Book(
            title=fake.sentence(nb_words=3),
            year=fake.random_int(min=1900, max=2022),
            copies=fake.random_int(min=1, max=10),
            author_id=author.id
        )
        db.session.add(book)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Здесь 10 - количество записей, которые вы хотите добавить
        generate_fake_data(10)
    app.run(debug=True)
