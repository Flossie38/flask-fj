import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.SECRET_KEY = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html", page_title="Choose from the below options")


@app.route("/resister", methods=["GET", "POST"])
def register():
    return render_template("register.html", page_title="Log in or Register")


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
