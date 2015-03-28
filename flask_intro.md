#Introduction to Flask
####By Eric Schles

#About me (Call me Eric)

* **[linkedin]()**
* **[github](http://www.github.com/EricSchles)**
* **hobbies**:
	* Break dancing / swing dancing
	* Juggling / hacky-sack / rock climbing / frisbee
	* guitar / piano / ukulele
* **Areas of Interest**:
	* _Computational Interests_
		* Natural language processing:
		* Predictive Mathematics / Statistics:
	* _Theoretical Interests_
		* Algebra:
		* Topology:
		* Combined Topics:
		* Meme Theory
	* _Economics_
		* International Economics
		* Econometrics
		* Environmental Economics
		* Financial Economics
		* Macro Economics
		* Micro Economics		
* **languages**
	* Python
	* JavaScript
	* Java
	* C++
	* HTML/CSS
	* R
	* x86
* **languages I'd like to learn**
	* Go
	* OCAML
	* Haskell
	* Lua
	* Scheme
	* C
	* COBOL
	* Fortran
	* MIPS
	* Scala
	* Groovy
	* Ruby
	* Erlang


##Prerequisites

The Flask framework requires understanding of the following concepts:

* Decorators
* The Model, View, Controller (MVC) design pattern

###Decorators

Decorators are functions that take in functions as parameters and then augment the function in someway. Either by doing something before the function is called, doing something after the function is called, or both.

A first example:

```
def functor(f):
	def wrapper(*args,**kwargs):
		print "First print this out"
		f()
		print "Last print this out"
	return wrapper

@functor
def func():
	print "Hello there"

func()
```

As you can see, we define a wrapper function inside the first function.  Inside this inner function we process the the function that is passed in as an argument.
We then return the inner function at the end of the function definition.  This is what allows us to use this function as a decorator for other functions.

For a full understanding of decorators please do check out [this great reference](https://freepythontips.wordpress.com/2013/10/10/all-about-decorators-in-python/).

A Second example:

Okay - so we can make our code more confusing and abstract, _great_.  Now why would we ever want to do that?  As the next example shows, decorators are actually very powerful.  They allow you to do inspection on your code, very gracefully - like checking how long the running time of a given piece of code will take or by doing formatting transformations easily and with a great degree of modularity.

```
from time import time
def currency(f):
    def wrapper(*args,**kwargs):
        return "$" + str(f(*args,**kwargs)[0])
    return wrapper

def logger(f):
 	def wrapper(*args,**kwargs):
        start = time()
        result = f(args)
        print f.__name__,"ran in:", time() - start
        return result
    return wrapper

@logger
@currency
def dollars(amount):
    return amount

print dollars(5.00)
print dollars(60)

```

Here we see currency and logger - two great decorators that can be used again and again.

_references_:
	
	* [first reference](https://freepythontips.wordpress.com/2013/10/10/all-about-decorators-in-python/) 

	*[decorators and classes](http://stackoverflow.com/questions/13852138/how-can-i-define-decorator-method-inside-class)
##Web Development - the Forrest and the Trees
* Understanding of Front end (client side):
	* Understanding of HTML
	* Understanding of CSS
	* Understanding of templating engines
	* Understanding of Javascript
* Understanding of Back end (server side):
	* Understanding of Servers
	* Understanding of OSI model - HTTP, TCP/IP, and DNS
	* Understanding of Web Datastructures - Packets
	* Understanding of Cybersecurity best practices:
		* Prevention of cross-site scripting 
		* Prevention of SQL injection
		* Prevention of DDoS attacks
		* Prevention of Spoofing
		* Understanding of server logging
		* Setting up security in depth (many layers of security)
	* Understanding of Database concerns:
		* Sharding of data
		* load balancing
		* database optimization through indexing, etc.
		* Datastore connectivity
		* Database anonimization/Differential privacy

##What Flask does

Flask is a minimal web development framework, that makes it easy to build a website in just a few lines of code.  The goal of flask is to give you exactly what you need and nothing more to get the job done.  

###A First example:

```
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
```

Here we see a minimal Flask app.  This is technically all the code you need to know - if you want to build very simple websites.  

We make use of app.route - a decorator - that takes a parameter which defines the relative url to a given action.  If you type this url into the browser (with the server running) the code defined in the method decorated will be executed.  Notice the second parameter - methods.  This defines the HTTP methods that the url accepts.  If you want users to be able to view data from the server make sure "GET" is in your list of methods.  If you want users to be able to send data to the server make sure "POST" is in your list of methods.

Notice also the app.run method.  This is what starts up the server.  If we want to be able to hotswap our code, we need only pass debug=True to the app.run.

####Dealing with our views

index.html
```
<!doctype html>
<html>
<head>
</head>
<body>
	<p>
		Hello there {{name}}
	</p>	 

</body>

</html>

```
 
Now that we know what our routes do, let's understand how to manipulate data that we send to the server.  Notice in our index method we have the following line:

`return render_template("index.html",name=name)`.

Here we are passing a variable name to our rendering engine - jinja2.  We name the variable that will be viewed in the HTML (the parameter on the left hand side of the equals sign) the same as the variable that we define here - in our middleware (the controller) (the variable on the right hand side of the equals sign).

Notice now that index.html contains a variable name contained in curly braces like this - {{ }}.  These double curly braces tell our templating engine to execute whatever python code exists in here.  In this case, name is executed and replaces the {{name}} when the server is run. 
  
###A Slightly more complete example:

Now that we understand the basics of setting up routes and passing data to our view we can add a little more control.  

```

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/<functionality>",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index(functionality):
	if functionality == "redirect":
		redirect("/hello")
	elif functionality == "redirect2":
		redirect(url_for("hi_there"))
	else:
		return render_template("index.html")

@app.route("/hello",methods=["GET","POST"])
def hello():
	return "Hello"

@app.route("/hi_there",methods=["GET","POST"])
def hi_there():
	return "Hi there"

app.run(
	debug=True,
	host="0.0.0.0", #broadcast mode
	port=5000
 )
	
```

Here notice that we can use redirects as well as simply loading the page.  A redirect allows multiple addresses to point to the same content (hurray).  Notice also that we added host and port to our parameter list.  Setting the host to 0.0.0.0 allows the url to be broadcast across any local area network.  So you can now write local websites for your home network or any set of devices all connected through one router (from a practical perspective).  Of course, you need to use a hosting service to connect to the world wide web.


###Flow of control/Iteration in your HTML

Now that we know how to send data to our front end, let's process it in our templating engine, for real.

index.html
```
<!doctype html>
<html>
<head></head>
<body>

{% if name=="Eric" %}
<p>Hello Eric</p>
{% else %}
<p>Hello there</p>
{% endif %}

<ul>
{% for key in things.keys() %}
<li> {{key}} : {{things[key]}}</li>
{% endfor %}
</ul>
</body>
</html>
```

app.py
```
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
```

So here we see more of the power of flask, the ability to loop through data structures as well as the ability to control who sees what content.

### Databases

Now that we understand how to manipulate data on the front end, let's learn how to store it on the back end and then finally, we'll create our own API's.

```
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
```

Before running our app we need to do the following

open a terminal and run:

```
python
>>> from app import db
>>> db.create_all()
```
