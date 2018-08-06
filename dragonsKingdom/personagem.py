#coding: utf-8

class Personagem(object):
	"""docstring for Personagem"""
	def __init__(self, nome, lp, atk, defense):
		self.nome = nome 
		self.lp = lp 
		self.atk = atk 
		self.defense = defense
	
		print("\nO nome do Personagem é {},\nseus pontos de vida são {} "
		"\nseus pontos de ataque são {} \ne os de defesa são {}\n"
		. format(nome.title(), lp, atk, defense))


msg = "Bem vindo a Dragon's Kingdom"
print("{:^80}".format(msg.upper()))

#x = Personagem(nome = '', lp = 128, atk = 124, defense = 60)


