'''1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.''' 
from os import system 
system("cls")

def calcular_area_circulo (area=3):
    resultado_circulo = 3.14 * (area ** 2)
    print (f"{resultado_circulo}")
    return  
def calcular_area_cuadrado (area):
    resultado_cuadrado = area * area
    print (f"{resultado_cuadrado}")
    return 
def calcular_area_triangulo (base, altura):
    resultado_triangulo = (base * altura) / 2
    print (f"{resultado_triangulo}")
    return

calcular_area_circulo()
calcular_area_circulo(5)
calcular_area_cuadrado(4)
calcular_area_triangulo(5,2)

