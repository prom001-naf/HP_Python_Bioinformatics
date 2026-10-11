# Part 1: Calculate the estimated molecular weight of Rattus norvegicus PKC Beta-1 protein

protein_sequence = """MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC
CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH
KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ
KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ
EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK
GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM
EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE
NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY
PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF
DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV"""

# Remove newline characters
protein_sequence = protein_sequence.replace('\r', '').replace('\n', '')

# Calculate protein length
protein_length = len(protein_sequence)

# Average molecular weight = 110 Daltons per amino acid
molecular_weight = protein_length * 110

# Convert Daltons to kilodaltons
molecular_weight_kda = molecular_weight / 1000

print('The length of "Protein kinase C beta type" is:', protein_length)
print("The average weight of this protein sequence in kilodaltons")
print("is:", round(molecular_weight_kda, 2))




# Part 2: Hard-coded DNA sequences

dna_sequences = [
    "ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC",
    "ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT",
    "ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC",
    "ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA",
    "ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA"
]

adapter_length = 14

# Loop through each sequence
for sequence in dna_sequences:

    # Remove the first 14 bases
    trimmed_sequence = sequence[adapter_length:]

    # Print cleaned sequence and length
    print("Trimmed sequence:", trimmed_sequence)
    print("Length:", len(trimmed_sequence))



# Part 3: Generating random DNA sequences

import random

# List of possible DNA nucleotides
nucleotides = ["A", "T", "C", "G"]

# Empty string to store the random DNA sequence
dna_sequence = ""

# Generate a random DNA sequence of 1001 bases
for i in range(1001):

    random_index = random.randint(0, 3)

    dna_sequence = dna_sequence + nucleotides[random_index]

# Count each nucleotide
a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
c_count = dna_sequence.count("C")
g_count = dna_sequence.count("G")

# Calculate the percentage of each nucleotide
a_percentage = (a_count / len(dna_sequence)) * 100
t_percentage = (t_count / len(dna_sequence)) * 100
c_percentage = (c_count / len(dna_sequence)) * 100
g_percentage = (g_count / len(dna_sequence)) * 100

# Print the generated DNA sequence
print("Random DNA sequence:")
print(dna_sequence)

# Print the percentages
print("A percentage:", round(a_percentage, 2), "%")
print("T percentage:", round(t_percentage, 2), "%")
print("C percentage:", round(c_percentage, 2), "%")
print("G percentage:", round(g_percentage, 2), "%")

# No, I do not get the same random DNA sequence each time the program is run.
# This is because random.randint() randomly selects nucleotides each time.