import bisect
from random import choice
from string import ascii_lowercase

# Given a 4X4 grid of letters and a dictionary, find all the words from the
# dictionary that can be formed in the grid.

def load_words():
  words = []
  with open('/usr/share/dict/words') as word_file:
    for word in word_file:
      word = word.strip()
      if word.islower():
        words.append(word)
  return words

WORDS = load_words()

def word_frequency_alphabet():
  freqs = {letter: 0 for letter in ascii_lowercase}
  total = 0
  for word in WORDS:
    for letter in word:
      freqs[letter] += 1
      total += 1
  alphabet = ''
  for letter in freqs:
    alphabet += letter * (int((float(freqs[letter]) / total) * 256) + 1)
  return ''.join(sorted(alphabet))

def is_word(word):
  index = bisect.bisect_left(WORDS, word)
  return WORDS[index] == word

def is_prefix(word):
  index = bisect.bisect_left(WORDS, word)
  return WORDS[index].startswith(word)

def new_game(alphabet):
  return [choice(alphabet) for _ in range(16)]

def search(board):
  for i in range(16):
    words = []
    if is_prefix(board[i]):
      _search(board, (i,), board[i], words)
    print ' '.join(words)


def adj(pos):
  up, down, left, right = pos >= 4, pos < 12, pos % 4 > 0, pos % 4 < 3
  if up:
    yield pos - 4
    if left:
      yield pos - 5
    if right:
      yield pos - 3
  if left:
    yield pos - 1
  if right:
    yield pos + 1
  if down:
    yield pos + 4
    if left:
      yield pos + 3
    if right:
      yield pos + 5


def _search(board, path, prefix, words):
  if len(prefix) > 2 and is_word(prefix):
    words.append(prefix)
  pos = path[-1]
  for next_pos in adj(pos):
    if next_pos in path:
      continue
    next_word = prefix + board[next_pos]
    if is_prefix(next_word):
      _search(board, path + (next_pos,), next_word, words)


def wait(seconds):
  import sys
  import select
  select.select([sys.stdin], [], [], seconds)


def play():
  print
  alphabet = word_frequency_alphabet()
  board = new_game(alphabet)
  for row in range(0, 16, 4):
    print ' '.join(board[row: row + 4])
  wait(10)
  print
  print 'searching...'
  search(board)

if __name__ == '__main__':
  play()
