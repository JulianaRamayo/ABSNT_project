
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
### Installing Requirements
Recommended to do on a dedicated python environment.

1. Clone the repository from [here](https://github.com/JulianaRamayo/ABSNT_project) or typing this in your terminal:
```bash
$ git clone <repository-url>
```
2. Navigate to the project directory: 
```bash
$ cd paht-to-the-directory
```
3. Install the required Python packages:
```bash
$ pip install -r requirements.txt
```
## Connecting to MongoDB
To connect your application to MongoDB, follow these steps:

1. Open connection_mondongo.py with a text editor.
2. Replace the username and password variables with your MongoDB Atlas credentials.
```python
username = "your_username"
password = "your_password"
```
Ensure your MongoDB Atlas cluster is accessible from your IP address.

## How to use it

With your environment active run the file 'App.py' inside the directory 'Front'.
You will se something like this on your terminal:
```
 * Serving Flask app 'App'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```
Now you can open the link http://127.0.0.1:5000 on your browser and will see the main page of the app.

You can sign up clicking on the button 'Registrarse', or login with 'Iniciar Sesion'. 

Remember that the data that you write on 'Registrarse' will be sent to your Mongo database, so make sure to use it correctly.
