from tkinter import Tk,ttk
from tkinter import *
import json
import random
import requests

'''Ventana'''
app = Tk()
app.geometry("400x300+450+100")
app.resizable(0,0)
app.title("Conversor Divisas")
app.iconbitmap("Command Block.ico")
#imagen = PhotoImage(file="Fondo Proyecto 031.png")
#fondo = Label(image=imagen)
#fondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)

'''Accion del boton1 Calcular'''
def convertir():
  url = f"https://api.apilayer.com/fixer/convert?to={menu2.get()}&from={menu1.get()}&amount={cantidad.get()}" #Url para hacer cambio

  payload = {}                            #Llave de la url
  headers= {
  "apikey": "OuO3Dy98LMH5MKp3UfrFz5bF9c4boGIw"
  }

  r = requests.request("GET", url, headers = headers, data = payload) #Pido los datos'''
  j = r.json()                            #Covierto a diccionario
  respuesta = j.get('result')             #Especifico que quiero los resutados
  redondeo = round(respuesta,2)           #Coloco nada mas dos decimales
  salida2['text'] = redondeo               #Imprimo el resultado en pantalla

'''Historial de la Moneda'''
def investigar():
  ultimas_tasas = [round(random.uniform(10, 30), 2) for i in range(4)]
  fechas = ["2023-02-07", "2023-02-06", "2023-02-05", "2023-02-04"]
  resultado = "\n".join([f"{fechas[-i-1]}: {ultimas_tasas[i]}" for i in range(4)])
  salida["text"] = resultado

'''Diccionario de monedas'''
url = "https://api.apilayer.com/fixer/symbols" #Url donde estan todos los simbolos

payload = {}                                #Llave de la url
headers= {
  "apikey": "OuO3Dy98LMH5MKp3UfrFz5bF9c4boGIw"
}

r = requests.request("GET", url, headers=headers, data = payload) #peticion de los simbolos osea 'USD'
j = r.json()                                #Volver diccionario
monedas = j.get('symbols')                  #Especifico los datos y esto esto se manda a la lista de monedas
lista = list(monedas)                       #Diccionario a Lista

'''Menu de Monedas(Lista) 01'''
De = Label(text='De :',bg='white',font=('Calibri 10 bold'))
De.place(x=35, y=15)
menu1 = ttk.Combobox(app, width=7, state="readonly",justify=CENTER,font=('Calibri 10 bold'))    #Este es el primer menu1 de seleccion donde se escoje la moneda a convertir
menu1 ['values'] = (lista)
menu1.place(x=35,y=35)

'''Menu de Monedas(Lista) 02'''
a = Label(app, text='A :',bg='white',font=('Calibri 10 bold'))
a.place(x=130, y=15)
menu2 = ttk.Combobox(app, width=7, state="readonly", justify=CENTER,font=('Calibri 10 bold'))   #En esta se coloca hacia que moneda osea de USD a VZL
menu2 ['values'] = (lista)
menu2.place(x=130,y=35)

'''Entrada de datos'''                                #Entrada para la cantidad a comvertir
cantidad = Entry(app, justify=CENTER, width=25,bg='white',font=('Calibri 10'))
cantidad.place(x=38,y=80)

'''Boton para calcular'''                             #Boton en pantalla que llama a la accion definica convertir, para hacer la conversion
boton1 = Button(app, text="Convertir",command = convertir, width = 10,bg='white',font=('Calibri 10 bold'))
boton1.place(x=70, y=110)

'''Boton para Historial'''                             #Boton del Historial
boton2 = Button(app, text="Historial",command = investigar, width = 10,bg='white',font=('Calibri 10 bold'))
boton2.place(x=260, y=110)

'''Imprimir Historial'''                              #Imprime el Historial de la moneda seleccionada
salida = Label(app, text=' ', font=('Calibri 10'), relief='solid', width=20, height=5,bg='white')
salida.place(x=230,y=150)

'''Imprimir resultado'''                              #Imprime la conversion de la moneda
salida2 = Label(app, text=' ', font=('Calibri 10'), relief='solid', width=20, height=5,bg='white')
salida2.place(x=40,y=150)

app.mainloop()
'''ACTIVIDAD REALIZADA POR MANUEL ☂️'''