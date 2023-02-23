------ stored procedures
--- productos

drop procedure insertar_producto;

DELIMITER //
create procedure insertar_producto(in _codigo varchar(10), in _nombre varchar(50), in _descripcion varchar(100), in _stock int(11), in _precio float, in _fecha_creacion DATETIME)
begin
    INSERT INTO productos (codigo, nombre, descripcion, stock, precio, fecha_creacion)
    VALUES (_codigo, _nombre, _descripcion, _stock, _precio, _fecha_creacion);
end//


call insertar_producto('00004', 'Lavandina', 'la mejor lavandina', 100, 5, now());




drop procedure eliminar_producto;

DELIMITER //
create procedure eliminar_producto(in _id int)
begin
    DELETE FROM productos where id = _id;
end//

call eliminar_producto(4);