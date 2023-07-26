import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306
                     )

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


@app.route('/')
def index():
    pages = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Hobbies', 'url': '/hobbies'}
    ]

    # Data for individual 2
    educations_mahek = [
        {'title': 'Honours Bachelor of Science in Computer Science',  'year': '2022-2026',
         'institution': 'University of Toronto'},
        {'title': 'International Baccalaureate Diploma & Ontario Secondary School Diploma', 'year': '2018-2022',
         'institution': 'Turner Fenton Secondary School'}
    ]
    experiences_mahek = [
        {'title': 'Production Engineering Fellow', 'duration': 'Jun 2023 - Sept 2023', 'company': 'MLH'},
        {'title': 'Finance Associate Coordinator', 'duration': 'Mar 2023 - Jun 2023', 'company': 'Pepsico'}
    ]

    return render_template('index.html', title="Mahek Cheema", url=os.getenv("URL"), pages=pages,
                           educations_mahek=educations_mahek, experiences_mahek=experiences_mahek)


@app.route('/hobbies')
def hobby():
    pages = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Hobbies', 'url': '/hobbies'}
    ]
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), pages=pages)


@app.route('api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


if __name__ == '__main__':
    app.run(debug=True)
