from flask import Flask, g

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    print("before requested")
    g.str = "hangul"

@app.route("/aa")    
def helloworld2():
    return "Hello world" + getattr(g, 'str', '111')

@app.route("/")    
def helloworld1():
    return "Hello world!"