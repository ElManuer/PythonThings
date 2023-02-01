'''Cree un diccionario de estudiantes con sus notas Exam1'''
'''Pida al usuario cuantos estudiantes y cada dato'''
'''Calcule el promedio de la nota'''
'''Muestre el estudiante con menor nota'''

#Entrada de cantidad de alumnos a agregar
print("\n\tMinisterio de estudios")
bd = {}
cantidad = int(input("\nIngrese la cantidad de estudianes a agregar: "))

#Bucle para agregar notas y estudiantes
for i in range(cantidad):
    estudiante = input("\nIngrese el nombre y apellido del estudiante: ")
    nota = int(input("\nIngrese la nota del estudiante --> "))

    #Agregar estudiantes y notas
    bd[estudiante] = nota

#Bucle para mostrar el diccionario de estudiantes agregados
print()
for i in sorted(bd):
    print(i, bd[i])

#Estudiante con menor nota
print()
print("El estudiante con menor calificacion es:",min(bd),"con",min(bd.values()),"pts")

#Calculo del promedio general
promedio = (sum(bd.values())/cantidad)
print(f"\n\tSu promedio es de {promedio}")
print()

'''ACTIVIDAD REALIZADA POR MANUEL ENRIQUE PASTRANO SUAREZ ☂️'''