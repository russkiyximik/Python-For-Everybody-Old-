# Given an input string of DNA nucleotide bases, this program will find all of a particular type and tell us where it is
# in the sequence. I will eventually make it so that it will ask which specific base you want.
from pprint import pprint

input = """gccgatcaatgctagagtcaactaccattggagggtacagtattaagcttggtgcacttagatgcggacaagtgagactataaggacccgagttgatgtgcagtttcaaggcttgaacggcgatttttatacttcgtttgataagtcaccctcacgaaagcaagcgtccccgtattgcaaggcaatgaaaccgacaatga"""
positions = []
dict = {}

# The program will find all mentions of the adenine nucleotide.
for i in range(len(input)):
    if input[i] == "a":
        positions.append(i+1)

for i in range(len(positions)):
    dict[i] = positions[i]

print("Format: \n\n(n)-th occurence: position\n")
pprint(dict)
