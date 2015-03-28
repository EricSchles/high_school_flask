from flask import Flask, has_request_context, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
class Log(db.Model):
    __tablename__ = "log"
    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(300))
    def __init__(self,ip_addr):
        self.ip_addr = ip_addr
    def __repr__(self):
        return '<ip_address %r>' % self.ip_addr

@app.route("/",methods=["GET","POST"])
def index():
    remote_addr = request.remote_addr
    log = Log(remote_addr)
    db.session.add(log)
    db.session.commit()
    return render_template("index.html")

if __name__ == '__main__':
        app.run(debug=True)
