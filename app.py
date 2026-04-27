from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

'''@app.route("/mecano")
def mecano():
    return render_template("mecano.html")

@app.route("/hadas")
def hadas():
    return render_template("hadas.html")

@app.route("/sol")
def sol():
    return render_template("sol.html")

@app.route("/suelo")
def suelo():
    return render_template("suelo.html")
'''

@app.route("/album/<int:id>")
def album(id):
    match id:
        case 1:
            return render_template("detalle_album.html",
                                nombre="Mecano (1981)",
                                imgnum="1",
                                albumid="2n1N39ZjNXxzoyDkYm6yid")
        case 2:
            return render_template("detalle_album.html",
                                nombre = "¿Dónde está el país de las hadas?",
                                imgnum="2",
                                albumid="395Ts8cMrWtmDHxrlYcTxz")
        case 3:
            return render_template("detalle_album.html",
                                nombre = "Ya viene el sol",
                                imgnum="3",
                                albumid="1m3nnPAQcMKR86QDfWsguj")

        case 4:
            return render_template("detalle_album.html",
                                nombre = "Entre el cielo y el suelo",
                                imgnum="4",
                                albumid="1vDYLED9bQwm3FzIdXs5H9")



if __name__ == "__main__":
    app.run(debug=True)
