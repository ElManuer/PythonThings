'''Dividir todo en funciones
Sueldo mayor
agregar empleados
sueldo de cada empleado'''


dicc = {}
while True:
    print("\n.:Empresas Rapipelao:.")
    print("\n\t.:MENU:.")
    print("1. Agregar empleados")
    print("2. Mostrar mayor sueldo")
    print("3. Ordenar empleados")

    opcion = int(input("\nIngrese la opcion deseada: "))
    opciones = [1,2,3]

    if opcion not in opciones:
        print("Opcion invalida")
    
    elif opcion == 1:
        cantidad = int(input("\nIngrese la cantidad de empleados a agregar: "))

        for i in range(cantidad):
            empleado = input("\nIngrese el nombre del empleado: ")
            sueldo = float(input(f"Ingrese el sueldo del empleado '{empleado}': "))

            dicc[empleado]=sueldo
            print()

        for x in sorted(dicc):
            print(x,dicc[x],"$")

    elif opcion == 2:
        print("\nEl empleado con mayor sueldo es", max(dicc.keys()),"con",max(dicc.values()),"$")
    
    elif opcion == 3:
        print("De que manera desea ordenar a sus empleados?")
        print("1. Por nombre")
        print("2. Por sueldo")
        opcion = int(input("\nIngrese la opcion deseada: "))
        print()

        if opcion == 1:
            for x in sorted(dicc):
                print(x,dicc[x],"$")
            print()

        elif opcion == 2:
            for x in sorted(dicc, key= lambda x: dicc[x], reverse=True):
                print(x,dicc[x])

'''ACTIVIDAD REALIZADA POR MANUEL ENRIQUE PASTRANO SUAREZ ☂️'''