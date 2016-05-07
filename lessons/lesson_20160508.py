"""
We will design an algorith and build a solver for the
game 'hot or cold'

"""
from random import randint
from math import log, ceil


class HotColdGame:
  def __init__(self, n=100, answer=None):
    assert n > 0, "n must be a positive integer"
    self.min, self.max = 1, n
    self.answer = answer if answer else randint(1, n)
    self.guesses = 0
    self.last_guess = 0

  def guess(self, guess):
    diff = abs(self.answer - guess)
    last_diff = abs(self.answer - self.last_guess)
    self.guesses += 1
    self.last_guess = guess
    return (guess == self.answer,
            '' if self.guesses == 1
            else 'hotter' if diff < last_diff
            else 'colder' if diff > last_diff
            else 'same')


def random_solver(game):
  assert isinstance(game, HotColdGame), 'random_solver takes a HotColdGame'
  solved, temp = game.guess(randint(game.min, game.max))
  while not solved:
    solved, temp = game.guess(randint(game.min, game.max))
  return game.guesses


def step_solver(game):
  assert isinstance(game, HotColdGame), 'solver takes a new HotColdGame'
  guess = (game.min + game.max) / 2
  solved, temp = game.guess(guess)
  if not solved:
    solved, temp = game.guess(guess + 1)
  step = 1 if temp == 'hotter' else -1
  while not solved:
    guess += step
    solved, temp = game.guess(guess)
  return game.guesses


def bisection_solver(game):
  assert isinstance(game, HotColdGame), 'solver takes a new HotColdGame'
  lo, hi, solved = game.min, game.max, False
  g1, g2 = lo, hi
  solved, temp = game.guess(g1)
  if not solved:
    solved, temp = game.guess(g2)
  while not solved and game.guesses < 30:
    mid = (lo + hi) / 2
    if temp == 'same':
      lo = hi = mid
    elif temp == 'colder' and g1 < g2 or temp == 'hotter' and g1 > g2:
      lo, hi = lo, mid
    else:
      lo, hi = mid, hi
    # handle edge case caused by integer division
    if temp != 'same' and g2 == lo:
      lo += 1
    mid = (lo + hi) / 2
    if hi - lo < 2:
      guess = lo
    else:
      guess = 2 * mid - g2
    solved, temp = game.guess(guess)
    g1, g2 = g2, guess
  assert solved, "Unable to solve: %s" % game.answer
  return game.guesses


# bisection_solver(HotColdGame(100, 1))

for a in range(1, 10001):
  bisection_solver(HotColdGame(10000, a))

# bisection_solver(HotColdGame(10000, 5001))
# for n in [10, 100, 1000, 10000, 100000]:
#   a = [bisection_solver(HotColdGame(n, ans)) for ans in range(1, n + 1)]
#   print n, min(a), max(a), sum(a) / float(len(a)), ceil(log(n, 2))




