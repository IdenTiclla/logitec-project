select * from sucursales;

select month(sucursales.fecha_creacion) from sucursales;

select month(ventas.fecha_creacion) from ventas;



select empleados.nombre from empleados, sucursales where empleados.id = sucursales.id;



select empleados.nombre, productos.nombre, ventas.cantidad from empleados, productos, sucursales, ventas where empleados.id = sucursales.id and ventas.id_empleado = empleados.id and ventas.id_producto = productos.id;


select empleados.nombre, productos.nombre, productos.precio, ventas.cantidad, ventas.total
from empleados, productos, sucursales, ventas 
where empleados.id = sucursales.id and ventas.id_empleado = empleados.id and ventas.id_producto = productos.id;


select empleados.nombre, productos.nombre, productos.precio, ventas.cantidad, ventas.total
from empleados, productos, sucursales, ventas 
where empleados.id = sucursales.id and ventas.id_empleado = empleados.id and ventas.id_producto = productos.id and month(ventas.fecha_creacion) = 2;


select empleados.nombre, productos.nombre, productos.precio, ventas.cantidad, ventas.total
from empleados, productos, sucursales, ventas 
where empleados.id = sucursales.id and ventas.id_empleado = empleados.id and ventas.id_producto = productos.id and month(ventas.fecha_creacion) = 2 and ventas.total > 7000;


select empleados.nombre as 'Nombre de empleado', contratos.descripcion as 'Tipo de contrato', productos.nombre as 'nombre del producto', productos.precio as 'Precion del producto', ventas.cantidad as 'Cantidad vendida', ventas.total
from empleados,contratos, productos, sucursales, ventas 
where empleados.contrato_id = contratos.id and empleados.id = sucursales.id and ventas.id_empleado = empleados.id and ventas.id_producto = productos.id and month(ventas.fecha_creacion) = 2 and ventas.total > 7000;