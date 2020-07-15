from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
        return request.form['texttoreverse'][::-1]

if __name__ == '__main__':
    app.run()