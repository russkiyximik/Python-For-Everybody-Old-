# Given an input string of DNA nucleotide bases, this program will find all of a particular type and tell us where it is
# in the sequence. I will eventually make it so that it will ask which specific base you want.
from pprint import pprint

seq = """gccgatcaatgctagagtcaactaccattggagggtacagtattaagcttggtgcacttagatgcggacaagtgagactataaggacccgagttgatgtgcagtttcaaggcttgaacggcgatttttatacttcgtttgataagtcaccctcacgaaagcaagcgtccccgtattgcaaggcaatgaaaccgacaatga"""
positions = []
dict = {}

ask = input("What base would you like to know the positions of? Selections: a, g, c, t\n")
print(ask)

# The program will find all mentions of the adenine nucleotide.
for i in range(len(seq)):
    if seq[i] == ask.strip().lower():
        positions.append(i+1)

for i in range(len(positions)):
    dict[i] = positions[i]

print(len(positions), "matching bases found \n\nFormat: \n\n(n)-th occurence: position\n")
pprint(dict)
