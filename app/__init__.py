import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    pages = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Hobbies', 'url': '/hobbies'}
    ]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), pages=pages)


@app.route('/hobbies')
def hobby():
    pages = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Hobbies', 'url': '/hobbies'}
    ]
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), pages=pages)


if __name__ == '__main__':
    app.run(debug=True)
