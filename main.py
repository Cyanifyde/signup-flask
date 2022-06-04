from flask import Flask,session,render_template

app = Flask(__name__, template_folder='templates')
app.secret_key="regbergi45444"


@app.route("/")
def index():
    try:
        name=session["user"]["name"]
        return render_template("index.html",name=name,access=session["access"])
    except:
        session["user"]=""
        session["access"]=""
        return render_template("index.html",name="",access=session["access"])


from auth.auth import app as auth
app.register_blueprint(auth)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
