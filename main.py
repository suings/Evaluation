from flask import Flask
from flask import render_template
from flask import request
from pj import pj
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pj", methods=["POST"])
def p():
    u = request.form["u"]
    pwd = request.form["pwd"]
    try:
        result = pj(u,pwd)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return "500"
    if result == "pwd err":
        return "err"
    elif result =="success":
        return "success"
    elif result == "err":
        return "err"

if __name__ == '__main__':
    app.run(port=80)
