from paqueteEquipo.Modelado import *

persona = PersonaEquipo()
persona.setNombre("Ana")
print(persona.entrenar())

f = Futbolista()
f.setNombre("Mario")
print(f.entrenar())

e = Entrenador()
print(e.entrenar())

lista = [persona, f, e]

for l in lista:
	print(l.entrenar())
