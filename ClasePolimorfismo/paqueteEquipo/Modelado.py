class PersonaEquipo(object):

	def __init__(self):
		self.nombre = ""

	def entrenar(self):
		return "Entreno"

	def setNombre(self, m):
		self.nombre = m

	def getNombre(self):
		return self.nombre


class Futbolista(PersonaEquipo):

	def __init__(self):
		super(Futbolista, self).__init__()
		self.posicionCampo = ""

	def entrenar(self):
		return "Hago practica en el entrenamiento"

	def setPosicionCampo(self, m):
		self.posicionCampo = m

	def getPosicionCampo(self, m):
		return self.posicionCampo

class Entrenador(PersonaEquipo):

	def __init__(self):
		super(Entrenador, self).__init__()
		self.codigoEntrenador = ""

	def setCodigoEntrenador(self, m):
		self.codigoEntrenador = m

	def getCodigoEntrenador():
		return self.codigoEntrenador