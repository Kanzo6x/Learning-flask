from flask import Flask,request,make_response ,render_template

app = Flask(__name__,template_folder='Templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amr')
def amr():
    myname:str ='Amr Naser'
    mymessage:str ='hello my name is amr'
    return render_template('amr.html', myname=myname, mymessage=mymessage)


if __name__ == '__main__':
    app.run(debug=True, port=5000,host="0.0.0.0")

