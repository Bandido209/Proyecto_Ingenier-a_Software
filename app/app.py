from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hola mundo<h1>"
    integrantes = ["Esteban", "Benjamin", "Martin", "Sebastian", "Joaquin"]
    data = {
        "titulo": "index",
        "bienvenida": "¡Que onda!",
        "integrantes": integrantes,
        "num_in": len(integrantes)
    }
    return render_template(('index.html'), data=data)

if __name__ == '__main__':
    app.run(debug=True, port=1928)