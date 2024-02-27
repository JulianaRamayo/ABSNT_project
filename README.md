
# ABSNT <span style="font-size:8pt;">Attendance Biometric System Networking Tool</span>



## Description
ABSNT (Attendance Biometric System Networking Tool) is an innovative solution designed to simplify attendance tracking for educators. Currently under development, this tool aims to revolutionize how attendance is recorded in educational settings, leveraging technology to ease the manual burden on teachers. By integrating biometric systems and a user-friendly networking tool, ABSNT promises to offer a reliable and efficient method for managing class attendance, reducing administrative workload and improving accuracy in record-keeping. With its focus on ease of use and secure data management, ABSNT is poised to become an essential resource for educators seeking to embrace digital solutions in their teaching practices.

## Features

- User registration and authentication.
- Secure password storage with MongoDB.
- Easy-to-use interface for managing user credentials.
- Suported on Linux and Windows.

## Project Structure
- App.py: The main Python script that runs your application.
- connection_mondongo.py: Contains the MongoDB connection logic​​.
- utils.py: Utility functions for user management, such as registering and authenticating users.

## Installation
### Prerequisites
- [Python 3.10 or higher](https://www.python.org/downloads/).
- [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas).
- [Docker](https://docs.docker.com/get-docker/).
- [Docker Compose](https://docs.docker.com/compose/install/).
### Clonning the repository
Recommended to do on a dedicated python environment.

1. Clone the repository from [here](https://github.com/JulianaRamayo/ABSNT_project) or typing this in your terminal:
```bash
$ git clone <repository-url>
```
### Connecting to MongoDB
To connect your application to MongoDB, follow these steps:

1. Open connection_mondongo.py with a text editor.
2. Replace the username, password, and uri variables with your MongoDB Atlas credentials.
```python
username = "your_username"
password = "your_password"
uri = uri = f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority&appName={cluster}"
```
Ensure your MongoDB Atlas cluster is accessible from your IP address.
### Navigating to the project directory
1. Navigate to the project directory: 
```bash
$ cd paht-to-the-directory
```
### Building the Docker Image:
1. Execute the following command in the terminal:
```bash
$ docker-compose up --build
```

## How to use it

With your environment active run 'docker-compose up --build' or 'docker-compose up' to make the file 'App.py' inside the directory 'Front' work.
You will se something like this on your terminal:
```
Creating network "absnt_project_default" with the default driver
Creating absnt_project_flask-app ... done
Attaching to absnt_project_flask-app
flask-app_1  |  * Serving Flask app 'Front/App.py'
flask-app_1  |  * Debug mode: off
flask-app_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
flask-app_1  |  * Running on all addresses (0.0.0.0)
flask-app_1  |  * Running on http://127.0.0.1:8000
flask-app_1  |  * Running on http://172.23.0.2:8000
flask-app_1  | Press CTRL+C to quit
```
Now you can open the link http://127.0.0.1:8000 on your browser and will see the main page of the app.

You can sign up clicking on the button 'Registrarse', or login with 'Iniciar Sesion'. 

Remember that the data that you write on 'Registrarse' will be sent to your Mongo database, so make sure to use it correctly.

## Managing Docker Containers and Images
- Stop the container:
```bash
$ docker-compose down
```

## Usage
Until the most recent update of the project, the signup and login functionalities have been developed. To begin using the application, users must first either sign up or log in, depending on whether they are new to the platform or returning users. For new users, clicking on the 'Registrarse' button on the homepage will navigate to the signup page. Here, the user will be prompted to enter their personal details. Once the signup form is completed and submitted, the account will be created, and users can proceed to log in.

If the user is returning, they must click on the 'Iniciar Sesión' button on the homepage to access the login page. Here, they will need to enter their email and password that were set up during the registration process. Upon successful authentication, they will gain access to the application's features.

After completing the session, the user can log out of the application through the logout option. This ensures that the account remains secure and that unauthorized access is prevented.