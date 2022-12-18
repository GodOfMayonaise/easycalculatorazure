from flask import Flask

app = Flask("easycalculatorwebapp")

@app.route("/")
def hello_world():
    return """<p>Hello Worl!</p> <a href="/store>Store</a>"""

@app.route("/store")
def store():
    return "<p>This is the Store front!</p>"