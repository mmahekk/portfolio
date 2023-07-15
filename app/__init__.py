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


if __name__ == '__main__':
    app.run(debug=True)
