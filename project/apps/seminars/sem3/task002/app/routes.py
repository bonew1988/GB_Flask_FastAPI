from app import app
from flask import render_template
from app.models import Book


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)
