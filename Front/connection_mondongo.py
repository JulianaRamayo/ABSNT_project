from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_mondongo():
    password = "papoche"
    username = "juan"
    # Construye la cadena de conexión con la contraseña actualizada
    uri = f"mongodb+srv://{username}:{password}@clusterhageo.fiomhxd.mongodb.net/?retryWrites=true&w=majority&appName=ClusterHageo"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client  # Devuelve el cliente conectado
    except Exception as e:
        print(e)
        return None  # Devuelve None en caso de error

# Revisión de función
if __name__ == "__main__":
    db_client = connect_mondongo()
    if db_client:
         
        # Operaciones en la base de datos con db_client
        pass
