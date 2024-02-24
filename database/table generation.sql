CREATE SCHEMA IF NOT EXISTS ABSNT;
USE ABSNT;

CREATE TABLE IF NOT EXISTS TEACHER (
	ID_TEACHER INT AUTO_INCREMENT,
    NAME_TEACHER VARCHAR(255) NOT NULL,
    LASTNAME_TEACHER VARCHAR(255) NOT NULL,
    EMAIL_TEACHER VARCHAR(255) NOT NULL,
    PASSWORD_TEACHER VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID_TEACHER)
);

CREATE TABLE IF NOT EXISTS ALUMNI(
	MATRICULA_STUDENT VARCHAR(255) NOT NULL,
    NAME_STUDENT VARCHAR(255) NOT NULL,
    LASTNAME_STUDENT VARCHAR(255) NOT NULL,
    EMAIL_STUDENT VARCHAR(255) NOT NULL,
	QUARTER_STUDENT INT NOT NULL,
    GROUP_STUDENT VARCHAR(255) NOT NULL,
    CAREER_STUDENT VARCHAR(255) NOT NULL,
    PRIMARY KEY (MATRICULA_STUDENT)
);

CREATE TABLE IF NOT EXISTS CLASSES (
	ID_CLASS INT AUTO_INCREMENT,
    NAME_CLASS VARCHAR(255) NOT NULL,
    ID_TEACHER INT NOT NULL,
    YEAR_CLASS INT NOT NULL,
    FOREIGN KEY (ID_TEACHER) REFERENCES TEACHER(ID_TEACHER),
    PRIMARY KEY (ID_CLASS)
);

CREATE TABLE IF NOT EXISTS CLASS_SESSION(
	ID_SESSION INT AUTO_INCREMENT,
    ID_CLASS INT NOT NULL, 
    DATE_SESSION DATETIME NOT NULL,
    DESCRIPTION VARCHAR(255),
    FOREIGN KEY (ID_CLASS) REFERENCES CLASSES(ID_CLASS),
    PRIMARY KEY (ID_SESSION)
);

CREATE TABLE IF NOT EXISTS ATTENDANCE(
	ID_ATTENDANCE INT AUTO_INCREMENT,
    MATRICULA_STUDENT VARCHAR(255) NOT NULL,
    ID_SESSION INT NOT NULL,
    ATTENDED BOOLEAN NOT NULL,
    FOREIGN KEY (MATRICULA_STUDENT) REFERENCES ALUMNI (MATRICULA_STUDENT),
    FOREIGN KEY (ID_SESSION) REFERENCES CLASS_SESSION (ID_SESSION),
    PRIMARY KEY (ID_ATTENDANCE)
); 