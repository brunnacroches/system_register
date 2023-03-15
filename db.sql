CREATE DATABASE system_register;

USE system_register;

CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name_user VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    street VARCHAR(100) NOT NULL,
    profession VARCHAR(25) NOT NULL
);

INSERT INTO users (name_user, birth_date, street, profession)
VALUES ('John Doe', '1990-01-01', '12345678901', 'Developer');
