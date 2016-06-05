"""
Design and analysis of algorithms -- continued.

The following problems all take a list of n random integers

ThreeSum
  Find all the triples that add to zero
  Faster ThreeSum: Can you solve it in n^2 lg(n) time? n^2 time?
Closest Pair
  Given an array of N floats, find the closest pair
  Can we solve it in linearithmic time (n lg (n))?
Ro Sham Bo
  Can you create an AI to defeat mankind?
"""

import random

def three_sum():
  xs = [random.randint(-100, 100) for _ in xrange(1000)]
  print xs

  triples = [(xs[a], xs[b], xs[c])
             for a in range(len(xs))
             for b in range(a, len(xs))
             for c in range(b, len(xs))
             if xs[a] + xs[b] + xs[c] == 0]

  print triples

  set_xs = set(xs)
  fast_triples = [(xs[a], xs[b], -(xs[a] + xs[b]))
                  for a in range(len(xs))
                  for b in range(a, len(xs))
                  if -(xs[a] + xs[b]) in set_xs]

  print fast_triples

def closest_pair():
  xs = [random.random() for _ in xrange(1000)]
  xs = sorted(xs)
  print xs
  min_pair = (xs[0], xs[1])
  min_dist = abs(xs[0] - xs[1])
  for a, b in zip(xs[:-1], xs[1:]):
    pair, dist = (a, b), abs(a-b)
    if dist < min_dist:
      min_pair, min_dist = pair, dist
  print min_pair, min_dist
