import random
import os 
from os import system


def main():
	try:
		os.system('cls')
		os.system('mode 55, 10') #change window size
		os.system('title muck settings gen')
		seed = random.randint(0, 999999999999999999) #1000000000000000000 possible muck seeds
		difficulties = ['easy', 'normal', 'gamer']
		difficulty = random.choice(difficulties)
		print(f'seed: {seed}')
		print(f'difficulty: {difficulty}\n')
		another = input("press the enter key to generate different settings")
		if another == 'something':
			main()
		elif another != 'something':
			main()
	except KeyboardInterrupt:
		main()
	

main()
