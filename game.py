
# say hello, explain the game
# generate random number, save it to variable
# get guess from user
# compare the guess to the random number
# if low, say 'low'
# if hi, say, 'hi'
# if equal, say 'you win' and exit.
# guess again

print 'hello. This is a guessing game. ' \
      'guess the number between 1 and 100'

import random

sean = random.randint(1, 100)

while True:
    a = raw_input('guess the number: ')
    a = int(a)
    print 'you guessed', a
    if a < sean:
        print 'too low'
    if a > sean:
        print 'too high'
    if a == sean:
        print 'you win!'
        exit()












