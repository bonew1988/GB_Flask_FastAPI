from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index11.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Обработка загрузки файла (ваш код обработки файла здесь)
        return "Файл успешно загружен!"

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
