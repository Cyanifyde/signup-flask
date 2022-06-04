
from flask import request,render_template,redirect,url_for,session, flash,Blueprint
from replit import db
from datetime import datetime

app = Blueprint('auth', __name__)
now = datetime.now()

def check_login():
    try:name=session["user"]["name"]
    except:name=""
    if name not in db.keys():
        session["access"]="False"
        return False
    elif int(now.strftime("%d%H"))+2<=int(session["user"]["time"]):
        session["access"]="False"
        return False
    else:
        return True

def set_time():
    session["user"]["time"]=now.strftime("%d%H")

app.secret_key = 'pohrjirtiou8646'
open_list=["/","/login","/signup"]

@app.before_request 
def before_request_callback(): 
    if not check_login():
        path=request.path
        if path not in open_list:
            flash("Session is over")
            return redirect(url_for('auth.login'))
    else: 
        set_time()
    

    
@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/login", methods=["POST"])
def loginPOST():
    data = request.form
    name=data["name"]
    password=hash(data["password"])
    if name in db.keys():
        if password==db[name]["password"]:
            session["user"]={"name":data["name"],"time":now.strftime("%d%H")}
            session["access"]="True"
            return redirect(url_for('auth.profile'))
        else:
            flash("wrong username/password")
            return redirect(url_for('auth.login'))
    else:
        flash("wrong username/password")
        return redirect(url_for('auth.login'))
            
    
@app.route("/profile")
def profile():
    return render_template("profile.html",access=session["access"])
    
@app.route("/signup")
def signup():
    return render_template("signup.html",access=session["access"])
    
@app.route("/signup", methods=["POST"])
def signupPOST():
    data = request.form
    if data["name"] not in db:
        session["user"]={"name":data["name"],"time":now.strftime("%d%H")}
        db[data["name"]]={"email":data["email"],"password":hash(data["password"]),"power":1}
        session["access"]="True"
        return redirect(url_for('index'))
    else:
        flash("Username in use")
        return redirect(url_for('auth.signup'))

@app.route("/signout")
def signout():
    session["user"]=""
    session["access"]="False"
    return redirect("/")
    
@app.route("/wipedb", methods=["GET"])
def wipe():
    for x in db.keys():
        del db[x]
