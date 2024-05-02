import pymongo


client = pymongo.MongoClient("mongodb+srv://JounDavBrown:1234@brownbd-2.j8tbged.mongodb.net/")

db = client["RecommendationSystem"]



# Selecciona las colecciones
coursesCollection = db["Courses"]
usersCollection = db["Users"]
tutorsCollection = db["Tutors"]

# Crea un documento para insertar en la colección
newCourse = {
    "name": "English",
    "category": "Basic Professional",
    "price": 300000,
    "totalHours":80,
    "certification":False
}

#----------------- CREACIÓN DE DOCUMENTOS ------------------
#--- InsertOne: 
# Inserta un documento en la colección
insert_result = coursesCollection.insert_one(newCourse)
print("ID del documento insertado:", insert_result.inserted_id)

