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

wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chrM.fa.gz'
gunzip chrM.fa.gz
mv chrM.fa human.chrM.fa

wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/canFam2/chromosomes/chrM.fa.gz'
gunzip chrM.fa.gz
mv chrM.fa genomics/dog.chrM.fa

Problems
how many genes?
decode a gene
decode all genes
length of genes
most common codons


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
  print(morse_code)
  message = from_morse_code(morse_code)
  print(message)


codon_amino_acid_map = {
    "AAA": "Lysine",
    "AAC": "Asparagine",
    "AAG": "Lysine",
    "AAT": "Asparagine",
    "ACA": "Threonine",
    "ACC": "Threonine",
    "ACG": "Threonine",
    "ACT": "Threonine",
    "AGA": "Arginine",
    "AGC": "Serine",
    "AGG": "Arginine",
    "AGT": "Serine",
    "ATA": "Isoleucine",
    "ATC": "Isoleucine",
    "ATG": "Methionine",
    "ATT": "Isoleucine",
    "CAA": "Glutamine",
    "CAC": "Histidine",
    "CAG": "Glutamine",
    "CAT": "Histidine",
    "CCA": "Proline",
    "CCC": "Proline",
    "CCG": "Proline",
    "CCT": "Proline",
    "CGA": "Arginine",
    "CGC": "Arginine",
    "CGG": "Arginine",
    "CGT": "Arginine",
    "CTA": "Leucine",
    "CTC": "Leucine",
    "CTG": "Leucine",
    "CTT": "Leucine",
    "GAA": "Glutamic_acid",
    "GAC": "Aspartic_acid",
    "GAG": "Glutamic_acid",
    "GAT": "Aspartic_acid",
    "GCA": "Alanine",
    "GCC": "Alanine",
    "GCG": "Alanine",
    "GCT": "Alanine",
    "GGA": "Glycine",
    "GGC": "Glycine",
    "GGG": "Glycine",
    "GGT": "Glycine",
    "GTA": "Valine",
    "GTC": "Valine",
    "GTG": "Valine",
    "GTT": "Valine",
    "TAA": "Stop",
    "TAC": "Tyrosine",
    "TAG": "Stop",
    "TAT": "Tyrosine",
    "TCA": "Serine",
    "TCC": "Serine",
    "TCG": "Serine",
    "TCT": "Serine",
    "TGA": "Stop",
    "TGC": "Cysteine",
    "TGG": "Tryptophan",
    "TGT": "Cysteine",
    "TTA": "Leucine",
    "TTC": "Phenylalanine",
    "TTG": "Leucine",
    "TTT": "Phenylalanine",
}

start_codon = "ATG"
stop_codons = ("TAA", "TAG", "TGA")


def read_dna_file(fname):
  data = ''
  for line in open(fname):
    data += line.strip().upper()
  return data


def find_gene(dna):
  i = dna.find(start_codon)
  gene = []
  while i < len(dna) and dna[i:i + 3] not in stop_codons:
    gene.append(codon_amino_acid_map[dna[i:i + 3]])
    i += 3
  return gene


def explore_genetics(fname):
  dna = read_dna_file(fname)
  number_of_genes = dna.count(start_codon)
  print('number of genes: %s' % number_of_genes)
  print('number of amino acids: %s' % len(set(codon_amino_acid_map.values())))
  gene = find_gene(dna)
  print('first gene: %s' % gene)


if __name__ == '__main__':
  test_morse_code("Cedric and Alexia are l33t hackerz")
  explore_genetics('../genomics/human.chrM.fa')





