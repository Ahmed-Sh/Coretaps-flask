from flask import render_template, request, redirect, url_for
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())
#    red posts is the one we handle in html


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        # Note "title and "content" should be same "name" as in  html form
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")
