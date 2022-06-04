import json
from flask import Flask, request, jsonify,render_template,redirect,url_for,session, flash
import uuid
from replit import db
from users.user import user,get_id
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

def check_login(user):
    #check user exists
    #check if time is not 1h off stored time
    pass

def set_time(user):
    #set cookie time to be current time
    pass






import os

app = Flask(__name__)
app.secret_key = 'pohrjirtiou8646'


@app.route("/")
def index():
    try:
        name=session["user"]["name"]
        return render_template("index.html",name=name)
    except:
        return render_template("index.html")
    
@app.route("/login")
def login():
   return render_template("login.html")


    
@app.route("/profile")
def profile():
   return render_template("profile.html")
    
@app.route("/signup")
def signup():
   return render_template("signup.html")
    
@app.route("/signup", methods=["POST"])
def signupPOST():
    data = request.form
    if data["name"] not in db:
        session["user"]={"email":data["email"],"name":data["name"],"time":now.strftime("%d%H")}
        db[data["name"]]={"email":data["email"],"password":hash(data["password"])}
        return redirect(url_for('index'))
    else:
        flash("name in use")
        return redirect(url_for('signup'))
        


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",port=8080, debug=True)
    except:
        os.system("python main.py")