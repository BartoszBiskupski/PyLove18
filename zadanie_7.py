from flask import Flask, request, render_template

app = Flask(__name__)

bands = ["Behemoth", "Vader", "Metallica", "Slayer", "Britnay Spears", "Spice Girls"]

@app.route("/bands", methods=["GET", "POST"])
def search():
    bands_todisplay = []
    band = request.args.get("band", "", type=str)
    for name in bands:
        if band.lower() in name.lower():
            bands_todisplay.append(name)
    if len(bands_todisplay) == 0:
        bands_todisplay = []
        bands_todisplay.append("No such bands")
    elif band == "":
        bands_todisplay = []
        bands_todisplay.append("No such bands")   

    return render_template("zadanie_7.html", bands_todisplay=bands_todisplay)


app.run(debug=True)
