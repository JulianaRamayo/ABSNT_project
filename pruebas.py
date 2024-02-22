from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_last_document():
    password = "papoche"
    username = "juan"
    # Build the connection string with the updated password
    uri = f"mongodb+srv://{username}:{password}@clusterhageo.fiomhxd.mongodb.net/?retryWrites=true&w=majority&appName=ClusterHageo"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Attempt to ping the database to confirm connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return None  # Return None in case of error

    # Specify your database and collection name here
    db = client['Authentication']
    collection = db['Sign_in']

    # Query to find the last document based on the _id
    try:
        last_document = collection.find().sort('_id', -1).limit(1).next()
        return last_document
    except Exception as e:
        print("Error fetching last document:", e)
        return None

# Example usage
last_document = get_last_document()
if last_document:
    print("Last document in collection:", last_document)
else:
    print("Could not retrieve the last document.")
