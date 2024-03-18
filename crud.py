import couchdb
user= "adminBrown"
pwd= "12345"
host = "127.0.0.1"
port = "5984"
# Conectar a CouchDB
couch_server = couchdb.Server(f"http://{user}:{pwd}@{host}:{port}/")
db = 'recommendation_system'

# Función para consultar usuarios por nombre
def consultar_usuario_por_nombre(nombre):
    vista = db.view('usuarios/por_nombre', keys=[nombre])
    for fila in vista:
        usuario = fila.value
        print(f"Usuario: {usuario['nombre']}, Carrera: {usuario['carrera']}, Semestre: {usuario['semestre']}")

# Función para consultar tutores por carrera
def consultar_tutor_por_carrera(carrera):
    vista = db.view('tutores/por_carrera', keys=[carrera])
    for fila in vista:
        tutor = fila.value
        print(f"Tutor: {tutor['nombre']}, Carrera: {tutor['carrera']}, Calificación Promedio: {tutor['calificacionPromedio']}")

# Función para consultar cursos por categoría
def consultar_curso_por_categoria(categoria):
    vista = db.view('cursos/por_categoria', keys=[categoria])
    for fila in vista:
        curso = fila.value
        print(f"Curso: {curso['nombre']}, Categoría: {curso['categoria']}, Modalidad: {curso['modalidad']}, Precio: {curso['precio']}")


consultar_usuario_por_nombre('Juan Mbaperez')
consultar_tutor_por_carrera('Ingeniería Electrica')
consultar_curso_por_categoria('Tecnología')