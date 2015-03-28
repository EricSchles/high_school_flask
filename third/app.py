from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index(name=None):
    things= {
        "Job":"Developer Evangelist @ Syncano",
        "Passion":"Music/Ending Slavery",
        "Contact":"eric.schles@syncano.com"
        }
    return render_template("index.html",name=name,things=things)

app.run(debug=True)
