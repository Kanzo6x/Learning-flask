from flask import Flask, make_response,request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "<h1>hello world</h1>"

@app.route("/say_a_message/<name>")
def say_something(name):
    return f"<h1>hello {name}</h1>"

@app.route("/sum/<int:a>/<int:b>")
def sumition(a:int,b:int):
    return f"<h1>sum of {a} and {b} is {a+b}</h1>"

@app.route("/handle_params")    #/handle_params?firstName=amr&secondName=ahmed&first=23&second=60&third=45.231   (unitest)
def handle_params():
    return request.args  # this return a dictionary with the arguments you have passed in the url 

@app.route("/more_handling")   #/more_handling?greeting=hello&firstName=amr
def more_handling():
    greeting = request.args.get("greeting")
    firstName = request.args.get("firstName")
    return f"{greeting} {firstName}"


@app.route("/hello_amr", methods=["GET","POST"])
def hello_amr():
    if request.method == "POST":
        return "you have sent a post request"
    else:
        return "you have sent a get request"

@app.route("/error") #/error
def error_handling():
    return "<h1>ERROR 404</h1>",404


#CUSTOM RESPONSES 
@app.route("/custom_respone") #/custom_respone
def custom_respone():
    response = make_response("hello world")
    response.status_code = 202
    return response 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)