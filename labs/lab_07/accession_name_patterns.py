"""Lab 7: Find gene accession names using regular expressions."""

import re


accession_names = [
    "xkn59438",
    "yhdck2",
    "eihd39d9",
    "chdsye847",
    "hedle3455",
    "xjhd53e",
    "45da",
    "de37dp",
]

# A: The accession contains the digit 5 anywhere.
print("Part A:")
for accession in accession_names:
    if re.search(r"5", accession):
        print(accession)

# B: A d occurs before an e, with any number of characters between them.
print("\nPart B:")
for accession in accession_names:
    if re.search(r"d.*e", accession):
        print(accession)

# C: Exactly one letter occurs between d and e.
print("\nPart C:")
for accession in accession_names:
    if re.search(r"d[A-Za-z]e", accession):
        print(accession)

# D: Both letters occur, either d before e or e before d.
print("\nPart D:")
for accession in accession_names:
    if re.search(r"d.*e|e.*d", accession):
        print(accession)

# E: The last two characters are da, dr or dp.
print("\nPart E:")
for accession in accession_names:
    if re.search(r"d[arp]$", accession):
        print(accession)
