from flask import Flask, render_template
from docx import Document
from python_docx_replace import docx_replace

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/doc")
def document():
    document = Document("templates/OffenderPaperLetter.docx")
    docx_replace(document, prisoner_first_name="JIMBO THE HIMBO!!!", prisoner_last_name="THE RULER OF EVERYTHING!")
    string = ""
    for paragraph in document.paragraphs:
        string += paragraph.text
    return string

if __name__ == "__main__":
    app.run()