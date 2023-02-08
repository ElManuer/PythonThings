'''Cantidad de empleados
Sueldo de cada empleado
Mostrar mayor sueldo
N° de orden'''

print("\n\t.:Empresas Rabipelao:.")

cantidad = int(input("\nIngrese la cantidad de empleados: "))

Dicc = {}

for i in range(cantidad):
	n_orden = int(input("\nIngrese su numero de orden: "))
	sueldo = input("\nIngrese sueldo: ")
	Dicc[n_orden] = sueldo
	
print("El empleado con mayor sueldo es ",max(Dicc.values()))