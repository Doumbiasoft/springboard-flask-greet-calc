from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def say_welcome():
    html= f"""
    <html>
        <head>
        <title>Welcome!</title>
        </head>
        <body>
        <h1>Welcome</h1>
        </body>
    </html>
    """
    return  html


@app.route("/welcome/<string:greet>")
def say_welcome_something(greet):
    html= f"""
    <html>
        <head>
        <title>Welcome {greet}!</title>
        </head>
        <body>
        <h1>Welcome {greet}</h1>
        </body>
    </html>
    """
    return  html
