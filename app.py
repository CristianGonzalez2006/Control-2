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
    
@app.get("/libros")
def obtener_libros():
    return jsonify(list(libros.values()))

@app.get("/libros/<int:id>")
def obtener_libro(id):
    libro = libros.get(id)
    
    if libro:
        return jsonify(libro)
    else:
        return jsonify({"error": "Libro no encontrado"}), 404
        
app.post("/libros")
def agregar_libro():
    datos = request.get_json()
    
    if not datos:
        return jsonify({"error": "Debe eneviar información"}), 400
    if "titulo" not in datos or "autor" not in datos:
        return jsonify({"error": "Los campos son requeridos"}), 400
    
    nuevo_id = max(libros.keys()) + 1

    libros[nuevo_id] = {
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "disponible": datos["Disponible"]
        
    }

    return jsonify({libros[nuevo_id]}), 201

if __name__ == '__main__':
    app.run(debug=True)