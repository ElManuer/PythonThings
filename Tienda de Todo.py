print()
print("\t.:Tiendas:.")
print("1. Panaderia")
print("1. Pizzeria")
print("3. Cafeteria")
print()
Tienda = int(input("A que tienda desea entrar? --> "))
if Tienda == 1:
    print()
    #Constantes
    Pan = 2.5
    Bs = 18

    #Bienvenida
    print()
    print("\t.:BIENVENIDA A LA PANADERIA VENDO PAN:.")

    #Costo de los panes
    print()
    print("\t.:Nuestros panes estan en un precio de $2.5 Und:.")

    #Usuario Digita la cantidad
    print()
    cantidad = int(input("Ingrese la Cantidad de Panes que desea llevar --> "))
    Pan *= cantidad
    Bs *= Pan

    #Total en Pantalla
    print()
    print(f"Su total a pagar es de : ${Pan}, en Bolivares serian un total de : Bs {Bs}")

    #Despedida
    print()
    print("\t.:Esperemos Vuelva Pronto:.")
    print()
elif Tienda == 2:
    print()
    Pizza = 5
    Bs = 18
    print()
    print("\t.:BIENVENIDA A LA PIZZERIA VENDO PIZZA:.")

    print()
    print("\t.:Nuestras pizzas estan en un precio de $5 Und:.")

    print()
    cantidad = int(input("Ingrese la Cantidad de Pizzas que desea llevar --> "))
    Pizza *= cantidad
    Bs *= Pizza

    print()
    print(f"Su total a pagar es de : ${Pizza}, en Bolivares serian un total de : Bs{Bs}")

    print()
    print("\t.:Esperemos Vuelva Pronto:.")
    print()
elif Tienda == 3:
    print()
    while True:

        Pan = 1.5
        Cachito = 2
        Torta = 2.5
        Jugo = 1
        Cafe = 1.5
        Bs = 18
        print("\t.:Bienvenido/a a la Cafeteria vendo de todo:.")
        
        print("\t.:MENU:.")
        print("1. Pan")
        print("2. Cachito")
        print("3. Torta")
        print("4. Jugo")
        print("5. Cafe")
        print()
        pedido = int(input("Ingrese el numero del articulo deseado --> "))

        if pedido == 1:
            print()
            print("Nuestros Panes tienes un precio de $1.5 la Und")
            print()
            cantidad = int(input("Ingrese la cantidad de panes a llevar --> "))
            Pan *= cantidad
            Bs *= Pan
            print()
            print(f"Su total a pagar es de : ${Pan}, en Bolivares serian un total de : Bs {Bs}")
        elif pedido == 2:
            print()
            print("Nuestros Cachitos tienen un precio de $2 la Und")
            print()
            cantidad = int(input("Ingrese la cantidad de Cachitos a llevar --> "))
            Cachito *= cantidad
            Bs *= Cachito
            print()
            print(f"Su total a pagar es de : ${Cachito}, en Bolivares serian un total de : Bs {Bs}")
        elif pedido == 3:
            print()
            print("Nuestras Tortas tienes un precio de $2.5 la Und")
            print()
            cantidad = int(input("Ingrese la cantidad de Tortas a llevar --> "))
            Torta *= cantidad
            Bs *= Torta
            print()
            print(f"Su total a pagar es de : ${Torta}, en Bolivares serian un total de : Bs {Bs}")
        elif pedido == 4:
            print()
            print("Nuestros Juegos tienes un precio de $1")
            print()
            cantidad = int(input("Ingrese la cantidad de jugos que llevara --> "))
            Jugo*= cantidad
            Bs *= Jugo
            print()
            print(f"Su total a pagar es de : ${Jugo}, en Bolivares serian un total de : Bs {Bs}")
        elif pedido == 5:
            print()
            print("Nuestros Cafes tienes un precio de $1.5 la Und")
            print()
            cantidad = int(input("Ingrese la cantidad de Cafes a llevar --> "))
            Cafe *= cantidad
            Bs *= Cafe
            print()
            print(f"Su total a pagar es de : ${Cafe}, en Bolivares serian un total de : Bs {Bs}")
        else:
            print()
            print("¡Opcion Invalida!, seleccione entre las opcciones (1), (2), (3), (4), (5)")
            print()
        
        print()
        volver = input("Desea volver a comprar otra cosa s/n --> ").lower()
        if volver != "s":
            print("Tenga un buena dia, muchas gracias")
            break
else:
    print()
    print("¡Opcion Invalida!, seleccione entre las opcciones (1), (2) y (3)")
    print()