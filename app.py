from flask import Flask, render_template
from docx import Document

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/doc")
def document():
    document = Document("templates/OffenderPaperLetter.docx")
    string = ""
    for paragraph in document.paragraphs:
        string += paragraph.text
    return string

if __name__ == "__main__":
    app.run()