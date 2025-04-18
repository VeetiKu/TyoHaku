from flask import Flask
import sqlite3
from flask import abort,redirect, render_template, request, session
import db
import re
import config
import items
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def check_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_items = items.get_items()
    return render_template("index.html", items=all_items)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    items = users.get_items(user_id)
    return render_template("show_user.html", user=user, items=items)

@app.route("/find_item")
def find_item():
    query = request.args.get("query")
    if query:
        results = items.find_items(query)
    else:
        query=""
        results = []
    return render_template("find_item.html", query=query, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    classes = items.get_classes(item_id)
    return render_template("show_item.html", item=item, classes=classes)

@app.route("/uusi_julkaisu")
def uusi_julkaisu():
    check_login()
    classes = items.get_all_classes()
    return render_template("uusi_julkaisu.html", classes=classes)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_item", methods=["POST"])
def create_item():
    check_login()
    
    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    author = request.form["author"]
    if not author or len(author) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 3000:
        abort(403)
    salary = request.form["salary"]
    if not re.search("^[1-9][0-9]{0,7}$", salary):
        abort(403)
    location = request.form["location"]
    if not location or len(location) > 50:
        abort(403)
    deadline = request.form["deadline"]
    user_id = session["user_id"]
    
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            parts = entry.split(":")
            classes.append((parts[0], parts[1]))
    
    items.add_item(title, author, description, salary, location, deadline, user_id, classes)
    
    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    check_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_item.html", item=item)

@app.route("/update_item", methods=["POST"])
def update_item():
    check_login()
    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    author = request.form["author"]
    if not author or len(author) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 3000:
        abort(403)
    salary = request.form["salary"]
    if not re.search("^[1-9][0-9]{0,7}$", salary):
        abort(403)
    location = request.form["location"]
    if not location or len(location) > 50:
        abort(403)
    deadline = request.form["deadline"]
    
    items.update_item(item_id, title, author, description, salary, location, deadline)
    
    return redirect("/item/" + str(item_id))

@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    check_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)
        
    if request.method == "GET":
        return render_template("remove_item.html", item=item)
    
    if request.method == "POST":
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:   
            return redirect("/item/" + str(item_id))


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"
    return '<p>Tunnus luotu! <a href="/">Palaa etusivulle</a></p>'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
    user_id = users.check_login(username, password)

    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        return redirect("/")
    else:
        return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["username"]
        del session["user_id"]
    return redirect("/")