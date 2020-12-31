# Setting up the environment
1. Create a the virtual environment and install all the requirements or dependencies.
```code
>>> py -m venv venv
>>> source venv/Scripts/activate
>>> pip install -r requirements.txt
```
2. Create a mySQL database with the following credentials. Also, run the following scripts to initialize the database.
```code
DATABASE CREDENTIALS

USER     =  root
PASSWORD =  password
```
```code
*RUN THIS SCRIPT*
-----------------
CREATE DATABASE Sample_DB;

USE Sample_DB;

CREATE TABLE _User(
    ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(30) NOT NULL UNIQUE,
    Password VARCHAR(30) NOT NULL UNIQUE,
);

INSERT INTO _User(Username, Password)
VALUES
    ('admin', 'password);
```

3. Run the `Dash App`.
```code
>>> python main.py
```

4. Login with credentials `admin` and `password`.
