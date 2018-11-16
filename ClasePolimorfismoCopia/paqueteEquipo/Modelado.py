import abc
#Creacion de la clase Abstracta
class PersonaEquipo(metaclass = abc.ABCMeta):

	__metaclass__ = abc.ABCMeta

	def __init__(self, m):
		self.nombre = m
#Metodo Abstracto
	@abc.abstractmethod
	def entrenamiento(self):
		pass

	def setNombre(self, m):
		self.nombre = m

	def getNombre(self):
		return self.nombre


#Clases Hijas de la clase PersonaEquipo
class Entrenador(PersonaEquipo):

	def __init__(self, n):
		super(Entrenador, self).__init__(n)
		self.codigoEntrenador = ""
#Getters & Setters
	def setCodigoEntrenador(self, m):
		self.codigoEntrenador = m

	def getCodigoEntrenador(self):
		return self.codigoEntrenador
#Sobreescritura del metodo
	def entrenamiento(self):
		cadena = ("Yo %s, entrenador, soy el director del entrenamiento") % Entrenador.getNombre(self)
		return cadena

class Futbolista(PersonaEquipo):

	def __init__(self, n):
		super(Futbolista, self).__init__(n)
		self.posicionCampo = ""

	def setPosicionCampo(self, m):
		self.posicionCampo = m

	def getPosicionCampo(self):
		return self.posicionCampo
#Metodo que presenta la cadena
	def entrenamiento(self):
		cadena = ("Yo %s, futbolista, hago practica en el entrenamiento") % Futbolista.getNombre(self)
		return cadena

class MedicoEquipo(PersonaEquipo):

	def __init__(self, n):
		super(MedicoEquipo, self).__init__(n)
		self.titulo = ""

	def setTitulo(self, m):
		self.titulo = m

	def getTitulo(self):
		return self.titulo

	def entrenamiento(self):
		cadena = ("Yo %s, medico, atiendo a los jugadores en el entrenamiento") % MedicoEquipo.getNombre(self)
		return cadena


class PresidenteEquipo(PersonaEquipo):

	def __init__(self, n):
		super(PresidenteEquipo, self).__init__(n)
		self.numPropiedades = ""

	def setPropiedades(self, m):
		self.numPropiedades = m

	def getPropiedades(self):
		return self.numPropiedades

	def entrenamiento(self):
		cadena = ("Yo %s, presidente, pongo dinero para el entrenamiento") % PresidenteEquipo.getNombre(self)
		return cadena

