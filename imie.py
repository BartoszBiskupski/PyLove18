from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("imie.html", name = request.args.get("name", ""))


app.run(debug=True)