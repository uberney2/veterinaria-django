from pymongo import MongoClient

# Conectarse a la base de datos de MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['VeterinariaMongo']
collection = db['Historia_clinica']