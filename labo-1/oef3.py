from random import randint

print('LINGO-BINGO Welkom bij het kip en eieren spel! ')

counter = 0

random_number = randint(1000, 9999)
random_number = str(random_number)

user_number = input('Geef een viercijferig nummer in: ')

while random_number != user_number:
	kip = 0
	ei = 0
	i = 0
	print('random en user niet gelijk aan elkaar')

	for number in user_number:
		if random_number[i] == user_number[i]:
			kip += 1
		if user_number[i] in random_number and random_number[i] != user_number[i]:
			ei += 1
		i += 1

	print(f'{kip} kippen, {ei} eieren')

	counter += 1

	user_number = input('Geef een viercijferig nummer in: ')

print(f'Je hebt gewonnen! Aantal pogingen: {counter}')
