from flask import Flask
from os import environ

app = Flask(__name__)

#constructs greeting for / and /root pages
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

#constructs a greeting for Patrick with image of kitten
@app.route("/hello/<name>")
def hello_person(name):
    html= """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here is a picture of a kitten. Awwwwww...
        </p>
        <img src="http://i.imgur.com/GvnvT8cb.jpg">
    """
    return html.format(name.title())

#takes first 3 letters of last name and first 2 letters of first name to combine into a Jedi name
@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    return last[:3]+first[:2]

if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))
    