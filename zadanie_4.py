from flask import Flask, render_template, request

class Osoba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __repr__(self):
        return "name: {}, surname: {}, age: {}".format(self.name, self.surname, self.age)


Osoby_dane = {"Bartek":["Bartek", "Biskupski", 32], "Vladimir":["Wlodzimir", "Slawiecki", 31]}


Osoba1 = Osoba(*Osoby_dane["Bartek"])
Osoba2 = Osoba(*Osoby_dane["Vladimir"])

Osoby_list = Osoby_dane.keys()
print(Osoby_list)
def Osoby():
    for osoba in Osoby_list:
        return Osoba(*Osoby_dane[osoba])

print(Osoby())

# app = Flask(__name__)
# @app.route("/osoby", methods = ["GET"])
# def name():
#
