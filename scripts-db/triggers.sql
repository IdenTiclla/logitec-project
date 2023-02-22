CREATE TABLE Logs (
    cod_accion INT NOT NULL AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL,
    usuario varchar(50) not null,
    fecha DATETIME NOT NULL,
    PRIMARY key(cod_accion)
)

----triggers tabla productos
----after insert
DROP TRIGGER IF EXISTS TgInsertarProductoLog;
DELIMITER $$
CREATE TRIGGER TgInsertarProductoLog AFTER INSERT ON productos
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Inserto producto",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;



--- after update

DROP TRIGGER IF EXISTS TgUpdateProductoLog;

DELIMITER $$
CREATE TRIGGER TgUpdateProductoLog AFTER UPDATE ON productos
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Se actualizo el producto",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;


--- after delete

DROP TRIGGER IF EXISTS TgDeleteProductoLog;

DELIMITER $$
CREATE TRIGGER TgDeleteProductoLog AFTER DELETE ON productos
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Se elimino un producto",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;