#Complementing DNA

#DNA

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Complement DNA sequence
#Can't do capital letters as it will replace the letters that have already been replaced. So, we will use lower case letters to replace the capital letters and then convert the final result to upper case.    

dna = dna.replace ("A", "t")

dna = dna.replace ("T", "a")

dna = dna.replace ("C", "g")

dna = dna.replace ("G", "c")

complementary_dna = dna.upper()

#Display result

print (complementary_dna)