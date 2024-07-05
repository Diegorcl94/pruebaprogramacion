import os
import json
import globales 
import statistics
import random
from math import prod

productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]

def asignar_montos_aleatorias():
    os.system("cls")
    monto = productos
    for producto in productos:
        producto = random.randint(2000, 10000)
        monto.append({"nombre":producto, "monto":monto})
    with open ("monto.json","w")as file:
        json.dump(producto,file)

        


def cargar_montos():
    with open ("montos.json","r")as file:
        json.load("montos.json")
        
    return productos

def ver_estadisticas():
     

def menu(): True
   
    print("====menu general")
    print("1.asignar montos aleatorios")
    print("2. ver estadisticas")
    print("3.salir")
     
    opcion = globales.seleccionar_opcion(3)

    if opcion == 1:
        print("asignar montos aleatorios")
        asignar_montos_aleatorias
    elif opcion == 2:
        print("estadisticas")
        ver_estadisticas
    elif opcion == 3:
        print("salir")
        break

    else:
        print("opcion no valida intente nuevamente")
