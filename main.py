from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/Senior")
def senior_team():
    return render_template("Senior.html")

@app.route("/Young")
def young_team():
    return render_template("Young.html")

if __name__ == '__main__':
    app.run()
