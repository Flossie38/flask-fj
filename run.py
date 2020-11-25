import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Choose from the below options")


@app.route("/search")
def search():
    return render_template("search.html", page_title="Search a recipe")


@app.route("/share")
def share():
    return render_template("share.html", page_title="Share your Yummy!")


@app.route("/breakfast")
def breakfast():
    return render_template("breakfast.html", page_title="Wholesome breakfasts!")


@app.route("/mains")
def mains():
    return render_template("mains.html", page_title="Luscious mains!")


@app.route("/dessert")
def dessert():
    return render_template("dessert.html", page_title="Decadent desserts!")


@app.route("/nibble")
def nibble():
    return render_template("nibble.html", page_title="Nibble and snacks")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
