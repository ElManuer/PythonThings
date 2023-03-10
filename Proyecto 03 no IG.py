import requests

'''API PARA PEDIR LOS SIMBOLOS'''
url = "https://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "s50VQQ5EDm0PoVBekdYzQAusXQn40lmz"
}

r1 = requests.request("GET", url, headers=headers, data = payload)
j = r1.json()
listado = ['USD','VES','JPY','EUR','BTC']

print('''
      Bienvenido a conversor API
Por favor escoja la moneda que quiere convertir''')
for x in range(len(listado)):
    print(listado[x])

fromm = input("\nIngrese la moneda que desee convertir: ").upper()
cantidad = int(input(f"\nIngrese la cantidad de '{fromm}' a convertir: "))

print()
for x in range(len(listado)):
    print(listado[x])
to = input("\nIngrese la moneda a la que la convertira: ").upper()

'''API PARA HACER LOS CAMBIOS'''
url = f"https://api.apilayer.com/fixer/convert?to={to}&from={fromm}&amount={cantidad}"

payload = {}
headers= {
  "apikey": "s50VQQ5EDm0PoVBekdYzQAusXQn40lmz"
}

r = requests.request("GET", url, headers=headers, data = payload)
j = r.json()


total = round(j.get('result'),2)
print(f"\n\tLa cantidad de '{fromm}' a '{to}' es de {total}")

'''ACTIVIDAD REALIZADA POR MANUEL ☂️'''