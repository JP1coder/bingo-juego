from random import randint
import time
def generador_matriz():
    matriz = []  
    for j in range(5): 
        i = 0            
        columna = []     
        while i < 5:
            numero = randint(15*j +1 , 15*j + 15)   
            if numero not in columna:
                columna.append(numero)
                i += 1
        matriz.append(columna)
    matriz[2][2] = "*"
    return matriz

def verificador_matriz(matriz, diccionario):
    matrices_existentes = list(diccionario.values())
    if matriz in matrices_existentes:
        return True
    else:
        return False
def creador_cartilla(diccionario):
    matriz_generada = generador_matriz()
    while verificador_matriz(matriz_generada, diccionario):
        matriz_generada = generador_matriz()
    return matriz_generada
def serie_cartilla(n_serie):
    return str(n_serie).zfill(3)
def imprimir_cartilla(cartilla,serie):
    print(f"N° serie: {serie} ")
    print("B  I  N  G  O")
    time.sleep(0.2)
    for i in range(5):
        for j in range(5):
            if len(str(cartilla[j][i])) == 2:
                print(cartilla[j][i], end=" ")
                time.sleep(0.02)

            else:
                print(cartilla[j][i], end="  ")
                time.sleep(0.02)

        print()
    print()