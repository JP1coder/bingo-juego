import time
from random import randint
def marcar_cartilla(numeros_generados, matriz):  
  for i in range(5):
    for j in range(5):
      if matriz[i][j] in numeros_generados:
        matriz[i][j] = str(matriz[i][j]) + "*"

def imprimir_cartilla_marcada(serie, diccionario_cartillas): #ryutaro
  print(f"N° serie: {serie} ")
  print("{:<3} {:<3} {:<3} {:<3} {:<3}".format("B", "I", "N", "G", "O"))     
  matriz = diccionario_cartillas[serie]
  for j in range(5):
    d1 = matriz[0][j]
    d2 = matriz[1][j]
    d3 = matriz[2][j]
    d4 = matriz[3][j]
    d5 = matriz[4][j]
    print("{:<3} {:<3} {:<3} {:<3} {:<3}".format(d1, d2, d3, d4, d5))
  print("\n")
def generador_numero_aleatorio(list):   #gabriel
  i=randint(1,75)
  if i not in list:
    list.append(i)
    print("Numero:"," ".join(str(list[-1])))
  else:
    while i in list:
      i=randint(1,75)
    list.append(i)
    print("Numero:"," ".join(str(list[-1])))
def cantidad_numeros_marcados(matriz): #adrian
  contador = 0
  for i in range(5):
    for j in range(5):
      if "*" in str(matriz[i][j]):
        contador +=1
  return contador 
def pantalla_numeros(numeros_generados): #sharon
  rayas = []
  for x in range(75):
    rayas.append("__")
  num_ordenados = sorted(numeros_generados)
  for i in range(len(num_ordenados)):
    tmp = num_ordenados[i]
    if len(str(num_ordenados[i])) ==1:
      tmp = num_ordenados[i]
      num_ordenados[i] = str(num_ordenados[i]) + " "
    rayas[tmp-1] = num_ordenados[i]
  print("B", "  ".join(str(i) for i in rayas[0:15]))
  print("I", "  ".join(str(i) for i in rayas[15:30]))
  print("N", "  ".join(str(i) for i in rayas[30:45]))
  print("G", "  ".join(str(i) for i in rayas[45:60]))
  print("O", "  ".join(str(i) for i in rayas[60:75]))
def bubble_sort(lista):
  for tope in range(len(lista)-1, 0, -1):
   for i in range(tope):
     if cantidad_numeros_marcados(lista[i][1]) > cantidad_numeros_marcados(lista[i+1][1]):
       temp = lista[i]
       lista[i] = lista[i+1]
       lista[i+1] = temp
def guardar_archivo(serie, diccionario_cartillas,archivo, numeros_generados, nombre_usuario):
  for i in range(len(numeros_generados)):
    archivo.write(str(numeros_generados[i]) + "-"*(len(numeros_generados) != i+1))
  archivo.write(f"\nusuario: {nombre_usuario} serie: {serie}\n")
  archivo.write("{:<3} {:<3} {:<3} {:<3} {:<3}".format("B", "I", "N", "G", "O")) 
  matriz = diccionario_cartillas[serie]
  archivo.write("\n")
  for j in range(5):
    d1 = matriz[0][j]
    d2 = matriz[1][j]
    d3 = matriz[2][j]
    d4 = matriz[3][j]
    d5 = matriz[4][j]
    archivo.write("{:<3} {:<3} {:<3} {:<3} {:<3}".format(d1, d2, d3, d4, d5))
    archivo.write("\n")
  
  
    
    
    
    
    

