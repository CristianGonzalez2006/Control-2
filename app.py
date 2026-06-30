from flask import Flask, jsonify, request

app = Flask(__name__)

#repositorio temporal de datos
#No representa persistencia de datos
libros = {
    101: 
         {"id": 101, "titulo": "Clean code", "autor": "Robert C. Martin", "disponible": True},
    102: 
         {"id": 102, "titulo": "Python Crash C", "autor": "Eric Matthes", "disponible": True},
    103: 
         {"id": 103, "titulo": "Architecture Patterns", "autor": "GoF", "disponible": False},
}

@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "API REST de biblioteca universitaria",
            "version": "1.0",
            "endpoints": [
                "GET /libros", # Muestra todos los libros
                "GET /libros/<id>", # Información de un libro
                "POST /libros", # Crear un nuevo libro
                "PUT /libros/<id>", # Modificar la disponibilidad 
                "DELETE /libros/<id>", # Borrar un libro
            ]
        }
    )


if __name__ == '__main__':
    app.run(debug=True)