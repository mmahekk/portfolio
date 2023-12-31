# Mahek Cheema - Portfolio Site ☆
![image](https://github.com/mmahekk/portfolio/assets/96924464/347bf008-e2de-4933-a701-d409a8c0d0a1)
![image](https://github.com/mmahekk/portfolio/assets/96924464/45006c04-ebd6-4d8a-beae-d22daefe5d84)
![image](https://github.com/mmahekk/portfolio/assets/96924464/1bf14c86-8044-41c8-9e9b-aabdabfd87c4)


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

