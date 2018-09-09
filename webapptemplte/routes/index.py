from webapptemplte import app
from flask import render_template


@app.route("/userForm", methods=("GET", "POST"))
def User():
    return render_template("userForm.html")


