print("")
print("12 Practicas")
Practica1 = int(input("Ingrese el numero de la practica que desea -> "))
if Practica1 == 1:

    print("")
    a = float(input("Ingresa 'a' :"))
    b = float(input("Ingresa 'b' :"))
    c = float(input("Ingresa 'c' :"))

    print("La ecuancion que realizaras sera")
    print("3 veces 'a' x 2 veces 'b' menos 2 x 'a' x 'c' entre 2 x 'b'")

    Resultado = (a**3 * (b**2 - 2*a*c)) / (2 * b)
    print("")
    print(Resultado)
    print("")

    #Nice operacion logica y aritmetica
    Respuesta = ((3 + 5 * 8) <3 and ((-6/3 * 4) + 2 <2 )) or (a > b)
    print(Respuesta)
    print("")

    #Intercambiar el valor de 2 variables
    d =input("Ingrese el Valor de 'd' --> ")
    e =input("Ingrese el Valor de 'e' --> ")

    d , e = e , d
    print(f"El nuevo valor de 'd' --> {d}")
    print(f"El nuevo valor de 'e' --> {e}")
    print("")

    #Rdio de un circulo, area y lngitud
    import math #Modulo matematico para importar, (pi)
    pi = 3.14
    r = float(input("Ingrese el Radio --> "))

    area = math.pi * r**2
    longitud = 2 * math.pi * r

    print(f"El area de su Circulo es de --> {area:.2f}") #El:.2f es para el numero de decimales
    print(f"La longitud de su Circulo es de --> {longitud:.3f}") #El:.3f es para el numero de decimales
    print("")

    #Ejercicio 5 Presta atencion wey
    print("Bienvenido a paga lo que debes")

    print("")
    Total1 = float(input("Digite el Precio del producto --> "))
    descuento = Total1 * 0.15
    Pagar1 = Total1 - descuento
    print("")
    print(f"Menos el 15% su pago total es de --> ${Pagar1:.2f}")

#Segunda practica Condicionales
elif Practica1 == 2:

    print("")
    edad = int(input("Ingrese su edad --> "))
    if edad>0 and edad<100:                     #Tambien puede colcoarse '0<edad<100'
        print("")
        print("Edad Valida")
        if edad>=18:
            print("")
            print("Usted es Mayor de Edad")
        else:
            print("")
            print("Usted no es mayor de edad")
    else:
        print("Edad Invalida")

#Ingresar numeros y ver cual de los dos es par.
elif Practica1 == 3:

    print("")
    a = int(input("Ingrese el Valor de 'a'--> "))
    b = int(input("Ingrese el Valor de 'b'--> "))

    if a%2 == 0 and b%2 == 0: #El % es el MOD de Python
        print("")
        print("Ambos son pares")
    elif a%2 != 0 and b%2 != 0:
        print("")
        print("Ambos numero son impares")
    elif a%2 == 0 and b%2 != 0:
        print("")
        print(f"El numero {a} es par, el numero {b} no es par")
    elif b%2 == 0 and a%2 != 0:
        print("")
        print(f"El numero {b} es par, el numero {a} no es par")

#Ingresar datos y ver cual es el mayor
elif Practica1 == 4:

    print("")
    a = float(input("Ingrese el valor de 'a'--> "))
    b = float(input("Ingrese el valor de 'b'--> "))
    c = float(input("Ingrese el valor de 'c'--> "))

    if a<b<c:
        print("'C' es el mayor de todos")
    elif b<c<a:
        print("'A' es el mayor de todos")
    elif a<c<b:
        print("'B' es el mayor de todos")
    else:
        print("Todos los numeros son iguales")

#Ingresar una letra y decir si es una vocal
elif Practica1 == 5:

    print("")
    Letra = input("Indique un caracter: ").lower() #Esto es para transformar todo en minusculas .lower()
    #Y el .upper() para volver todo mayuscula
    if Letra == "a" or Letra == "e" or Letra == "i" or Letra == "o" or Letra == "u":
        print("")
        print("Es una Vocal")
    else:
        print("No es una vocal")

#Calculadora basica
elif Practica1 == 6:

    print("")
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))

    opcion = input("Digite la operacion --> ").upper()

    if opcion == "S":
        Resultado = num1 + num2
        print(f"La suma de ambos numeros es de :{Resultado}")
    elif opcion == "R":
        Resultado = num1 - num2
        print(f"La resta de ambos numeros es igual a: {Resultado}")
    elif opcion == "M" or opcion == "P":
        Resultado = num1 * num2
        print(f"La multiplicacion es: {Resultado}")
    elif opcion == "D":
        Resultado = num1 / num2
        print(f"La division es de: {Resultado:.2f}")
    else:
        print("Operacion Invalida")

#Cajero automatico
elif Practica1 == 7:

    cuenta = 1000
    print("")
    print("\t.:Menu:.")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Monstrar dinero en la cuenta")
    print("4. Salir")
    print("")
    opcion = int(input("Ingrese la opcion que desea realizar -> "))
    
    print()

    if opcion == 1:
        print()
        suma = float(input("Digite la cantidad de dinero a ingresar: "))
        cuenta += suma
        print()
        print(f"Se han agregado a su cuenta: ${suma}, su cuenta tiene un total de: ${cuenta}")
    elif opcion == 2:
        print()
        resta = float(input("Digite la cantidad de dinero a retirar de su cuenta: "))
        if resta>cuenta:
            print()
            print("Usted no Posee ese dinero")
        else:
            cuenta -= resta
            print()
            print(f"Se han retirado de su cuenta: ${resta}, le queda un total de: ${cuenta}")
    elif opcion == 3:
        print()
        print(f"El dinero en su cuenta es de: ${cuenta}")
    elif opcion == 4:
        print()
        print("Hasta la proxima")
    else:
        print()
        print("- Error - esa opcion no es validad")

#Bucles\Listas
elif Practica1 == 8:

    print()
    lista = [3,4,6,3,2,5,87,9,5,34,6,6,5] #* 3 #Esto hace que la lista se copie en si N veces
    lista[6] = 20 #Esto es para cambiar el valor del indice por el indicado

    '''lista.append(6)''' #Sirve para agregar un dato al final de la lista.
    '''lista.insert(2,5)''' #Sirve para agregar algo en un punto especifico de la lista, primero el la posicion (2), luego el numero (5).
    '''lista.extend([6,7,8,9])''' #Esto agrega varios datos AL FINAL de la lista, siendo otra lista [].
    '''len(lista)''' #Para leer el numero de caracteres que hay en la lista.

    print(lista.index(5)) #Esto para que me de el caracter en el Indice 5. (Osea el 4)
    print(lista.count(7)) #Esto para contar el numero de veces que un valor esta en un lista

    '''lista.pop(3)''' #Sirve para elimnar, si se coloca () solo eliminara el ultimo, especficar Indice (#).
    '''lista.remove(7)''' #Sirve para eliminar un valor en especifico (Hay que darselo)
    '''lista.clear()''' #Borar completamente la lista
    '''lista.reverse()''' #Voltear la lista
    '''lista.sort()''' #Ordenar de menos a mayor
    '''lista.sort(reverse = True)''' #Ordenar de mayor a menor

    print(lista)
    print()

#Tuplas
elif Practica1 == 9:

    print()
    #Sirven para crear algo que no sera modificado, se pueden realizar busquedas pero no modificaciones de ningun tipo
    GG = (4,5,4,6,67,4,3,5,5667,5,4,3,3,4,5) #Una tupla va con () y una lista con []
    lista = list(GG) #Esto convertiria toda la Tupla en una Lista
    print(lista)
    print()
    lista1 = [4,45,6,7,4,3,2,4,56]
    Tupla = tuple(lista1) #Para convertir una Lista en Tupla.

#Conjuntos
elif Practica1 == 10:

    print()
    add = input("Chingadera --> ")
    conjunto = set() #Especificar que es un conjunto set()
    #Se deben seguir estos dos pasos, si no se interpreta como un Diccionario
    conjunto = {1,2,3,4,5,"Mamalon",45} #En esta si no se pueden colocar otras lista dentro []
    conjunto.add(add) #Agrega datos en el conjunto ed orden aleatorio
    conjunto.discard(23) #Elimina el elemento indicado
    conjunto.clear() #Limpiar
    print(52 not in conjunto) #In (Ver si esta) Not In (Ver si no esta)

elif Practica1 == 11:

    print()
    print("Continuacion conjuntos: ")

    #Colocar el '''set()''' solo si empezaras desde 0 y quieres agregar, si no pues asi como esta abajo
    a = frozenset({1,2,3}) #Al colocar Frozenset() Se vuelve inmodificable
    b = {3,4,5}
    c = {1,2,3,4,5}

    '''c = a & b''' #Esto es para saber en que indice chocan las dos lista (osea el 3)

    '''print(a.issubset(c))''' #Esto sirve para saber si el conjunto de a {1,2,3} se encuentra en c {1,2,3,4,5} YES
    '''print(a.isdisjoint(b))''' #Para saber si NO comparten elemento, en esta caso si el {3}

    print("Lo que vayas a imprimir")

#Diccionarios
elif Practica1 == 12:

    print()

    #En este hay que colocarlo sin el set()
    #Un diccionario se compone de {"Clave":"Valor",}
    diccionario = {"Azul":"Blue","Rojo":"Red","Verde":"Green","Morado":"Purple"}

    #Agregar Cosas
    diccionario["Amarillo"] = "Yellow"

    #Modificar
    diccionario["Azul"] = "Red"

    #Elimnar ["Especificar"]
    del(diccionario["Verde"])

    print(diccionario)

    print()
    diccionario1 = {"manuel":{"Edad":21, "Altura":1.82},"diego":{"Edad":16, "Altura":1.75},"angela":{"Edad":40, "Altura":1.65}}
    print(diccionario1.keys())

    #Este solo para buscar cualquiera y ya xd
    print()
    Buscar = input("Buscar a --> ").lower()
    #Mostrara los datos guardados en esa "Variable"
    print()
    print(diccionario1[Buscar])


























































print()