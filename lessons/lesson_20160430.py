"""
Problems
how many genes?
decode a gene
decode all genes
length of genes
most common codons

wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chrM.fa.gz'
gunzip chrM.fa.gz
mv chrM.fa human.chrM.fa

wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/canFam2/chromosomes/chrM.fa.gz'
gunzip chrM.fa.gz
mv chrM.fa genomics/dog.chrM.fa

"""


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


dna = ''.join(map(str.strip, open('../genomics/human.chrM.fa').readlines()))
print(dna[:200])

num_genes = 0
gene = []
genes = []
in_gene = False
i = 0
while i < len(dna):
  codon = dna[i:i + 3].upper()
  if in_gene or codon == start_codon:
    in_gene = True
    if codon in stop_codons:
      in_gene = False
      genes.append(gene)
      gene = []
    else:
      gene.append(codon_amino_acid_map[codon])
    i += 3
  else:
    i += 1

print("num genes:", len(genes))
for gene in genes:
  print(gene)








