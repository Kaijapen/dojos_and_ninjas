from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/")
def start_page():
    dojos_list = Dojo.get_all()
    return render_template("index.html", dojos_list = dojos_list)

@app.route("/add/dojo", methods=["POST"])
def add_dojo():
    data = {
        "name" : request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')