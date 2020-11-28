import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html", page_title="Choose from the below options")


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #CHECK IF USER EXISTS
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("  Ooops! That Username already exists - Please choose another  ")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("You are registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect login details!  Please try again!")
                return redirect(url_for("login"))

        else:
            flash("Incorrect login details!  Please try again!")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Log in")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #grab username from database
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are logged out of Yummy!  See you next time!")
    session.pop("user")
    return redirect(url_for("login"))


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