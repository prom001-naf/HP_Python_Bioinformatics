CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAG': '*'
}


def transcribe_dna_to_rna(dna_sequence: str):
    """Replace DNA's T bases with U. Report invalid bases and return None."""
    dna_sequence = dna_sequence.upper()

    for base in dna_sequence:
        if base not in 'ACGT':
            print(f"Error: Invalid DNA base '{base}'. Use only A, C, G, and T.")
            return None

    return dna_sequence.replace('T', 'U')


def translate_rna_to_protein(rna_sequence: str, codon_table: dict):
    """Map RNA triplets to amino acids. Report unmapped codons and return None."""
    rna_sequence = rna_sequence.upper()
    protein_sequence = ''

    for index in range(0, len(rna_sequence), 3):
        codon = rna_sequence[index:index + 3]

        try:
            protein_sequence += codon_table[codon]
        except KeyError:
            print(f"Error: RNA codon '{codon}' is invalid or incomplete.")
            return None

    return protein_sequence


# Main Program Execution------------------------------
def main():
    """Read DNA and display its protein sequence or an error."""
    dna_sequence = input('Enter a DNA sequence: ').strip()
    rna_sequence = transcribe_dna_to_rna(dna_sequence)

    if rna_sequence is None:
        return

    protein_sequence = translate_rna_to_protein(rna_sequence, CODON_TABLE)

    if protein_sequence is not None:
        print(f'Protein sequence: {protein_sequence}')


# Assertions---------------------------------
def test_functions():
    """Run these assertions by calling test_functions()."""
    # Test valid DNA, lowercase input, empty input, and invalid bases.
    assert transcribe_dna_to_rna('ATGCGT') == 'AUGCGU'
    assert transcribe_dna_to_rna('ACG') == 'ACG'
    assert transcribe_dna_to_rna('atgc') == 'AUGC'
    assert transcribe_dna_to_rna('') == ''
    assert transcribe_dna_to_rna('ATX') is None
    assert transcribe_dna_to_rna('ATU') is None

    # Test amino acids, stop codons, empty RNA, and unmapped codons.
    assert translate_rna_to_protein('AUGGCU', CODON_TABLE) == 'MA'
    assert translate_rna_to_protein('UUUCCCGGG', CODON_TABLE) == 'FPG'
    assert translate_rna_to_protein('UAAUGAUAG', CODON_TABLE) == '***'
    assert translate_rna_to_protein('', CODON_TABLE) == ''
    assert translate_rna_to_protein('AUGXXX', CODON_TABLE) is None
    assert translate_rna_to_protein('AUGGC', CODON_TABLE) is None
    assert translate_rna_to_protein('AUG', {}) is None


if __name__ == '__main__':
    main()
