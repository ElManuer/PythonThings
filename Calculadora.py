# Creo una condicion para que el usuario escoja que realizar
while True:

    def main_menu():

# Menu de opciones
        print("Universidad Experimental Nacional de Guayana")
        print("Bienvenida al menu, ¿que desea realizar?")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sacar porcentaje")
        print("6. Sacar La potencia de una potencia")
        print("7. Sacar una divicion exacta")
        opcion = input("--> ")

#Coloco las entradas segun lo que decida el usuario
        if opcion == "1":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese con que lo sumara :")
            Resultado =  float(n1) + float(n2)
        elif opcion == "2":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese con que lo restara :")
            Resultado =  float(n1) - float(n2)
        elif opcion == "3":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese con que lo multiplicara :")
            Resultado =  float(n1) * float(n2)
        elif opcion == "4":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese con que lo dividira :")
            Resultado =  float(n1) / float(n2)
        elif opcion == "5":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese el porcentaje a sacar :")
            Resultado =  float(n1) * float(n2)
            Resultado = Resultado / 100
        elif opcion == "6":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese su exponente :")
            Resultado =  float(n1) ** float(n2)
        elif opcion == "7":
            n1 = input("Ingrese un numero :")
            n2 = input("Ingrese con que lo dividira :")
            Resultado =  float(n1) // float(n2)

        return Resultado

# El resultado final con la opcion de seguir o terminar el programa
    Calculo = main_menu()
    print("Tu resultado es: ", Calculo)
    print("Que desea realizar?")
    seguir = input("Quiere sacar otro calculo? (s/n): ")
    if seguir != "s":
# Mensaje de mi parte, nada mas que ver. Buenas Noches zZz
        print("Tenga un buena dia, muchas gracias")
        print("Actividad realizada por Manuel Pastrano")
        break

print("Caca Seca")