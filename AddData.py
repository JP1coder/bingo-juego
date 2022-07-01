import time
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
#dat
def addnombre():
  time.sleep(0.5)
  name = input("Ingrese su nombre (Nombre y apellido): ")
  while True:
    contador_numeros = 0
    contador_espacios = 0
    for i in name:
      if i in ["1","2","3","4","5","6","7","8","9","0"]:
        contador_numeros += 1
      if i == " ":
        contador_espacios += 1
    if contador_numeros == 0 and contador_espacios == 1:
      break
    time.sleep(0.3)
    name = input("Ingrese correctamente su nombre 'Sin valores numéricos y solo 2 palabras': ")
  return name
def addDNI():
  time.sleep(0.5)
  DNI = int(input("DNI: "))
  while len(str(DNI)) != 8:
    time.sleep(0.3)
    DNI = int(input("Ingrese correctamente su DNI '8 dígitos': "))
  return DNI
def addemail():
  time.sleep(0.5)
  email = input("email: ")
  while True:
    contador_arroba = 0
    contador_punto = 0
    for i in email:
      if i == "@":
        contador_arroba += 1 
      if i == ".":
        contador_punto +=1
    if contador_arroba == 1 and contador_punto == 1:
      break
    elif contador_punto == 1 and contador_arroba != 1:
      time.sleep(0.3)
      email = input("email no válido, debe contener un'@': ")
    elif contador_arroba == 1 and contador_punto != 1:
      time.sleep(0.3)
      email = input("email no válido, debe contener un dominio: ")
    else:
      time.sleep(0.3)
      email = input("email no válido, debe contener '@' y un dominio: ")
  return email
def addcantidad():
  time.sleep(0.5)
  cant_bingos = int(input("Cantidad cartillas: "))
  while cant_bingos <= 0:
    time.sleep(0.3)
    cant_bingos = int(input("Ingrese una cantidad real: "))
  return cant_bingos

def addmetododepago():
  time.sleep(0.5)
  print("Metodo de Pago:")
  time.sleep(0.4)
  print("1 .   VISA")
  time.sleep(0.4)
  print("2 .   Transferencia BCP")
  time.sleep(0.4)
  print("3 .   Yape")
  time.sleep(0.4)
  opcionPago = int(input("Opcion de pago: "))
  while opcionPago not in [1, 2, 3]:
    time.sleep(0.3)
    opcionPago = int(input("ingrese una opcion válida: "))
  metodosDePago = {1:"VISA", 2:"Transferencia BCP", 3:"Yape"}
  return metodosDePago[opcionPago]
def addnombre_empresa():
  time.sleep(0.5)
  print("Inicie el nombre con 'BINGO'")
  time.sleep(0.4)
  print("por ejemplo: BINGO Jesus Obrero")
  time.sleep(0.4)
  nombre_empresa = input("Nombre elegido: ")
  while nombre_empresa[:5].lower() != "bingo":
    print(nombre_empresa[:5].lower())
    time.sleep(0.3)
    nombre_empresa = input("Escriba la informacion correctamente: ")
  return nombre_empresa

def addfecha():
  while True:
    time.sleep(0.5)
    print("Ingrese una fecha:\nEjm: 16 diciembre 2004")
    time.sleep(0.4)
    fecha = input("(dia mes año): ")
    list = fecha.split()
    contador_no_numeros = 0
    for digito in list[0]:
      if digito not in "1234567890":
        contador_no_numeros += 1
    for digito in list[2]:
      if digito not in "1234567890":
        contador_no_numeros += 1
    if list[1].lower() in meses and len(list[0]) == 2 and len(list[2]) == 4 and contador_no_numeros == 0:
      break
    else:
      time.sleep(0.3)
      print("Ingrese correctamente la fecha")
  return fecha

def addhora():
  time.sleep(0.5)
  hora = input("Hora formato 24h (HH:MM): ")
  def validador_hora():
    hora_in = int(hora[0:2])
    minuto_in = int(hora[3:])
    condicion1 = hora_in >= 0 and hora_in <24
    condicion2 = minuto_in >= 0 and minuto_in <60
    if condicion1 and condicion2:
      return True
    else: 
      return False  
  while not(validador_hora()):
    time.sleep(0.3)
    hora = input("Escriba una hora correcta (HH:MM) : ")
  return hora
def addcosto_cartilla():
  time.sleep(0.5)
  costo_cartilla = int(input("Costo S/: "))
  while costo_cartilla <= 0:
    time.sleep(0.3)
    print("Ingrese un costo válido")
    costo_cartilla = int(input("Costo S/: "))
  return costo_cartilla