from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        titulo="Biblioteca Universitaria UDL-ICO",
        mensaje="¡Te damos la bienvenida a nuestra biblioteca universitaria!",
        active_page="inicio",
    )


@app.route("/catalogo")
def catalogo():
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Explora los materiales disponibles para apoyar tu aprendizaje e investigación.",
        active_page="catalogo",
    )


@app.route("/servicios")
def servicios():
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios que ponemos a tu disposición.",
        active_page="servicios",
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Estamos para orientarte. Aquí encontrarás nuestros medios de contacto y horario.",
        active_page="contacto",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5050)
