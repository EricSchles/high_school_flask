#referencing the framework
from flask import Flask, render_template

app = Flask(__name__)

#use of our first decorator
@app.route("/",methods=["GET","POST"])
def start():
	return "Hello there"

#a second web address
@app.route("/index",methods=["GET","POST"])
@app.route("/index/<name>",methods=["GET","POST"])
def index(name=None):
	if name:
		return render_template("index.html",name=name)
	else:
		return render_template("index.html")

app.run(debug=True)
