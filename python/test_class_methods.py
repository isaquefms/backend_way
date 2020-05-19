# Compreendendo na prática a diferença entre métodos da classe e estáticos
from datetime import date

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	# método da classe que cria um objeto Pessoa pela data de nacimento
	@classmethod
	def pela_data_de_nascimento(cls, nome, ano):
		return cls(nome, date.today().year - ano)

	# método estático para checar se a pessoa é adulta ou não
	@staticmethod
	def is_adult(age):
		return age > 18

pessoa1 = Pessoa('Isaque', 23)
pessoa2 = Pessoa.pela_data_de_nascimento('Isaque', 23)

print(Pessoa.is_adult(23))