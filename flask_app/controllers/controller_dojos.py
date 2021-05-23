from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_dojos import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_dojo():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    return render_template("result.html", name = name, location = location, language = language, comment = comment )
