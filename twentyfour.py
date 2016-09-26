from fractions import Fraction

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return Fraction(a, b)
def rsub(a, b): return b - a
def rdiv(a, b): return Fraction(b, a)
ops = [add, sub, mul, div, rsub, rdiv]

def solver(target, xs):
  """
  Finds an equation that combines rational numbers using the four arithmetic
  operators to equal the target value. The classic example is using 4 ints 1-9
  with a target value of 24
  :param target: an integer
  :param xs: a list of integers or Fractions
  :return: a string describing the operations to be performed, or None if there
  is no solution
  """
  if len(xs) == 1:
    return '= %s' % target if xs[0] == target else None
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


def twentyFour(a, b, c, d):
  """
  (int, int, int, int) -> str
  returns string with 24 solution
  Written by Katherine Paur
  """
  import itertools
  operations = [' add ', ' sub ', ' mult ', ' div ',
                ' reverseSub ', ' reverseDiv ']
  numPermutations = list(itertools.permutations([a, b, c, d], 4))
  operationPermutations = list(itertools.product(operations, repeat=3))
  for numList in numPermutations:
    "check for solutions of form ((x#y)#z)#t"
    for opList in operationPermutations:
      result = operateOn(numList[0], numList[1], opList[0])
      result = operateOn(result, numList[2], opList[1])
      result = operateOn(result, numList[3], opList[2])
      if result == 24:
        return "((" + str(numList[0]) + opList[0] + str(numList[1]) \
               + ")" + opList[1] + str(numList[2]) + ")" + opList[2] \
               + str(numList[3])
    "check for solutions of form (x#y)#(z#t)"
    for opList in operationPermutations:
      result1 = operateOn(numList[0], numList[1], opList[0])
      result2 = operateOn(numList[2], numList[3], opList[1])
      result = operateOn(result1, result2, opList[2])
      if result == 24:
        return "(" + str(numList[0]) + opList[0] + str(numList[1]) \
               + ")" + opList[2] + "(" + str(numList[2]) + opList[1] \
               + str(numList[3]) + ")"
  return None


def operateOn(x, y, operation):
  """
  (int, int, str) -> int
  operation is either add, sub, mult, or div
  Written by Katherine Paur
  """
  if (x == 'NaN') or (y == 'NaN'):
    return 'NaN'
  if operation == ' add ':
    return x + y
  if operation == ' sub ':
    return x - y
  if operation == ' reverseSub ':
    return y - x
  if operation == ' mult ':
    return x * y
  if operation == ' div ':
    if y == 0:
      return 'NaN'
    return x / float(y)
  if operation == ' reverseDiv ':
    if x == 0:
      return 'NaN'
    return y / float(x)


if __name__ == '__main__':
  from itertools import combinations_with_replacement as combos
  from random import choice
  from time import time

  print len(list(combos(range(1, 10), 4)))

  count, t = 0, time()
  for a, b, c, d in combos(range(1, 10), 4):
    if solver(24, [a, b, c, d]):
      count += 1
  print count, time() - t

  count, t = 0, time()
  for a, b, c, d in combos(range(1, 10), 4):
    if twentyFour(a, b, c, d):
      count += 1
  print count, time() - t

  while True:
    question = [choice(range(1, 10)) for _ in range(4)]
    answer = solver(24, question)
    if answer:
      print '\n', question
      raw_input('')
      print answer
      print twentyFour(*question)
