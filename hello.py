from flask import Flask,render_template,flash
# from flask_wtf import FlaskForm
# from wtforms import StringField,SubmitField
# from wtforms.validators import DataRequired
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3
# from datetime import datetime

#create a flask instance
app=Flask(__name__)

#Create a route decorator
@app.route('/')
# def index():
#     return "<h1> Hello world! </h1>"
def index():
    first_name="Anjali"
    something="This is <strong> BOLD TEXT </strong>"
    some_more_things="This is an <em> italic text </em>"
    best_fictional_chars=["Stefan","Chandler","Atlas","Monica","Lydia","Layken","Natasha",7,"Will","Stiles"]
    # flash("Welcome to my website!")
    return render_template("index.html",
                           f_name=first_name,
                           stuff=something,
                           some_other_stuff=some_more_things,
                           best_fictional_chars=best_fictional_chars)

#localhost:5000/user/Anjali
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

#Create custom error pages

#1.INVALID URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#2.INTERNAL SERVER ERROR
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__=="__main__":
    app.run(debug=True)