phrase = input('Give a phrase you want to reverse: ')

reverse_phrase = phrase.split(' ')
reverse_phrase.reverse()

print('Your phrase reversed: ')
print(' '.join(reverse_phrase))