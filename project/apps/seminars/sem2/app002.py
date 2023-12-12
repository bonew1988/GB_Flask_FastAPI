from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Добавим функцию для создания папки, если она не существует


def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    image_path = request.args.get('image_path')
    return render_template('index.html', image_path=image_path)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', image_path=None)

        create_upload_folder()  # Создаем папку, если ее нет

        file = request.files['image']

        if file.filename == '':
            return render_template('index.html', image_path=None)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('index', image_path=filename))

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
