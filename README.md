
# Python for Bioinformatics | Humber Polytechnic

A collection of Python programming labs, assignments, and projects completed as part of the **Clinical Bioinformatics program at Humber Polytechnic**.

This repository documents coursework in Python programming, bioinformatics, molecular biology, and healthcare data management.

## Repository organization

Assignments and labs are grouped into numbered folders. Each folder contains the available source, brief, and required input data.

```text
assignments/assignment_01/
labs/lab_01/ through labs/lab_07/
```

- [Assignment 1](assignments/assignment_01/)
- [Labs 1–5](labs/)
- [Lab 6 source, brief, and dataset](labs/lab_06/)
- [Lab 7 source and brief](labs/lab_07/)

Use Python 3 to run the scripts. Lab 6 requires pandas and reads `data/eukaryotes.tsv` by default; an alternate TSV path may be supplied as the first command-line argument. Install pandas with `python -m pip install pandas` if needed.

---

## 📚 Course Overview

**Institution:** Humber Polytechnic  
**Program:** Clinical Bioinformatics (Ontario Graduate Certificate)  
**Programming Language:** Python  
**Focus:** Python Programming for Bioinformatics

### Learning Objectives

- Develop foundational Python programming skills.
- Work with variables, data types, lists, and user inputs.
- Implement mathematical calculations relevant to laboratory science.
- Manipulate biological sequences programmatically.
- Organize and manage structured healthcare information.
- Develop problem-solving skills for future bioinformatics applications.

---

## 🧪 Lab 1: Python Fundamentals and Biological Applications

### 1. Molarity Calculator

**File:** [`interactive_molarity_calculator.py`](labs/lab_01/interactive_molarity_calculator.py)

#### Objective

Develop an interactive Python program that calculates the mass of a chemical compound required to prepare a solution with a specified molarity.

#### Methodology

The program requests three inputs from the user:

1. Molecular mass of the compound (g/mol).
2. Desired solution volume (mL).
3. Desired molar concentration (mol/L).

The required mass is calculated using:

**Mass (g) = Concentration (mol/L) × Volume (L) × Molecular Mass (g/mol)**

Since the user provides volume in millilitres, the program must convert it to litres before performing the calculation.

#### Programming Concepts

- Variable assignment
- User input using `input()`
- Numeric data type conversion
- Arithmetic operations
- Unit conversion
- Formatted output using `print()`

---

### 2. Complementary DNA Sequence

**File:** [`complementing_dna.py`](labs/lab_01/complementing_dna.py)

#### Objective

Create a Python program that generates the complementary DNA sequence of a given nucleotide sequence.

#### Input Sequence

```text
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
```

#### Methodology

The program applies the complementary DNA base-pairing rules:

| Original Base | Complementary Base |
|---------------|--------------------|
| A (Adenine) | T (Thymine) |
| T (Thymine) | A (Adenine) |
| C (Cytosine) | G (Guanine) |
| G (Guanine) | C (Cytosine) |

The exercise focuses on using Python string manipulation to replace nucleotides and construct the complementary sequence.

#### Programming Concepts

- String manipulation
- Character replacement
- DNA sequence representation
- Sequential operations
- String immutability

---

## 🏥 Lab 2: Patient Data Management

### 3. Managing Patient Records Using Python Lists

**File:** [`patient_data_management.py`](labs/lab_02/patient_data_management.py)

#### Objective

Develop a Python program that demonstrates how lists can be used to store, update, search, and consolidate patient records.

This exercise introduces basic data management operations using a simulated healthcare setting.

#### Tasks

**1. Creating and Accessing Patient Records**

- Initialize a list containing four patient names.
- Retrieve the second patient using list indexing.

**2. Adding New Patients**

- Append a new patient, Sarah Miller, to the existing list.

**3. Updating Patient Information**

- Correct a misspelled patient name from Emily White to Emily Williams.

**4. Merging Patient Records**

- Create a second list representing another healthcare provider.
- Combine both lists into a single consolidated patient list.

**5. Searching Patient Records**

- Prompt the user to enter a patient name.
- Check whether the name exists in the list.
- Return a Boolean result (`True` or `False`).

**6. Inserting Multiple Patient Records**

- Accept multiple patient names separated by commas.
- Request an insertion index from the user.
- Insert the new patient names beginning at the specified position.

#### Programming Concepts

- Python lists
- Zero-based indexing
- List modification
- `append()` and `insert()`
- List concatenation
- Membership testing using `in`
- Boolean expressions
- User input processing
- String splitting using `split()`

*Note: The patient records used in this exercise are fictional and intended for educational purposes.*

---

## 🧪 Lab 3: Dynamic Laboratory Protocol and Error Handling

### 1. Dynamic Protocol Calculator

**File:** [`dynamic_protocol.py`](labs/lab_03/dynamic_protocol.py)

#### Objective

Modify an existing Python laboratory protocol program to allow users to dynamically calculate the volumes of stock solutions required to prepare a solution with specified final concentrations.

The program must replace hard-coded values with interactive user inputs and implement error handling to manage invalid inputs.

#### Methodology

The program prompts the user to enter five values:

1. Final volume of the solution (mL).
2. NaCl stock concentration (mM).
3. NaCl desired final concentration (mM).
4. MgCl2 stock concentration (mM).
5. MgCl2 desired final concentration (mM).

The required volume of each stock solution is calculated using the dilution equation:

**C₁V₁ = C₂V₂**

Rearranging to calculate the volume of stock solution:

**V₁ = (C₂ × V₂) / C₁**

Where:

- **C₁:** Stock concentration
- **V₁:** Volume of stock solution required
- **C₂:** Desired final concentration
- **V₂:** Final solution volume

The program calculates the required volumes of NaCl and MgCl2 and provides instructions for preparing the final solution.

The script also implements a `try/except` structure to handle at least two types of errors:

- **ValueError:** Occurs when the user enters a non-numeric value.
- **ZeroDivisionError:** Occurs when a stock concentration of zero causes division by zero.

#### Example Input and Output

```text
Please enter the final volume of the solution (ml): 3
Please enter the NaCl stock (mM): 1000
Please enter the NaCl final (mM): 10
Please enter the MgCl2 stock (mM): 100
Please enter the MgCl2 final (mM): 0.5

Add 0.03 ml NaCl
Add 0.015 ml MgCl2
Add water to a final volume of 3.0 ml and mix
```

#### Programming Concepts

- Variable assignment
- Interactive user input using `input()`
- Numeric conversion using `float()`
- Mathematical calculations
- Functions and program modification
- Exception handling using `try/except`
- Handling `ValueError` and `ZeroDivisionError`
- Dynamic input processing
- Formatted output using `print()`

---

## 📝 Assignment 1: Python Programming Fundamentals and Sequence Analysis

### Assignment Overview

This assignment introduces Python programming through protein sequence calculations, DNA sequence processing, and random sequence generation.

The assignment source implements all three tasks in one script. The [Python source](assignments/assignment_01/assignment_01_calc_daltons.py) and [assignment brief](assignments/assignment_01/assignment_01_brief.pdf) are included in the repository.

The assignment focuses on three main areas:

1. Protein sequence length and molecular-weight calculation
2. Trimming a fixed adapter from DNA sequences
3. Generating random DNA and calculating nucleotide percentages

---

### 1. Calculate Protein Molecular Weight

**File:** [assignment source](assignments/assignment_01/assignment_01_calc_daltons.py)

#### Objective

Estimate the molecular weight in kilodaltons of the *Rattus norvegicus* PKC Beta-1 protein using an average of 110 Daltons per amino acid.

#### Methodology

The protein sequence is stored as a multiline string. Newline characters are removed before calculating sequence length. The script multiplies the number of amino acids by 110 Daltons and divides by 1,000 to convert Daltons to kilodaltons.

```python
protein_sequence = protein_sequence.replace("\r", "").replace("\n", "")
protein_length = len(protein_sequence)
molecular_weight = protein_length * 110
molecular_weight_kda = molecular_weight / 1000
```

#### Output Example

```text
The length of "Protein kinase C beta type" is: 671
The average weight of this protein sequence in kilodaltons
is: 73.81
```

#### Programming Concepts

- Multiline strings
- String replacement and length calculation
- Variables and arithmetic operations
- Unit conversion
- Formatted output using `print()`

---

### 2. Trim DNA Adapter Sequences

**File:** [assignment source](assignments/assignment_01/assignment_01_calc_daltons.py)

#### Objective

Remove the shared 14-base-pair sequencing adapter from each DNA sequence, then display each cleaned sequence and its length.

#### Methodology

The five input sequences are stored in a list. A loop processes each sequence, uses slicing to remove its first 14 bases, and prints the remaining sequence and its length.

```python
adapter_length = 14

for sequence in dna_sequences:
    trimmed_sequence = sequence[adapter_length:]
    print("Trimmed sequence:", trimmed_sequence)
    print("Length:", len(trimmed_sequence))
```

#### Programming Concepts

- Lists of strings
- `for` loops
- String slicing
- Sequence length with `len()`
- Repeated output for each input sequence

---

### 3. Generate Random DNA Sequences

**File:** [assignment source](assignments/assignment_01/assignment_01_calc_daltons.py)

#### Objective

Generate a random DNA sequence that is 1,001 bases long and report the percentage of each nucleotide.

#### Methodology

The script selects nucleotides from a list containing A, T, C, and G using `random.randint()`. It appends 1,001 randomly selected bases to a string, counts each nucleotide, and calculates each percentage relative to the sequence length. A code comment answers whether repeated runs produce the same sequence.

#### Programming Concepts

- Importing and using the `random` module
- Lists and indexed selection
- Loops and string concatenation
- Counting characters with `str.count()`
- Calculating percentages
- Rounding and displaying results

---

### Assignment Instructions

- Submit Python source files through the course assignment portal.
- Write answers in your own words.
- The brief allows up to two submissions and specifies its late-submission policy.

---

## 🛠️ Technical Skills Developed

| Category | Skills |
|----------|--------|
| Programming Language | Python |
| Data Structures | Strings, Lists |
| Data Types | Integers, Floats, Strings, Booleans |
| Input and Output | `input()`, `print()` |
| Data Manipulation | Indexing, Updating, Inserting, Concatenation |
| Scientific Computing | Molarity Calculations, Unit Conversion |
| Sequence Analysis | DNA Complementation |
| Healthcare Applications | Basic Patient Record Management |

---

## 🎯 Key Learning Outcomes

Through these assignments, I have gained practical experience in:

1. Writing interactive Python scripts to solve scientific problems.
2. Applying mathematical formulas to laboratory calculations.
3. Manipulating nucleotide sequences using programming techniques.
4. Organizing and modifying healthcare-related data.
5. Using Python data structures to perform common data management operations.

These foundational skills support my continued development in bioinformatics, computational biology, and clinical data analysis.

---

## 🧬 Lab 4: DNA Pattern Searching and Reverse Complement Analysis

### 1. Searching for DNA Sequence Patterns

**File:** [`dna_sequence_patterns.py`](labs/lab_04/dna_sequence_patterns.py)

#### Objective

Develop a Python program that identifies a specific nucleotide pattern within a DNA sequence.

The program must search both the forward DNA strand and its reverse complementary strand to determine whether the target pattern is present.

The program must also report the position of the detected pattern and distinguish between sequences containing the pattern and those without a match.

#### Target DNA Pattern

```text
TATAxxxATGxxxT
```

Where:

- **TATA:** A fixed four-nucleotide sequence.
- **xxx:** Any three consecutive DNA nucleotides (A, T, C, or G).
- **ATG:** A fixed three-nucleotide sequence.
- **T:** A fixed final nucleotide.

The complete target pattern contains 14 nucleotides.

An example of a valid matching sequence is:

```text
TATAACGATGGCAT
```

#### Methodology

The program searches DNA sequences for the specified nucleotide pattern using string operations and pattern-matching techniques.

The implementation can be divided into two primary functions:

**1. Reverse Complement Function**

A function generates the reverse complementary strand of a DNA sequence by applying nucleotide base-pairing rules and reversing the resulting sequence.

| Original Base | Complementary Base |
|---------------|--------------------|
| A (Adenine) | T (Thymine) |
| T (Thymine) | A (Adenine) |
| C (Cytosine) | G (Guanine) |
| G (Guanine) | C (Cytosine) |

**2. DNA Pattern Search Function**

A second function searches a DNA sequence for the target pattern:

```text
TATAxxxATGxxxT
```

The program must ensure that:

- The fixed nucleotide regions appear in the correct order.
- The `xxx` positions represent variable bases. The submitted script checks the fixed motif positions and does not separately validate the variable bases.
- The pattern is searched on both the forward and reverse complementary strands.
- The position of each detected pattern is reported.

#### Test Cases

The program must demonstrate three different scenarios.

**Test Case 1: Pattern Present in the Forward Strand**

Use a DNA sequence containing the target pattern in its forward orientation.

Expected behavior:

- Identify the pattern in the forward strand.
- Print a message confirming the match.
- Display the position where the pattern begins.

**Test Case 2: Pattern Present in the Reverse Complementary Strand**

Use a DNA sequence whose reverse complement contains the target pattern.

Expected behavior:

- Generate the reverse complementary sequence.
- Identify the pattern in the reverse complement.
- Print a message confirming the match.
- Display the position of the pattern.

**Test Case 3: Pattern Not Present**

Use a DNA sequence that does not contain the target pattern in either orientation.

Expected behavior:

- Search the forward DNA strand.
- Search the reverse complementary strand.
- Print a message indicating that no matching pattern was found.

#### Programming Concepts

- Python functions using `def`
- Function parameters and return values
- String manipulation
- DNA sequence representation
- String slicing and indexing
- Reverse complementary DNA generation
- Pattern matching and sequence searching
- Conditional statements using `if/else`
- Iteration through nucleotide sequences
- Test case development
- Formatted output using `print()`

---

## 🧪 Lab 5: DNA Transcription and Translation

### DNA Sequence Transcription and Translation

**Files:** [Python source](labs/lab_05/dna_transcription_translation.py) and [lab brief](labs/lab_05/lab_05_brief.pdf).

#### Objective

Complete a program that accepts a DNA sequence, validates its bases, transcribes it to RNA, and translates the RNA codons into an amino-acid sequence.

#### Methodology

The program converts the input to uppercase, checks that each DNA base is A, C, G, or T, and replaces T with U to transcribe DNA to RNA. It processes the RNA sequence in triplets and looks up each codon in a codon table. Stop codons are represented by `*`. Invalid bases and incomplete or unmapped codons produce an error message.

The source defines a `test_functions()` function with assertions for valid and lowercase DNA, empty input, invalid bases, valid amino-acid translation, stop codons, incomplete codons, and missing codon-table entries. Call `test_functions()` explicitly to run those assertions.

#### Example Input and Output

For the input DNA sequence `ATGGCT`, the program transcribes `AUGGCU` and reports the protein sequence `MA`.

#### Programming Concepts

- Function definitions, parameters, and return values
- String normalization and validation
- DNA-to-RNA transcription
- Codon-table lookup
- Iteration over sequence triplets
- Exception handling for missing codons
- Assertions for function checks

---

## 🧪 Lab 6: Eukaryote Genome Data Analysis

**Files:** [analysis script](labs/lab_06/eukaryotes_analysis.py), [input dataset](labs/lab_06/data/eukaryotes.tsv), and [lab brief](labs/lab_06/lab_06_brief.pdf).

#### Objective

Use pandas to inspect a tab-separated eukaryote genome dataset, filter records, calculate protein-to-gene ratios, and identify fungal species with larger genomes.

#### Methodology

The script reads the TSV with explicit text and nullable-integer column types and treats `-` as a missing value. It reports sample rows, data types, dimensions, and missingness before completing three analyses:

1. Create `euk_float` from rows with `Size (Mb)` below 4,000, then drop rows containing missing values.
2. Create `euk_filtered` for records with a positive gene count and at least 1.1 proteins per gene.
3. List distinct fungal species or assembly labels with genome sizes greater than 100 Mb.

The dataset is loaded from the lab folder by default. An alternate TSV path can be supplied as the first command-line argument. The script reports 2,365 complete rows for Part A, 547 rows for Part B, and 57 fungal species or assembly labels for Part C.

#### Example Command

```bash
python eukaryotes_analysis.py
```

To use another TSV file:

```bash
python eukaryotes_analysis.py path/to/eukaryotes.tsv
```

#### Programming Concepts

- Reading tab-separated data with `pandas.read_csv()`
- Explicit data types and missing-value handling
- DataFrame inspection and summary methods
- Boolean filtering and missing-value removal
- Calculating ratios with aligned Series
- Selecting, deduplicating, and sorting values
- Command-line arguments with `sys.argv`

---

## 🧪 Lab 7: Accession-Name Pattern Matching

**Files:** [Python source](labs/lab_07/accession_name_patterns.py) and [lab brief](labs/lab_07/lab_07_brief.pdf).

#### Objective

Use Python regular expressions to select made-up gene accession names that match five independent criteria.

#### Accession Names

```text
xkn59438, yhdck2, eihd39d9, chdsye847,
hedle3455, xjhd53e, 45da, de37dp
```

#### Tasks and Patterns

| Part | Criterion | Regular Expression |
|------|-----------|--------------------|
| A | Contains the digit 5 | `5` |
| B | Contains d before e, with any number of characters between | `d.*e` |
| C | Contains d followed by exactly one letter and then e | `d[A-Za-z]e` |
| D | Contains d and e in either order | `d.*e|e.*d` |
| E | Ends in d followed by a, r, or p | `d[arp]$` |

Each criterion is processed separately. The script uses `re.search()` to test each accession and prints the matches for that part.

#### Programming Concepts

- Importing and using the `re` module
- Regular-expression character and sequence patterns
- Wildcards and repetition
- Alternation with `|`
- End-of-string anchors with `$`
- Iterating through a list and conditional matching

---

---

## 🚀 Future Development

This repository will continue to expand as additional assignments and labs are completed.

Future additions will include:

- Additional Python programming labs
- Bioinformatics assignments
- More advanced biological data processing

---

## 👨‍💻 Author

**Nafis Mohammad**  
Clinical Bioinformatics | Humber Polytechnic

**Research Interests:** Bioinformatics, Computational Biology, Cancer Genomics, and Biomedical Data Analysis


