from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello, NEW World!</p>"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    
    app.run(debug = True)
    