import couchdb
import os

# Leer las variables de entorno para la conexión a CouchDB
COUCHDB_USER = os.environ.get("COUCHDB_USER", "admin")
COUCHDB_PASSWORD = os.environ.get("COUCHDB_PASSWORD", "admin123")
COUCHDB_HOST = os.environ.get("COUCHDB_HOST", "127.0.0.1")
COUCHDB_PORT = os.environ.get("COUCHDB_PORT", "5984")

# Conectar a CouchDB
couch_server = couchdb.Server(f"http://{COUCHDB_USER}:{COUCHDB_PASSWORD}@{COUCHDB_HOST}:{COUCHDB_PORT}/")
db_name = 'recommendation_system'

try:
    db = couch_server.create(db_name)  # Intentar crear la base de datos si no existe
except couchdb.http.PreconditionFailed:
    db = couch_server[db_name]  # Si ya existe, usar la existente

# Función para consultar usuarios por ID, nombre, carrera o semestre
def consultar_usuario(key, value):
    try:
        vista = db.view('usuarios/por_' + key, keys=[value])
        for fila in vista:
            usuario = fila.value
            print(f"Usuario encontrado - ID: {fila.id}, Nombre: {usuario['nombre']}, Carrera: {usuario['carrera']}, Semestre: {usuario['semestre']}")
    except Exception as e:
        print(f"Error al consultar usuarios: {e}")

# Función para consultar tutores por ID, nombre, carrera o calificación promedio
def consultar_tutor(key, value):
    try:
        vista = db.view('tutores/por_' + key, keys=[value])
        for fila in vista:
            tutor = fila.value
            print(f"Tutor encontrado - ID: {fila.id}, Nombre: {tutor['nombre']}, Carrera: {tutor['carrera']}, Calificación Promedio: {tutor['calificacionPromedio']}")
    except Exception as e:
        print(f"Error al consultar tutores: {e}")

# Función para consultar cursos por ID, nombre, categoría o modalidad
def consultar_curso(key, value):
    try:
        vista = db.view('cursos/por_' + key, keys=[value])
        for fila in vista:
            curso = fila.value
            print(f"Curso encontrado - ID: {fila.id}, Nombre: {curso['nombre']}, Categoría: {curso['categoria']}, Modalidad: {curso['modalidad']}, Precio: {curso['precio']}")
    except Exception as e:
        print(f"Error al consultar cursos: {e}")

# Función para filtrar documentos por un rango de valores para un atributo específico
def filtrar_por_rango(coleccion, atributo, valor_min, valor_max):
    try:
        vista = db.view(f'{coleccion}/por_{atributo}', start_key=valor_min, end_key=valor_max)
        for fila in vista:
            documento = fila.value
            print(f"Documento encontrado - ID: {fila.id}, {atributo}: {documento[atributo]}")
    except Exception as e:
        print(f"Error al filtrar documentos por rango: {e}")

# Función para crear un nuevo documento en la base de datos
def crear_documento(coleccion, datos):
    try:
        db.save(datos)
        print(f"Nuevo documento creado en la colección {coleccion}.")
    except Exception as e:
        print(f"Error al crear documento: {e}")

# Función para actualizar un documento existente en la base de datos
def actualizar_documento(id, nuevos_datos):
    try:
        documento = db.get(id)
        if documento:
            for key, value in nuevos_datos.items():
                documento[key] = value
            db.save(documento)
            print("Documento actualizado con éxito.")
        else:
            print("Documento no encontrado.")
    except Exception as e:
        print(f"Error al actualizar documento: {e}")

# Función para eliminar un documento de la base de datos
def eliminar_documento(id):
    try:
        documento = db.get(id)
        if documento:
            db.delete(documento)
            print("Documento eliminado con éxito.")
        else:
            print("Documento no encontrado.")
    except Exception as e:
        print(f"Error al eliminar documento: {e}")

# Crear las vistas en la base de datos
vistas = {
    "usuarios/por_id": {"map": "function(doc) { if (doc.type === 'usuario') emit(doc._id, doc); }"},
    "usuarios/por_nombre": {"map": "function(doc) { if (doc.type === 'usuario') emit(doc.nombre, doc); }"},
    "usuarios/por_carrera": {"map": "function(doc) { if (doc.type === 'usuario') emit(doc.carrera, doc); }"},
    "usuarios/por_semestre": {"map": "function(doc) { if (doc.type === 'usuario') emit(doc.semestre, doc); }"},
    "tutores/por_id": {"map": "function(doc) { if (doc.type === 'tutor') emit(doc._id, doc); }"},
    "tutores/por_nombre": {"map": "function(doc) { if (doc.type === 'tutor') emit(doc.nombre, doc); }"},
    "tutores/por_carrera": {"map": "function(doc) { if (doc.type === 'tutor') emit(doc.carrera, doc); }"},
    "tutores/por_calificacionPromedio": {"map": "function(doc) { if (doc.type === 'tutor') emit(doc.calificacionPromedio, doc); }"},
    "cursos/por_id": {"map": "function(doc) { if (doc.type === 'curso') emit(doc._id, doc); }"},
    "cursos/por_nombre": {"map": "function(doc) { if (doc.type === 'curso') emit(doc.nombre, doc); }"},
    "cursos/por_categoria": {"map": "function(doc) { if (doc.type === 'curso') emit(doc.categoria, doc); }"},
    "cursos/por_modalidad": {"map": "function(doc) { if (doc.type === 'curso') emit(doc.modalidad, doc); }"}
}

# Crear las vistas en la base de datos
for view_name, view in vistas.items():
    try:
        db.save({
            "_id": f"_design/{view_name}",
            "views": {
                view_name.split("/")[1]: view
            }
        })
    except Exception as e:
        print(f"Error al crear vista: {e}")

# Ejemplos de uso
try:
    nuevo_usuario = {
        "type": "usuario",
        "nombre": "Juan Mbaperez",
        "carrera": "Ingeniería",
        "semestre": 5
    }
    crear_documento("usuarios", nuevo_usuario)

    consultar_usuario("nombre", "Juan Mbaperez")

    consultar_tutor("carrera", "Ingeniería Electrica")

    consultar_curso("categoria", "Tecnología")

    filtrar_por_rango("usuarios", "semestre", 3, 6)  # Ejemplo de filtrar usuarios por semestre entre 3 y 6
except Exception as e:
    print(f"Error: {e}")