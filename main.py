from Menu_funciones import MENU_OPCIONES, Datos, visualizar_compra, configurar_informacion
from Cartillas import creador_cartilla, imprimir_cartilla, serie_cartilla
from JugarBingo import imprimir_cartilla_marcada, generador_numero_aleatorio, pantalla_numeros, marcar_cartilla, cantidad_numeros_marcados, bubble_sort, cantidad_numeros_marcados, guardar_archivo
import time
orden_compra = 1
n_serie = 0
diccionario_clientes = {}    #orden : datos
diccionario_cartillas = {}   #serie : cartilla
# variables que cambia con la opcion 3
costo_cartilla = 5  # variable que cambia con la opcion 3
nombre_empresa = "BINGO PARA RECAUDAR FONDOS PARA LA COMPETICION INTERNACIONAL DEL EQUIPO BLUMETEAM DE UTEC"
fecha = "12 Noviembre 2022"
hora =  "11:00"
numeros_generados = []
while True:
    time.sleep(0.7)
    print(nombre_empresa)
    time.sleep(0.7)
    print(f"{fecha}\t\t{hora}\t\tCosto: S/ {costo_cartilla}\n")
    time.sleep(1.3)
    opcion_menu = MENU_OPCIONES()
    print()
    if opcion_menu == 1:  
        time.sleep(1)
        print("{:^35}".format("COMPRANDO BINGOS"))
        print()
        informacion_cliente = Datos(costo_cartilla)
        #
        cantidad_comprada = informacion_cliente["cant_bingos"]
        diccionario_clientes[orden_compra] = informacion_cliente 
        diccionario_cartillas_usuario = {}
        for i in range(cantidad_comprada):
            time.sleep(0.5)
            n_serie += 1
            serie = serie_cartilla(n_serie) 
            cartilla = creador_cartilla(diccionario_cartillas)
            diccionario_cartillas[serie] = cartilla
            imprimir_cartilla(cartilla, serie)
            diccionario_cartillas_usuario[serie] = cartilla
        diccionario_clientes[orden_compra]["cartillas_compradas"] =  diccionario_cartillas_usuario
        orden_compra += 1
        volver_menu = int(input("0. Volver al menu principal: "))
        while volver_menu != 0:
            volver_menu = int(input("Ingrese una opción válida: "))
        print()
    elif opcion_menu == 2:
        print("{:^70}".format("VISUALIZANDO COMPRAS"))
        visualizar_compra(diccionario_clientes)
        volver_menu = int(input("0. Volver al menu principal\Opción : "))
        while volver_menu != 0:
            volver_menu = int(input("Ingrese una opción válida: "))
        print()
    elif opcion_menu == 3:
        print("CAMBIAR INFORMACIÓN")
        print("")
        nombre_empresa, fecha, hora, costo_cartilla = configurar_informacion()
        print()
    else:
      if len(list(diccionario_cartillas.keys())) >= 5:
        archivo = open("Historial_bingos.txt", "a")
        cartillas_en_juego = [] 
        for k,v in diccionario_cartillas.items():
          cartillas_en_juego.append([k,v])
        print("{:^61}".format("JUEGO DEL BINGO"))
        pantalla_numeros(numeros_generados)
        opcion_jugar_aleatorio= input("Aprete'S' para elegir el siguiente número aleatorio ")
        while opcion_jugar_aleatorio.lower() == "s":
          print()
          print("{:^61}".format("JUEGO DEL BINGO"))
          generador_numero_aleatorio(numeros_generados)
          pantalla_numeros(numeros_generados)
          for serie in diccionario_cartillas.keys():
            marcar_cartilla(numeros_generados, diccionario_cartillas[serie])
          bubble_sort(cartillas_en_juego)
          series_elegidas = [ cartillas_en_juego[i][0] for i in range(-1, -6, -1)]
          for serie in series_elegidas:
            imprimir_cartilla_marcada(serie,diccionario_cartillas)
          serie_ganadora = None
          nombre_usuario = None
          if cantidad_numeros_marcados(cartillas_en_juego[-1][1]) == 25:
            serie_ganadora= cartillas_en_juego[-1][0]
            for v in diccionario_clientes.values():
              if serie_ganadora in list(v["cartillas_compradas"].keys()):
                nombre_usuario = v["nombre"]
            print("¡BINGO!")
            print(nombre_usuario)
            imprimir_cartilla_marcada(serie_ganadora,diccionario_cartillas)
            guardar_archivo(serie_ganadora, diccionario_cartillas, archivo, numeros_generados, nombre_usuario)
            archivo.close()
            break
          opcion_jugar_aleatorio= input("Aprete'S' para elegir el siguiente número aleatorio ")
      else:
        print("No se puede jugar el bingo con menos de 5 cartillas")
        random = None
      volver_menu = int(input("0. Volver al menu principal: "))
      while volver_menu != 0:
        volver_menu = int(input("Ingrese una opción válida: "))
      print()