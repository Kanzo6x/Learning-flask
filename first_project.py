from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>HELLO WORLD</h1"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5555,debug=True)