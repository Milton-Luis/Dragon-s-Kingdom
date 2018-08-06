#coding: utf-8

class Dragon(object):
	"""docstring for Dragon"""
	def __init__(self, lpD, atkD, defenseD):
		self.lp = lpD
		self.atk = atkD
		self.defense = defenseD

	
	def getDragon(self):
		return self.lp
		return self.atk
		return self.defense


	def dragonAttack(bf, cw):
		bf = 'baforada'
		cw = 'ataque de garras'
		
x = Dragon(lpD = 200,atkD = 160,defenseD = 190)
ataque = {1:Dragon.dragonAttack(bf), 2:Dragon.dragonAttack(cw)
print(ataque())