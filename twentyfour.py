from fractions import Fraction
from random import choice

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return Fraction(a, b)
ops = [add, sub, mul, div]

def solver(target, xs):
  if len(xs) == 1:
    return '= 24' if xs[0] == target else None
  for i in xrange(len(xs) - 1):
    for j in xrange(i + 1, len(xs)):
      a, b, rest = xs[i], xs[j], xs[:i] + xs[i + 1:j] + xs[j + 1:]
      for op in ops:
        try:
          ans = solver(target, rest + [op(a, b)])
        except ZeroDivisionError:
          continue
        if ans:
          return '%s(%s, %s) %s' % (op.__name__, a, b, ans)

if __name__ == '__main__':
  while True:
    question = [choice(range(1, 10)) for _ in range(4)]
    answer = solver(24, question)
    if answer:
      print '\n', question
      raw_input('')
      print answer
