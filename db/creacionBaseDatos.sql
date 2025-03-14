--CREATE DATABASE  gestorBD;
-- Crear la base de datos
CREATE TABLE contrasenias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    fecha_creacion DATE NOT NULL,
    sitio TEXT NOT NULL
);

