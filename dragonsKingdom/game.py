#coding: utf-8
import random
import time

from personagem import Personagem
from dragon import Dragon


myPersonagem = Personagem(nome= raw_input("digite o nome do personagem: "), lp = 128
	, atk = random.randint(1, 100), defense = 60)
dragoon = Dragon(lpD = 200, atkD = 178, defenseD = 190)


def displayIntro():
	print("You are in a land full of dragons. In front of you,")
	print('you see two caves. In one cave, the dragon is friendly')
	print('and will share his treasure with you. The other dragon')
	print('is greedy and hungry, and will eat you on sight.')
	print('')

def chooseCave():
	cave = ''
	while cave != 1 and cave != 2:
		cave = input('Which cave will you go into? (1 or 2): ')
		print('')
	return cave

def fight():
	print('you attack the great dragon with your giant sword')
	print('')
	return fight

def run():
	print('you try scape')
	print('')
	return run

def dano():
	danoP = myPersonagem.atk
	PersonagemDef = myPersonagem.defense
	danoD = dragoon.atkD
	dragonDef = dragoon.defenseD

	dano = (dragonDef - danoP)/ 2
	DragonDano = (PersonagemDef - danoD)/2
	
	return dano

def DragonLife(resultDano):
	lifeD = dragoon.lpD
	resultDano = dano()
	lifeD-=resultDano
	return lifeD

def LpPersonagem(resultDano):
	LifeP = myPersonagem.lp
	resultDano = dano()
	lifeP-=resultDano
	return lifeP


def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print('')
	time.sleep(2)

	
	action= raw_input('what do you do? fight or run? ')
	print('')
	if action == 'fight':
		'fight' = fight()	
		print '{} causou {} de dano\nVida do dragão é de {}'.format(myPersonagem.nome.title(),
		 dano(),DragonLife(''))

	if action == 'run':
		'run' = run()

	friendlyCave = random.randint(1, 2)
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')
		
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	playAgain = raw_input('Do you want to play again? (yes or no): ')
else:
	print("GAME OVER!!")
	