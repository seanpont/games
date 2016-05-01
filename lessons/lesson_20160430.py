"""
Two quick games

Josephus Problem
N people are in dire straits and agree to the following strategy to reduce
the population: They arrange themselves in a circle (apt positions numbered
from 0 to N-1) and proceed around the circle starting at 0 and eliminating
every Mth person until only one person is left. Legend has it that Josephus
figured out where to sit to avoid being eliminated.

Write a function which takes M and N from the command line and prints out
the order in which people are eliminated. For example:

Number of people: 7
Skip: 1
answer: 1 3 5 0 4 2 6

Bonus problem:
Use the 'Josephus Cipher' to encode and decode messages!

================================================================================

Hot or cold

Your goal is to guess a secret number!
You repeatedly guess a number between 0 and N and the game stops when you
guess the secret number. When you guess incorrectly, you learn if the
guess is hotter (closer) or colder (farther) from than the last guess.

Alternate version: Play the game on a 2D grid instead of a 1d number line.

Bonus: design an algorithm that find the secret square in at most ~2*lg N
guesses. Can you do it in lgN?
















================================================================================

"""

def josephus(n, m):
  x, y, i = range(n), [], m
  while x:
    y.append(x.pop(i))
    i = (i + m) % len(x) if x else 0
  return y

print josephus(7, 1)


import string
characters = (string.ascii_letters +
              string.digits +
              string.punctuation +
              string.whitespace)

def encode(message, key):
  cipher = josephus(len(characters), key)
  return ''.join((characters[cipher[characters.index(m)]] for m in message))

def decode(message, key):
  cipher = josephus(len(characters), key)
  return ''.join((characters[cipher.index(characters.index(m))] for m in message))


key = 17
encoded = encode("Cedric and Alexia are l33t h4ckerz!", key)
print encoded
decoded = decode(encoded, key)
print decoded


def hot_or_cold(n):
  guess1 = guess2 = int(raw_input("guess: "))
  if guess1 == n:
    print 'bingo!'
    return
  while guess2 != n:
    guess1 = guess2
    guess2 = int(raw_input("guess again: "))
    diff1 = abs(n - guess1)
    diff2 = abs(n - guess2)
    if diff2 == 0:
      print 'bingo!'
    elif diff1 < diff2:
      print 'getting colder...'
    elif diff1 > diff2:
      print 'getting warmer...'
    else:
      print 'same degree'


from random import randint
# hot_or_cold(randint(0, 100))






