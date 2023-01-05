#Modelos para la lista de Computadoras
Modelos = {}
Modelos["apple"] = ["modelo 2019 con 8GB de Ram y un Procesador i7 8970k a 3.8GHZ"]
Modelos["samsumg"] = ["modelo 2016 con 4GB de Ram y un Procesador i5 3200M a 2.4GHZ"]
Modelos["dell"] = ["modelo 2005 con 2GB de Ram y un Procesador i3 1024M a 2.0GHZ"]
Modelos["t-plink"] = ["modelo 2017 con 8 GB de Ram y un Procesador AMD Ryzen 5 5600G a 4.5GHZ"]
Modelos["siragon"] = ["modelo 2015 con 4 GB de Ram y un Procesador i5 4400K a 3.8GHZ"]
Modelos["huawei"] = ["modelo 2011 con 6 GB de Ram y un Procesador Intel Core Duo a 2.4GHZ"]
Modelos["tecno"] = ["modelo 2017 con 8 GB de Ram y un Procesador ADM Threadripper 3990X a 4.8GHZ"]
Modelos["alcatel"] = ["modelo 2020 con 2 GB de Ram y un Procesador i3 4500M a 3.2 GHZ"]
Modelos["realme"] = ["modelo 2022 con 8 GB de Ram (Expandible) y un Procesador i7 12000K a 4.9GHZ"]
Modelos["xiaomi"] = ["modelo 2015 con 3 GB de Ram y un Procesador i5 3200K a 2.5GHZ"]
Modelos["sky"] = ["modelo 2015 con 2 GB de Ram y un Procesador intel Core Duo a 2.2GHZ"]
Modelos["blu"] = ["modelo 2013 con 8 de Ram y un Procesador i5 3200K a 2.8GHZ"]
Modelos["toshiba"] = ["modelo 2022 con 16 GB de Ram y un Procesador i7 9900k a 5.2GHZ"]
Modelos["acer"] = ["modelo 2005 con 1 GB de Ram y un Procesador intel Pentium a 1.8GHZ"]
Modelos["motorola"] = ["modelo 2022 con 6 GB de Ram y un Procesador i7 5200M a 3.8GHZ"]

#Bienvenida y Pregunta para entrar al Sistema
print("\t Bienvenida/o a ElectronicArts")
print("")
opcion = input("¿Deseas entrar a la tienda? 'Y/N' --> ").lower()
if opcion == 'y' or opcion == 'si': #Pregunta si desea entrar a la Tienda Virtual
    modelos = input("¿Que modelo de computadora estas buscando?:.")
    if modelos in Modelos:
        print("") #Codigo de Disponibilidad
        print("Su modelo si esta disponible y tiene las siguientes Caracteristicas :")
        print("")
        print(Modelos[modelos])
    else:
        print("")
        print("Lamentamos informar que ese modelo no esta disponible")
        print("")
        print('¿Desea ver la lista completa de todas las marcas disponibles?')
        listado = input('Y/N -->')
        if listado == 'y' or listado == 'si':
            print(Modelos.keys())
#Bucle para preguntar si volver a buscar
while True:
  print("")
  opcion = input("¿Quieres  buscar otro modelo? 'Y/N' --> ").lower()
  if opcion == 'y' or opcion == 'si':
    modelos = input(" ¿Que modelo de computadora estas buscando ?:.")
    if modelos in Modelos:
        print("")
        print("Su modelo si esta disponible y tiene las siguientes Caracteristicas :")
        print("")
        print(Modelos[modelos])
    else:
      print("")
      print("Lamentamos informar que ese modelo no esta disponible")
      print("")
      print('¿Desea ver la lista completa de todas las marcas disponibles?')
      listado = input('Y/N -->')
      if listado == 'y' or listado == 'si':
          print(Modelos.keys())
      
  else:
    print("")
    print("Hasta la proxima y vuelva pronto, aqui donde la Tecnologia es mas que un Arte")
    break

else:
  print("")
  print("Hasta la proxima y vuelva pronto, aqui donde la Tecnologia es mas que un Arte")
print("")
print('Eso es todo, hasta la proxima <3, Actvidad realizada por Manuel Pastrano')
