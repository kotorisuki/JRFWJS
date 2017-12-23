from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/<int:page_id>")
def page(page_id):
    return render_template("page%d.html" % page_id)

if __name__ == "__main__":
    app.run()
