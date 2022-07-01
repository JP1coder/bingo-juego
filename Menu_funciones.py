import datetime
import time
from AddData import addnombre, addDNI, addemail, addcantidad, addmetododepago, addnombre_empresa, addfecha, addhora, addcosto_cartilla
def MENU_OPCIONES():
    print("\t¿Qué desea realizar?")
    time.sleep(0.6)
    print("1\tComprar BINGOS")
    time.sleep(0.6)
    print("2\tVisualizar compras")
    time.sleep(0.6)
    print("3\tConfigurar Información")
    time.sleep(0.6)
    print("4\tJugar Bingo")  
    time.sleep(1)
    numero_elegido = int(input("\nOpción : "))
    while numero_elegido not in [1,2,3,4]:
        time.sleep(0.2)
        numero_elegido = int(input("Error, ingrese una opción válida (1, 2, 3 o 4): "))
    return numero_elegido
  
def Datos(parametro_costo):
    diccionarioCliente = {}
    time.sleep(0.5)
    nombre = addnombre()
    time.sleep(0.5)
    DNI = addDNI()
    time.sleep(0.5)
    email = addemail()
    time.sleep(0.5)
    cant_bingos = addcantidad()
    time.sleep(0.5)
    costo_total = cant_bingos * parametro_costo
    print(f"Costo total: S/. {costo_total}")
    time.sleep(0.5)
    metodo_pago_elegido = addmetododepago()
    fechaActual = datetime.datetime.now()
    fecha_con_formato = datetime.datetime.strftime(fechaActual, "%d/%m/%Y %H:%M" ) #relacionado a datos
    diccionarioCliente = {"nombre":nombre,"DNI": DNI,"email": email,
                    "fecha_con_formato": fecha_con_formato, "cant_bingos": cant_bingos,
                    "costo_total": costo_total,"metodo_pago_elegido": metodo_pago_elegido}
    def imprimir_boleta():
        time.sleep(0.5)
        print("COMPRA REALIZADA CORRECTAMENTE")
        print()
        time.sleep(0.4)
        print(
              f"Comprador:\t\t\t{nombre}\t{DNI}\t{email}\n"
              f"Cantidad de Bingos:\t{cant_bingos}\t\t\t\tTotal:\t{costo_total}\tPagado con:\t{metodo_pago_elegido}\n"
              f"Fecha y Hora de compra:\t{fecha_con_formato}")
      #imprimir boleta
    print()
    imprimir_boleta()
    print()
    time.sleep(2)
    print("Los Bingos generados son: ")
    print()
    return diccionarioCliente

def visualizar_compra(diccionario_clientes):
    time.sleep(0.5)
    print('{:<3}|{:<20}|{:<16}|{:<4}|{:<10}|{:9}'.format("N°","Nombre", "Fecha/Hora", "Cant", "Num. Serie", "Total(S/)"))
    suma_total = 0
    for orden, datos in diccionario_clientes.items():
      time.sleep(0.01)
      nombre = diccionario_clientes[orden]['nombre']
      fecha_con_formato = diccionario_clientes[orden]['fecha_con_formato']
      cant_bingos = diccionario_clientes[orden]['cant_bingos']
      serie_impresa = num_series(datos)  #da un string en forma de rango
      costo_total = diccionario_clientes[orden]['costo_total']
      print('{:<3}|{:<20}|{:<16}|{:<4}|{:<10}|{:9}'.format(orden,nombre, fecha_con_formato, cant_bingos, serie_impresa, costo_total))
      suma_total += costo_total
    print()
    print('{:>5}{:>62}'.format("Total",suma_total))
    print()

def num_series(datos_cliente): #datos es el diccionario con datos de cada cliente
    list =[]
    for numero in datos_cliente['cartillas_compradas'].keys(): #keys son las series 001 , 002, 003
        list.append(numero)
    if len(list) == 1:
        return str(list[0])
    else:
        return str(list[0])+" - "+str(list[-1])  
def configurar_informacion():
    nombre_empresa = addnombre_empresa()
    fecha = addfecha()
    hora = addhora()
    costo_cartilla = addcosto_cartilla()
    return nombre_empresa, fecha, hora, costo_cartilla










