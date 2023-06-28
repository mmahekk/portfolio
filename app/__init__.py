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

    # Data for individual 1
    educations_sydney = [
        {'title': 'Bachelor of Science, Double major in Computer Science and Biochemistry',  'year': '2018-2023',
         'institution': 'The University of British Columbia (UBC)'},
        {'title': 'High School Diploma', 'year': '2018',
         'institution': 'BC High School'}
    ]
    experiences_sydney = [
         {'title': 'Production Engineering Fellow', 'duration': 'Jun 2023 - Sept 2023', 'company': 'MLH'}
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

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), pages=pages,
                           educations_sydney=educations_sydney, experiences_sydney=experiences_sydney,
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

