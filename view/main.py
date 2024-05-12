from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def mainpage_render():
    testvar = "Test variable"
    return render_template("mainpage.html", testvar=testvar)
