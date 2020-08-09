from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

from app.models import model

app = Flask(__name__, static_folder='../../static', template_folder='../views')


@app.route("/", methods=['GET'])
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():

    user_datas = model.get_all()

    user_name = request.form.get("name")
    user_pass = request.form.get("pass")

    for user_data in user_datas:
        if user_name == user_data["name"]:
            if user_pass == user_data["pass"]:
                return redirect(url_for("success"))
            else:
                return redirect(url_for("fail"))
    return redirect(url_for("fail"))


@app.route("/success")
def success():
    return "login success"


@app.route("/fail")
def fail():
    return "login error"


def start():
    app.run(host='127.0.0.1', port=8080, threaded=True)