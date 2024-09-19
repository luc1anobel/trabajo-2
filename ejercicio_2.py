'''2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.'''
from os import system 
system("cls")

def calcular_perimetro_circulo ():
    diametro = float(input("ingrese el diametro del circulo: "))
    resultado_circulo = 3.14 * diametro
    print (f"{resultado_circulo}")
    return  
def calcular_perimetro_cuadrado (lado):
    resultado_cuadrado = lado * 4 
    print (f"{resultado_cuadrado}")
    return 
def calcular_perimetro_triangulo ():
    contador = 0
    resultado_triangulo = 0
    while contador < 3:
        contador+=1
        base = float(input("ingrese el lado del triangulo: "))
        resultado_triangulo += base 
    print(f"{resultado_triangulo}")
    return 

calcular_perimetro_circulo ()
calcular_perimetro_triangulo()
calcular_perimetro_cuadrado (5)