from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/sum", methods=["GET"])
def numbers():
    num1 = request.args.get("num1", 0, type=int)
    num2 = request.args.get("num2", 0, type=int)
    sum_of = num1 + num2

    return render_template("zadanie_6a.html", sum_of = sum_of)


app.run(debug=True)