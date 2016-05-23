import random


def to_pairs(a):
  return [tuple(sorted((a[2 * i], a[2 * i + 1]))) for i in range(len(a) / 2)]

def count_error(xs):
  """
  for each row:
    for each pair in row
      for each subsequent row:
        error + 1 if row contains pair
  """
  errors = 0
  row_pairs = [to_pairs(x) for x in xs]
  for i, row in enumerate(row_pairs):
    for row2 in row_pairs[i + 1:]:
      for pair in row:
        if pair in row2:
          errors += 1
  return errors


def tweak(xs):
  ys = [x[:] for x in xs]
  random.shuffle(random.choice(ys))
  return ys


def solve(n):
  xs = [range(n) for _ in range(n - 1)]
  for x in xs:
    random.shuffle(x)
  error = count_error(xs)
  streak = 0
  while error > 0:
    streak += 1
    ys = tweak(xs)
    ys_error = count_error(ys)
    if ys_error < error or streak > 10000:
      print 'error:', ys_error, 'streak:', streak
      xs, error, streak = ys, ys_error, 0

  return xs

def format_answer(xs):
  names = ['Cedric', 'Ellen', 'Aiden', 'Sasha', 'Sebastian',
           'Nate', 'Alexia', 'Keegan', 'Caleb', 'Gaelen']

  ns = [[names[i] for i in x] for x in xs]

  for round, row in enumerate(ns):
    for pair in to_pairs(row):
      print round + 1, pair[0], pair[1]
      print round + 1, pair[1], pair[0]


if __name__ == '__main__':
  format_answer(solve(10))