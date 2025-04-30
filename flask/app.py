from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Hello<h1><html>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        marks=request.form['marks']
    if int(marks)>50:
        res="passed"
    else:
        res="failed"

    return render_template('result.html',name1=name,marks1=marks,result=res)

if __name__ == "__main__":
    app.run(debug=True)
