def registrar_nuevo_cliente():
  """Registra un nuevo cliente pidiendo los datos con Python."""

  # Pide los datos del cliente.
  nombre = input("Nombre: ")
  apellido = input("Apellido: ")
  email = input("Email: ")
  telefono = input("Teléfono: ")

  # Crea un nuevo cliente.
  cliente = Cliente(nombre, apellido, email, telefono)

  # Guarda el cliente en la base de datos.
  cliente.save()

  # Imprime un mensaje de confirmación.
  print("Cliente registrado correctamente.")
  
# Pedir dimensiones de donde se va a usar el hormigón (longitud, anchura y altura)

# Pedir al usuario que introduzca las dimensiones del hormigón
longitud = float(input("Introduzca la longitud del hormigón en metros,pies o centrimetros: "))
anchura = float(input("Introduzca la anchura del hormigón en metros,pies o centrimetros: "))
altura = float(input("Introduzca la altura del hormigón en metros,pies o centrimetros: "))

# Calcular el volumen del hormigón
volumen = longitud * anchura * altura

# Imprimir el volumen del hormigón
print("El volumen del hormigón es de", volumen, "metros cúbicos,pies o centrimetros.")

# Imprimir los datos del cliente y los metros solicitados
Datosdelcliente   =   {'''nombre
                         apellido
                         calle
                         domicilio'''}
print(Datosdelcliente)

import random
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)