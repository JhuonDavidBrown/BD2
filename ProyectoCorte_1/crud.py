import couchdb
COUCHDB_USER = "adminBrown"
COUCHDB_PASSWORD = "12345"
COUCHDB_HOST = "127.0.0.1"
COUCHDB_PORT =  "5984"
couch_server = couchdb.Server(f"http://{COUCHDB_USER}:{COUCHDB_PASSWORD}@{COUCHDB_HOST}:{COUCHDB_PORT}/")
db_name = 'recommendation_system'
db = couch_server[db_name]

def consultar_cursos():
    vista_por_id = db.view('cursos/por_id')
    for fila in vista_por_id:
        print(f"ID del Curso: {fila.key}")
        print(f"Nombre: {fila.value[0]}")
        print(f"Categoría: {fila.value[1]}")
        print("---")
def consultar_tutores():
    vista_por_nombre = db.view('tutores/por_nombre')
    for fila in vista_por_nombre:
        print(f"Nombre: {fila.key}")
        print(f"ID del Tutor: {fila.value[0]}")
        print(f"Carrera: {fila.value[1]}")
        print(f"Semestre: {fila.value[2]}")
        print("---")
def consultar_usuarios():
    vista_por_id = db.view('usuario/por_id')
    for fila in vista_por_id:
        print(f"ID del Usuario: {fila.key}")
        print(f"Nombre: {fila.value[0]}")
        print(f"Carrera: {fila.value[1]}")
        print(f"Semestre: {fila.value[2]}")
        print(f"Cursos: {fila.value[3]}")
        print(f"Calificaciones de cursos: {fila.value[4]}")
        print("---")
def eliminar_curso():
    curso_id = input("Ingresa el ID del curso que deseas eliminar: ")
    vista_por_id = db.view('cursos/por_id', key=curso_id)
    filas = list(vista_por_id)
    
    if len(filas) > 0:
        doc_id = filas[0].id  
        curso_doc = db.get(doc_id)  
        if curso_doc:
            confirmation = input(f"¿Estás seguro de eliminar el curso con ID {curso_id}? (s/n): ").lower()
            if confirmation == "s":
                db.delete(curso_doc)
                print(f"Curso con ID {curso_id} eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print(f"No se encontró un curso con el ID {curso_id}.")
    else:
        print(f"No se encontró un curso con el ID {curso_id}.")

def eliminar_usuario():
    usuario_id = input("Ingresa el ID del usuario que deseas eliminar: ")
    usuario_por_id = db.view('usuario/por_id', key=usuario_id)
    filas = list(vista_por_id)
    
    if len(filas) > 0:
        doc_id = filas[0].id  
        usuario_doc = db.get(doc_id)  
        if usuario_doc:
            confirmation = input(f"¿Estás seguro de eliminar el usuario con ID {usuario_id}? (s/n): ")
            if confirmation == "s":
                db.delete(usuario_doc)
                print(f"Usuario con ID {usuario_id} eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print(f"No se encontró un usuario con el ID {usuario_id}.")
    else:
        print(f"No se encontró un usuario con el ID {usuario_id}.")

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

def modificar_curso():
    curso_id = input("Ingresa el ID del curso que deseas modificar: ")
    vista_por_id = db.view('cursos/por_id', key=curso_id)
    filas = list(vista_por_id)

    if len(filas) > 0:
        doc_id = filas[0].id  
        curso_doc = db.get(doc_id)  
        if curso_doc:
            print(f"Valores actuales del curso con ID {curso_id}:")
            print(f"Nombre: {curso_doc['nombre']}")
            print(f"Categoría: {curso_doc['categoria']}")
            print(f"Modalidad: {curso_doc['modalidad']}")
            print(f"Duración: {curso_doc['duracion']}")
            print(f"Gratuito: {'Sí' if curso_doc['gratuito'] else 'No'}")
            print(f"Precio: {curso_doc['precio']}")
            print(f"Otorga certificado: {'Sí' if curso_doc['certificado'] else 'No'}")

            nuevo_nombre = input(f"Ingresa el nuevo nombre (actual: {curso_doc['nombre']}): ") or curso_doc['nombre']
            nueva_categoria = input(f"Ingresa la nueva categoría (actual: {curso_doc['categoria']}): ") or curso_doc['categoria']
            nueva_modalidad = input(f"Ingresa la nueva modalidad (actual: {curso_doc['modalidad']}): ") or curso_doc['modalidad']
            nueva_duracion = input(f"Ingresa la nueva duración (actual: {curso_doc['duracion']}): ") or curso_doc['duracion']
            nueva_gratuito = input(f"¿Es gratuito? (s/n) (actual: {'Sí' if curso_doc['gratuito'] else 'No'}): ").lower() or str(curso_doc['gratuito'])
            nuevo_precio = input(f"Ingresa el nuevo precio (actual: {curso_doc['precio']}): ") or curso_doc['precio']
            nuevo_certificado = input(f"¿Otorga certificado? (s/n) (actual: {'Sí' if curso_doc['certificado'] else 'No'}): ").lower() or str(curso_doc['certificado'])

            curso_doc['nombre'] = nuevo_nombre
            curso_doc['categoria'] = nueva_categoria
            curso_doc['modalidad'] = nueva_modalidad
            curso_doc['duracion'] = int(nueva_duracion) if nueva_duracion else curso_doc['duracion']
            curso_doc['gratuito'] = nueva_gratuito == 's'
            curso_doc['precio'] = float(nuevo_precio) if nuevo_precio else curso_doc['precio']
            curso_doc['certificado'] = nuevo_certificado == 's'

            db.save(curso_doc)
            print(f"Curso con ID {curso_id} actualizado correctamente.")
        else:
            print(f"No se encontró un curso con el ID {curso_id}.")
    else:
        print(f"No se encontró un curso con el ID {curso_id}.")

def menu():
    while True:
        print("\nSelecciona una opción:")
        print("1. Consultar curso")
        print("2. Consultar tutor")
        print("3. Consultar usuario")
        print("4. Eliminar usuario")
        print("5. Eliminar curso")
        print("6. Crear curso")
        print("7. Modificar curso")
        print("8. Salir")

        try:
            opcion = int(input("Ingresa el número de opción: "))
        except ValueError:
            print("Opción inválida. Ingresa un número entero.")
            continue

        switch_case = {
            1: consultar_cursos,
            2: consultar_tutores,
            3: consultar_usuarios,
            4: eliminar_usuario,
            5: eliminar_curso,
            6: crear_curso,
            7: modificar_curso,
            8: lambda: None  
        }

        funcion = switch_case.get(opcion, lambda: print("Opción inválida. Intenta de nuevo."))
        funcion()

        if opcion == 8:
            break

if __name__ == "__main__":
    menu()








