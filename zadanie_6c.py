from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/sum", methods=["POST"])
def numbers():
    if request.method == "POST":
        num1 = request.form("num1", 0)
        num2 = request.form("num2", 0)
        try:
            sum_of = int(num1) + int(num2)
        except Exception:
            sum_of = "Please put only numbers"
        return render_template("zadanie_6a.html", sum_of = sum_of)
        


app.run(debug=True)