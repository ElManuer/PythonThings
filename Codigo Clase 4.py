import random
lista = ['Perro','Gato','Ganzo','Leon','Tigre','Toro','Burro','Loro','Liebre','Oveja','Camello']
i = 1
jugador = {}

while True:
    pass
    print('''\n\t.:Menu:.
    1. Comprar Ticket
    2. Soltar ganador''')

    opcion = int(input('\nIngrese una opcion: '))

    if opcion == 1:
        print('''
    0. Perro
    1. gato
    2. Ganzo
    3. Leon
    4. Tigre
    5. Toro
    6. Burro
    7. Loro
    8. Liebre
    9. Oveja
    10. Camello''')
        escojer = int(input("\nIngrese el Numero del animal que desee: "))
        print(f"\n Usted a escogido '{lista[escojer]}'")
        jugador [f'Jugador {i}'] = {lista[escojer]}
        i += 1
        print(jugador)

    elif opcion == 2:
        ganador = random.randrange(1,11)
        print(f"\nEl animal de esta ronda es '{lista[ganador]}' Felicidades a los ganadores")
        animal = lista[ganador]
        
        if escojer == ganador:
            print(jugador())
            print(f"\n\tA ganado la ronda con '{lista[escojer]}'")

        else:
            print("\n\tRonda perdida, Sigue participando para ganar el mejor premio")

    else:
        print("\n\tpcion Invalida escoja una opcion correcta")