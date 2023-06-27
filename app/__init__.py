import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    #OG: return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))
    return render_template('index.html', url=os.getenv("URL"))

@app.route('/hobbies')
def hobby():
    return render_template('hobbies.html', url=os.getenv("URL"))