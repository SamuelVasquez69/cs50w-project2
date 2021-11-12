import os

from flask import Flask, render_template, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_session import Session
from datetime import date, datetime

from werkzeug.utils import redirect

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins = '*')

app.config["SESSION_TYPE"] = "filesystem"
Session(app)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

## pa guardar los usuarios
usuarios=[]

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/login", method=['GET','POST'])
def login():
    session.clear()
    usuario = request.form.get("username")

    if request.method == "POST":
        session["usuario"]=usuario

        return redirect("/")
    else:
        return redirect("/login")

@app.route("/logout", methods=['POST','GET'])
def logout():
    session.clear()
    return redirect("/")
    
