from flask import Flask


app = Flask(__name__)


html = '''
<h1>Привет!</h1>
<p>Какой-то текст...</p>
'''


@app.route('/')
def index():
    return 'Hi!'


@app.route('/text/')
def text():
    return html


if __name__ == '__main__':
    app.run()