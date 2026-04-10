from flask import Flask, render_template, request, url_for
from database import conectar 

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():

    usuario = request.form["txtusuario"]
    password = request.form["txtcontrasena"]
    rolusu = request.form["txtrol"]
    documento = request.form["txtdocumento"]

    con = conectar()
    cursor = con.cursor()

    sql = """INSERT INTO usuarios(usuario, PASSWORD, rol, documentoEmple) 
             VALUES (%s, %s, %s, %s)"""

    cursor.execute(sql, (usuario, password, rolusu, documento))
    con.commit()

    return "usuario guardado"

if __name__ == "__main__":
    app.run(debug=True)