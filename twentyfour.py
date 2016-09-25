from random import choice

def add(a, b): return a + b

def sub(a, b): return a - b

def mult(a, b): return a * b

def div(a, b): return a / float(b)

ops = (add, sub, mult, div)

def solve(*xs):
  for i in xrange(len(xs)):
    x, rest = xs[i], xs[:i] + xs[i + 1:]
    ans = _solve(x, *rest)
    if ans:
      return '(((%s %s' % (x, ans)
  return None

def _solve(val, *xs):
  if not xs:
    return ' = 24' if val == 24 else None
  for i in xrange(len(xs)):
    x, rest = xs[i], xs[:i] + xs[i + 1:]
    for op in ops:
      y = _solve(op(val, x), *rest)
      if y:
        return '%s %s) %s' % (op.__name__, x, y)


if __name__ == '__main__':
  count = 0
  for a in range(1, 10):
    for b in range(1, 10):
      for c in range(1, 10):
        for d in range(1, 10):
          if solve(a, b, c, d):
            count += 1
  print 'total combinations: %s of %s' % (count, 9**4)


  # while True:
  #   question = [choice(range(1, 10)) for _ in range(4)]
  #   answer = solve(*question)
  #   if answer:
  #     print '\n', question
  #     raw_input('')
  #     print answer


