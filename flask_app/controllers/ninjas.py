from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas/<int:dojo_id>")
def dojo_table(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    dojo = Ninja.get_one_dojo(data)
    print(dojo)
    return render_template("dojo_ninjas.html", dojo=dojo)

@app.route("/ninja/add")
def add_ninja_page():
    dojos_list = Dojo.get_all()
    return render_template("add_ninja.html", dojos_list=dojos_list)

@app.route("/ninja/submit", methods=["POST"])
def submit_new_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo']
    }
    Ninja.create_ninja(data)
    return redirect('/')
