from flask import Flask, render_template, request

class Osoba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.surname, self.age)


Osoby_dane = {"Batman":["Bruce", "Wayne", 25], "Superman":["Clark", "Kent", 25]}


# Osoby = []
# lista_osob = locals().update(Osoby_dane)
#
# for key in Osoby_dane.keys():
#     lista_osob.append(key)
#     key = [Osoba(*Osoby_dane[key])]
#     Osoby.append(key)
#
# print(lista_osob)


Batman = Osoba("Bruce", "Wayne", 25)
Superman = Osoba("Clark", "Kent", 25)
Osoby = [Batman, Superman]


app = Flask(__name__)
@app.route("/osoby", methods = ["GET"])
def name():
    return render_template("zadanie_4.html", Osoby = Osoby)

app.run(debug=True)