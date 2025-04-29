from flask import Flask

app=Flask(__name__)    #creating an instance of Flask for WSGI

@app.route('/')
def welcome():
    return "hello world, this is"

@app.route('/index')
def index():
    return "index page"

if __name__=="__main__":
    app.run(debug=True)