from flask import Flask, render_template, request

class Osoba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.surname, self.age)


Osoby_dane = {"Bartek":["Bartek", "Biskupski", 32], "Vladimir":["Wlodzimir", "Slawiecki", 31]}


Osoby = []


print(Osoby)
app = Flask(__name__)
@app.route("/osoby", methods = ["GET"])
def name():
    global status
    for key in Osoby_dane.keys():
        Osoby.append([Osoba(*Osoby_dane[key])])
    return render_template("zadanie_4.html", Osoby = Osoby)

app.run(debug=True)