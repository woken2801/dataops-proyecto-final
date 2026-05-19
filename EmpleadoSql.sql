/*
** Conexion a Base de datos clase
Tipo		: Postgresql
Host		: mgg.vps.webdock.cloud
Puerto		: 5432
Database	: dmc
Schema		: rrhh

Usuario		: usr_ro_dmc_rrhh_estudiantes
Contraseña	: fZp!jHt0j6%89^B4I*L*29bz4b^

*/

SELECT cod_departamento, des_departamento
FROM rrhh.Departamento;


SELECT empleado_id, tip_documento, num_documento, nom_empleado, ape_empleado, cod_cargo, cod_departamento, mnt_salario, mnt_tope_comision
FROM rrhh.Empleado;


SELECT cod_cargo, des_cargo
FROM rrhh.cargo;