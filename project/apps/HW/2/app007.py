from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = float(request.form['number'])
        square = number ** 2
        return redirect(url_for('result', number=number, square=square))
    return render_template('index4.html')


@app.route('/result/<float:number>/<float:square>')
def result(number, square):
    return render_template('result4.html', number=number, square=square)


if __name__ == '__main__':
    app.run(debug=True)
