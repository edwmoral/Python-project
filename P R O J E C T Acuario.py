import os

#Función para pintar el menú.
def menu():
	"""
	Función que pinta un menú
        """
	print ("\t")
	print ("Seleccione la opción que desea realizar")
	print ("\t1 - Crear registro de pez")
	print ("\t2 - Buscar condiciones de pez")
	print ("\t3 - Lista de peces")
	print ("\t4 - Lista de peces y condiciones")	
	print ("\t5 - salir")

#Función para obtener las condicones de acuario del pez.
def condiciones(ind):
	print("\t\tpH: "+str(CondicionesAcuario[ind+1]))
	print("\t\tTemperatura: "+CondicionesAcuario[ind+2])
	print("\t\tDureza: "+CondicionesAcuario[ind+3])
	print("\t\tOxigeno: "+CondicionesAcuario[ind+4])
	print("\t\tAlimento: "+CondicionesAcuario[ind+5])

#Función para verificar que se ingrese un dato para que no quede vacio
def vacio(valor, mensaje):
	while True:
		if not valor:
			print("El dato solicitado es requerido.")
			dato = input(mensaje)
			valor = dato
		else:
			break
	return valor

#Diccionario para lista de peces.
peces = {
    "Ramirezi Electro Blue":"Tropical",
    "Tetra Neon":"Tropical",
    "Tetra Cardenal":"Tropical",
    "Cuatro Colas":"Oriental"
}
#Lista de características 
#Nombre del pez, pH, Temperatura, Dureza, oxigeno, alimentación.
CondicionesAcuario = ['Ramirezi Electro Blue',6,'24','baja','alto','seco-vivo',
                      'Tetra Neon',6.5,'24-27','baja','alto','seco-vivo',
                      'Tetra Cardenal',6.5,'24-27','baja','alto','seco-vivo',
                      'Cuatro Colas',7,'24-26','baja','alto','seco']
existe = False

while True:
	# Mostramos el menu.
	menu()
 
	# solicitamos una opción al usuario.
	opcionMenu = input("Ingrese el número de opción de menú: ")
	print ("\t")
	if opcionMenu=="1":
		nombre = input("Indique nombre del pez: ")
		nombre = vacio(nombre, "Indique nombre del pez: ")
		tipo = input("Indique el tipo de pez: ")
		tipo = vacio(tipo, "Indique el tipo de pez: ") 
		# agrego a la lista de peces.
		# llave - valor
		peces[nombre]=tipo
		#--Diccionario
		pH = input("Indique pH: ")
		pH = vacio(pH, "Indique pH: ")
		temp = input("Indique Temperatura: ")
		temp = vacio(temp, "Indique Temperatura: ")
		dureza = input("Indique Dureza del Agua: ")
		dureza = vacio(dureza, "Indique Dureza del Agua: ")
		oxigeno = input("Indique cantidad de oxigeno: ")
		oxigeno = vacio(oxigeno, "Indique cantidad de oxigeno: ")
		alimento = input("Indique tipo de alimentación: ")
		alimento = vacio(alimento, "Indique tipo de alimentación: ")
		#--
		# agrego a la lista de características
		CondicionesAcuario.append(nombre)
		CondicionesAcuario.append(pH)
		CondicionesAcuario.append(temp)
		CondicionesAcuario.append(dureza)
		CondicionesAcuario.append(oxigeno)
		CondicionesAcuario.append(alimento)
		#--
		input("Registro de pez y características de acuario exitoso...\nPulsa una tecla para continuar")
		os.system('cls')
	elif opcionMenu=="2":
			nombre = input("Indique nombre del pez a buscar: ")
			for clave, valor in peces.items():
				if clave==nombre:
					print ("\nNombre del pez: %s Tipo: %s" % (clave, valor))
					indice = CondicionesAcuario.index(clave)
					condiciones(indice)
					existe = True
					break
			if not existe:
				input("No existe registro del pez indicado...\npulsa una tecla para continuar")
				os.system('cls')
			else:
				existe = False
				input("Busqueda exitosa...\npulsa una tecla para continuar")
				os.system('cls')
	elif opcionMenu=="3":
		for clave, valor in peces.items(): 
			print ("\tNombre del pez: %s Tipo: %s" % (clave, valor))
		input("\npulsa una tecla para continuar")
		os.system('cls')
	elif opcionMenu=="4":
		for clave, valor in peces.items(): 
			print ("\tNombre del pez: %s Tipo: %s" % (clave, valor))
			indice = CondicionesAcuario.index(clave)
			condiciones(indice)
		input("\npulsa una tecla para continuar")
		os.system('cls')
	elif opcionMenu=="5":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")
		os.system('cls')
		
