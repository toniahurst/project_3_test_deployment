from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html", name="About Us")

if __name__ == "__main__":
    
    app.run(debug = True)
    


    