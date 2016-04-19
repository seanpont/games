"""
Compression algorithms
lossy vs loss-less
Consider: all 3-bit messages
model and coder
  model: captures probability of distribution of messages
  coder: uses model to generate messages where high-probability words are
  shortened and low-probability words enlarged.
Information theory
  Invented by Claude Shannon - MIT!
  Glues the model and coder together
Encoding data
  fixed-length codes
    ascii characters
    genomic sequences
    (sort of) Chinese
  variable length codes
    morse code
    utf-8
    (sort of) English

Problem 1: Compress and decompress a message using morse code

Problem 2: Design and write a codec to compress genomic data

To download genomic some data:
$ wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chrM.fa.gz'
$ gunzip chrM.fa.gz
"""

morse_code_dict = {"A": ".-",
                   "B": "-...",
                   "C": "-.-.",
                   "D": "-..",
                   "E": ".",
                   "F": "..-.",
                   "G": "--.",
                   "H": "....",
                   "I": "..",
                   "J": ".---",
                   "K": "-.-",
                   "L": ".-..",
                   "M": "--",
                   "N": "-.",
                   "O": "---",
                   "P": ".--.",
                   "Q": "--.-",
                   "R": ".-.",
                   "S": "...",
                   "T": "-",
                   "U": "..-",
                   "V": "...-",
                   "W": ".--",
                   "X": "-..-",
                   "Y": "-.--",
                   "Z": "--..",
                   "0": "-----",
                   "1": ".----",
                   "2": "..---",
                   "3": "...--",
                   "4": "....-",
                   "5": ".....",
                   "6": "-....",
                   "7": "--...",
                   "8": "---..",
                   "9": "----."}


reverse_morse_code_dict = {value: key for key, value in
                           morse_code_dict.iteritems()}


def to_morse_code(message):
  return '  '.join((
      ' '.join((morse_code_dict.get(letter.upper(), '') for letter in word))
      for word in message.split()))


def from_morse_code(morse_code):
  return ' '.join((
      ''.join((reverse_morse_code_dict.get(letter, '')
               for letter in word.split(' ')))
      for word in morse_code.split('  ')))


def test_morse_code(message):
  morse_code = to_morse_code(message)
  print morse_code
  message = from_morse_code(morse_code)
  print message


def read_file(fname):
  data = ''
  for line in open(fname):
    data += line.strip().upper()
  return data


def codon_frequencies(data):
  freq_map = {}
  for i in xrange(0, len(data), 3):
    codon = data[i:i + 3]
    freq_map[codon] = freq_map.get(codon, 0) + 1
  codon_counts = list(freq_map.iteritems())
  codon_counts = sorted(codon_counts, key=lambda x: x[1], reverse=True)
  for codon, count in codon_counts:
    print "%s: %s" % (codon, count)
  print "number of codons: %s" % len(codon_counts)



def encode_data(data):
  return data


def decode_data(data):
  return data


def encode_decode(fname):
  data = read_file(fname)
  codon_frequencies(data)
  print "Data length: %s" % len(data)
  encoded = encode_data(data)
  print "Encoded length: %s" % len(encoded)
  decoded = decode_data(data)
  print "Decoded length: %s" % len(decoded)
  print "Original == Decoded (ie lossless)? %s" % (data == decoded)



if __name__ == '__main__':
  test_morse_code("Cedric and Alexia are l33t hackerz")
  # encode_decode('../genomics/chrM.fa')





