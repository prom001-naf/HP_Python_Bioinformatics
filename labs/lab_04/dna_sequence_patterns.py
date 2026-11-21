# Function to calculate the reverse complementary DNA strand
def reverse_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

# Empty string to hold the reverse complement sequence
    reverse_sequence = ""

    for base in reversed(sequence):
        reverse_sequence += complement[base]

    return reverse_sequence


# Function to search for TATAxxxATGxxxT
def find_pattern(sequence):

    # The pattern is 14 bases long
    for position in range(len(sequence) - 13):

        # TATA must be first
        # positions 4, 5, 6 can be any bases
        # ATG must come next
        # positions 10, 11, 12 can be any bases
        # final base must be T

        if (sequence[position:position + 4] == "TATA" and
            sequence[position + 7:position + 10] == "ATG" and
            sequence[position + 13] == "T"):

            return position

    return -1


# Function to check both the forward and reverse complementary strands
def check_sequence(sequence):

    print("Original DNA sequence:", sequence)

    # Check forward strand
    forward_position = find_pattern(sequence)

    if forward_position != -1:
        print("Pattern found in the FORWARD strand.")
        print("Position:", forward_position)
        print("Pattern:",
              sequence[forward_position:forward_position + 14])
        return

    # Calculate reverse complement
    reverse_sequence = reverse_complement(sequence)

    # Check reverse complementary strand
    reverse_position = find_pattern(reverse_sequence)

    if reverse_position != -1:
        print("Pattern found in the REVERSE COMPLEMENTARY strand.")
        print("Reverse complement:", reverse_sequence)
        print("Position in reverse complement:", reverse_position)
        print("Pattern:",
              reverse_sequence[reverse_position:reverse_position + 14])
        return

    print("Pattern was NOT found in either strand.")
