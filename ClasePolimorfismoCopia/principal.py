from paqueteEquipo.Modelado import *

#persona = PersonaEquipo("Luis")

#Instancia y creación de objetos
f = Futbolista("Antonio")
e = Entrenador("Jose")
m = MedicoEquipo("Ramon")
p = PresidenteEquipo("Francisco") 
#Creacion de lista
lista = [f, m, p, e]
#Iteración de presenta los elementos de la lista
for l in lista:
	print(l.entrenamiento())
