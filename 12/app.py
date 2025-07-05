from flask import Flask  

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá mundo do docker! Me chamo TM22!"

@app.route("/square/<int:number>")
def square(number):
    return str(number * number)

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


