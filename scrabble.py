#!/usr/bin/python
# coding=utf-8


def load_words():
  words = []
  with open('/usr/share/dict/words') as word_file:
    for word in word_file:
      word = word.strip()
      if word.islower():
        words.append(word)
  return words


def is_anagram(word, letters):
  if len(word) != len(letters):
    return False
  word = list(word)
  for letter in letters:
    if letter not in word:
      return False
    word.remove(letter)
  return True


def find_anagrams1(words, letters):
  anagrams = []
  for word in words:
    if is_anagram(word, letters):
      anagrams.append(word)
  return anagrams


def generate_anagram_map(words):
  letter_map = {}
  for word in words:
    key = ''.join(sorted(word))
    words = letter_map.get(key, [])
    words.append(word)
    letter_map[key] = words
  return letter_map


def play():
  words = load_words()
  anamap = generate_anagram_map(words)
  print 'here are the first 10 words we loaded:', words[:10]

  print 'some anagrams: ', find_anagrams1(words, 'game')
  print 'same stuff', anamap.get('aegm')

if __name__ == '__main__':
  play()
