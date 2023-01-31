print()
monedas = {"Euro":"€","Dollar":"$","Yen":"¥"}
print(monedas.keys())

print()
buscar = input("Ingresa la moneda a buscar :").title
print(monedas.get(buscar(),"Moneda Inexistente"))

print()
for i in range(3):
    agregar = input("\nIngrese el nombre de la moneda a registrar :")
    simbolo = input("\nIngrese el simbolo de su moneda registrada :")
    monedas[agregar] = simbolo
    print(monedas)

print()
eliminar = input("Ingrese la moneda a eliminar :")
del monedas[eliminar]

print()
print(f"Usted elimino '{eliminar}' de la lista de monedas")
print(f"\nEstan son sus monedas {monedas}")

print()
