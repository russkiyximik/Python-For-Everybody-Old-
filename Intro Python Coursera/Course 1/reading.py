# Given an input string of DNA nucleotide bases, this program will find all of a particular type and tell us where it is
# in the sequence. I will eventually make it so that it will ask which specific base you want.
from pprint import pprint

seq = """gccgatcaatgctagagtcaactaccattggagggtacagtattaagcttggtgcacttagatgcggacaagtgagactataaggacccgagttgatgtgcagtttcaaggcttgaacggcgatttttatacttcgtttgataagtcaccctcacgaaagcaagcgtccccgtattgcaaggcaatgaaaccgacaatga"""
dict = {}
ask = input("What base would you like to know the positions of? Selections: a, g, c, t\n").strip().lower()

for i in range(len(seq)):
    dict[seq[i]] = dict.get(seq[i], 0) + 1

print(dict[ask], "matching bases found \n")
pprint(dict)
