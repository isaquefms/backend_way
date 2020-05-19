class TestMagicMethods:

	# define o inicializador de um determinado objeto
	def __init__(self, obj):
		self.obj = obj

	# define o método que retornará o representante do objeto
	def __repr__(self):
		return 'Object: {}'.format(self.obj)

	# define como o operador + irá agir sobre um objeto
	def __add__(self, other):
		return self.obj + other

	# define a string printável do objeto
	def __str__(self):
		return self.obj

	# Existem diversos métodos adicionais que podem auxiliar nas operações dos objetos.
	#	Para mais detalhes veja a documentação. Referência: https://rszalski.github.io/magicmethods/