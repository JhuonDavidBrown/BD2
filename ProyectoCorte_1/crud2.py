import couchdb
import os
# Leer las variables de entorno para la conexión a CouchDB
COUCHDB_USER = os.environ.get("COUCHDB_USER", "adminBrown")
COUCHDB_PASSWORD = os.environ.get("COUCHDB_PASSWORD", "12345")
COUCHDB_HOST = os.environ.get("COUCHDB_HOST", "127.0.0.1")
COUCHDB_PORT = os.environ.get("COUCHDB_PORT", "5984")
# Conectar a CouchDB
couch_server = couchdb.Server(f"http://{COUCHDB_USER}:{COUCHDB_PASSWORD}@{COUCHDB_HOST}:{COUCHDB_PORT}/")
db_name = 'recommendation_system'
db = couch_server[db_name]


# Consultar la vista "por_id"
def consultar_cursos():
    vista_por_id = db.view('cursos/por_id')
    for fila in vista_por_id:
        print(f"ID del Curso: {fila.key}")
        print(f"Nombre: {fila.value[0]}")
        print(f"Categoría: {fila.value[1]}")
        print("---")

def eliminar_usuario():
    user_id = input("Ingresa el ID del usuario que deseas eliminar: ")
    user_doc = db.get(user_id)

    if user_doc:
        confirmation = input(f"¿Estás seguro de eliminar el usuario con ID {user_id}? (s/n): ").lower()
        if confirmation == "s":
            db.delete(user_doc)
            print(f"Usuario con ID {user_id} eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"No se encontró un usuario con el ID {user_id}.")


def eliminar_curso():
    curso_id = input("Ingresa el ID del usuario que deseas eliminar: ")
    curso_doc = db.get(curso_id)

    if curso_doc:
        confirmation = input(f"¿Estás seguro de eliminar el usuario con ID {curso_id}? (s/n): ").lower()
        if confirmation == "s":
            db.delete(curso_doc)
            print(f"Usuario con ID {curso_id} eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"No se encontró un usuario con el ID {curso_id}.")

def crear_curso():
    print("Ingresa los datos del nuevo curso:")
    id_curso = input("ID del curso: ")
    nombre_curso = input("Nombre: ")
    categoria_curso = input("Categoría: ")
    modalidad_curso = input("Modalidad (Presencial/En línea): ")
    duracion_curso = int(input("Duración (en horas): "))
    gratuito_curso = input("¿Es gratuito? (s/n): ").lower() == "s"
    precio_curso = 0 if gratuito_curso else float(input("Precio: "))
    certificado_curso = input("¿Otorga certificado? (s/n): ").lower() == "s"

    nuevo_curso = {
        'id': id_curso,
        'tipo': 'curso',
        'nombre': nombre_curso,
        'categoria': categoria_curso,
        'modalidad': modalidad_curso,
        'duracion': duracion_curso,
        'gratuito': gratuito_curso,
        'precio': precio_curso,
        'certificado': certificado_curso
    }
    db.save(nuevo_curso)
    print(f"Nuevo curso insertado")


def menu():
  while True:
    print("\nSelecciona una opción:")
    print("1. Consultar cursos")
    print("2. Eliminar usuario")
    print("3. Eliminar curso")
    print("4. Crear curso")
    print("5. Salir")

    try:
      opcion = int(input("Ingresa el número de opción: "))
    except ValueError:
      print("Opción inválida. Ingresa un número entero.")
      continue

    if opcion == 1:
      consultar_cursos()
    elif opcion == 2:
      eliminar_usuario()
    elif opcion == 3:
      eliminar_curso()
    elif opcion == 4:
      crear_curso()
    elif opcion == 5:
      break
    else:
      print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
  menu()









