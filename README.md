
# Python for Bioinformatics | Humber Polytechnic

A collection of Python programming labs, assignments, and projects completed as part of the **Clinical Bioinformatics program at Humber Polytechnic**.

This repository documents my progression in learning Python programming, from foundational concepts to their applications in bioinformatics, molecular biology, and healthcare data management.

As the course progresses, this repository will be updated with additional labs, assignments, and the final course project.

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

**File:** `Lab_1_MolarityCalculator.py`

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

#### Bioinformatics and Laboratory Relevance

Preparing solutions with accurate concentrations is fundamental to molecular biology and laboratory research.

This exercise demonstrates how Python can automate routine scientific calculations, reducing the need for manual computation.

---

### 2. Complementary DNA Sequence

**File:** `Lab_1_ComplementaryDNA.py`

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

#### Bioinformatics Relevance

DNA sequence manipulation is a foundational task in computational biology.

Understanding nucleotide complementarity is important for applications involving:

- DNA sequence analysis
- Primer design
- Sequence alignment
- Molecular genetics

---

## 🏥 Lab 2: Patient Data Management

### 3. Managing Patient Records Using Python Lists

**File:** `Lab_2_Patient_Data_Management.py`

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

#### Healthcare Data Relevance

Managing patient records introduces essential concepts used in healthcare informatics and clinical data processing.

This exercise provides foundational experience with data organization and manipulation, which can later be extended to structured clinical datasets and database systems.

*Note: The patient records used in this exercise are fictional and intended for educational purposes.*

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

## 🚀 Future Development

This repository will continue to expand as I progress through the course.

Future additions will include:

- Additional Python programming labs
- Bioinformatics assignments
- More advanced biological data processing
- Final course project

---

## 👨‍💻 Author

**Nafis Mohammad**  
Clinical Bioinformatics | Humber Polytechnic

**Research Interests:** Bioinformatics, Computational Biology, Cancer Genomics, and Biomedical Data Analysis
