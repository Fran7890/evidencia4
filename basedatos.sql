CREATE DATABASE MAQUINA;
use MAQUINA;
CREATE TABLE Maquina (
    MaquinaID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Ubicacion VARCHAR(100) NOT NULL
);
CREATE TABLE Ficha (
    FichaID INT PRIMARY KEY AUTO_INCREMENT,
    Valor DECIMAL(10, 2) NOT NULL,
    Color VARCHAR(50) NOT NULL
);
CREATE TABLE Usuario (
    UsuarioID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Rol VARCHAR(50) NOT NULL
);
INSERT INTO Ficha (Valor, Color) VALUES (10.00, 'Rojo');
INSERT INTO Ficha (Valor, Color) VALUES (25.00, 'Azul');
use MAQUINA;
INSERT INTO Usuario (Nombre, Rol) VALUES ('Juan Pérez', 'operario');
INSERT INTO Usuario (Nombre, Rol) VALUES ('Ana Gómez', 'Supervisor');
use Maquina;
SELECT Nombre, Ubicacion FROM Maquina;
SELECT Nombre, Ubicacion FROM Maquina;
SELECT * FROM Ficha;
SELECT * FROM Usuario;
SELECT * FROM Ficha
WHERE Color = 'Rojo';