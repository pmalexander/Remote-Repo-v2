from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
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
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))
    