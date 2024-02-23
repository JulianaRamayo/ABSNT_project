from connection_mondongo import connect_mondongo






def insertar_usuario(nombre,email, contraseña):
    
    # Conectar a MongoDB
    client = connect_mondongo()
    if not client:
        print("No se pudo conectar con mondongo")

    # Selecciona la base de datos y la colección
    db = client["Authentication"]  # nombre base de datos
    collection = db["Sign_in"]  # nombre colección
    contraseña = contraseña.strip()
    # Encriptar la contraseña antes de insertarla en la base de datos

    
    # Crea el documento del usuario con la contraseña encriptada
    usuario = {
        "nombre": nombre,
        "email":email,
        "contraseña": contraseña  # Convierte a lista para almacenar en MongoDB
    }

    # Inserta el usuario en la colección
    resultado = collection.insert_one(usuario)

    # Devuelve el ID del documento insertado
    return resultado.inserted_id

def obtener_usuarios(email,password):
    # Conectar a MongoDB
    client = connect_mondongo()
    if not client:
        print("No se pudo conectar con mondongo")
        
    # Selecciona la base de datos y la colección
    db = client["Authentication"]
    collection = db["Sign_in"]

    # Realiza una consulta para obtener todos los documentos
    
    usuario = collection.find_one({"email": email})
    if usuario:
        # Aquí deberías tener lógica para comparar la contraseña ingresada con la almacenada.
        # Suponiendo que la contraseña ya está encriptada y almacenada,
        # necesitarías desencriptar o usar la misma técnica de encriptación para comparar.
        # Por simplificación, aquí se compara directamente.
        
        if password.strip() == usuario["contraseña"]:
            return True
        else:
            # Retornar una página o mensaje de error de contraseña incorrecta
            return False
    else:
        # Retornar una página o mensaje de error de usuario no encontrado
        return False
    return False


