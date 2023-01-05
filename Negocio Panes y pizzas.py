Pan = 2
Pizza = 5
Dolar = 12

print("Bienvenida/o a la panaderia y ahora pizzeria Manu")
print("Vendemos pizza y pana :D")

Producto = int(input("¿Que producto desea?: 1 para Pan y 2 para Pizza :"))

if Producto == 1:
    Cantidad1 = int(input("Cuantos panes desea llevar? :"))
    precio1 = Cantidad1 * Pan
    precioF1 = precio1 * Dolar
    print("El monto a pagar es :",precioF1,"Bolivares")
if Producto == 2:
    Cantidad2 = int(input("Cuantas pizzas desea llevar? :"))
    precio2 = Cantidad2 * Pizza
    precioF2 = precio2 * Dolar
    print("El monto a pagar es :",precioF2,"Bolivares")
else:
    print("")
    print("Solo vendemos Pizza y Pan")
