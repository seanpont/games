from random import choice
from matplotlib import pyplot


def roll_score(a, b):
  return 0 if a == 1 or b == 1 else a + b

def sum0(a, b):
  return 0 if a == 0 or b == 0 else a + b

ROLL = tuple(roll_score(i, j) for i in range(1, 7) for j in range(1, 7))

def how_many_rolls():
  print 'first roll'
  print ROLL
  print len(ROLL)
  print sum(ROLL) / float(len(ROLL))

  print 'second roll:'
  roll2 = tuple(sum0(r1, r2) for r1 in ROLL for r2 in ROLL)
  print len(roll2)
  print sum(roll2) / float(len(roll2))

  print 'third roll:'
  roll3 = tuple(sum0(r2, r3) for r2 in roll2 for r3 in ROLL)
  print len(roll3)
  print sum(roll3) / float(len(roll3))

  print 'fourth roll:'
  roll4 = tuple(sum0(r3, r4) for r3 in roll3 for r4 in ROLL)
  print len(roll4)
  print sum(roll4) / float(len(roll4))

DIE = (1, 2, 3, 4, 5, 6)


def player(num_rolls):
  """returns number of turns required to reach score of 100"""
  score = 0
  scores = [0]
  while score < 100:
    round_score = 0
    for _ in xrange(num_rolls):
      a, b = choice(DIE), choice(DIE)
      round_score = roll_score(a, b)
      if a == 1 and b == 1:
        score = 0
      if round_score == 0:
        break
    score += round_score
    scores.append(score)
  return scores

for i in range(1, 6):
  print '%s roller:' % i
  print sum(len(player(i)) for _ in xrange(1000)) / 1000.


for _ in xrange(100):
  pyplot.plot(player(1), 'r')
  pyplot.plot(player(2), 'b')
pyplot.axes()
pyplot.show()




