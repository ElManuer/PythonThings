print("\n\tFruteria.cum")
frutas = {"Fresa":5,"Melon":20,"Naranja":0.5}
print(frutas)

fruta = input("\n¿Que fruta desea llevar? :")
cantidad = int(input("\n¿Cuanta fruta desea llevar? :"))

print(f"su monto total a pagar es de: ${frutas[fruta] * cantidad} en {fruta}")
