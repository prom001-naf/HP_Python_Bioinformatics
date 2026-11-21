"""
Lab 6: Eukaryote genome data

"""

from pathlib import Path
import sys

import pandas as pd


# STEP 1: Load the tab-separated data.
# By default, the TSV is expected.
# A path can also be supplied as the first command-line argument.
data_path = (
    Path(sys.argv[1])
    if len(sys.argv) > 1
    else Path(__file__).parent / "data" / "eukaryotes.tsv"
)

# Set text and integer column types explicitly.
# The source uses "-" to represent missing gene/protein counts, so those values as missing.
column_types = {
    "Species": "string",
    "Kingdom": "string",
    "Class": "string",
    "Assembly status": "string",
    "Number of genes": "Int64",
    "Number of proteins": "Int64",
}
euk = pd.read_csv(
    data_path,
    sep="\t",
    dtype=column_types,
    na_values=["-"],
)


# STEP 2: Investigate the structure and contents of the DataFrame.
print("First five records:")
print(euk.head().to_string(index=False))
print("\nDataFrame information:")
euk.info()
print(f"\nNumber of rows: {euk.shape[0]}")
print(f"Number of columns: {euk.shape[1]}")
print("\nMissing values by column:")
print(euk.isna().sum().to_string())


# PART A: Keep rows with Size (Mb) below 4,000 and drop rows with any missing values.
# The result is stored in the euk_float DataFrame.
euk_float = euk.loc[euk["Size (Mb)"] < 4000].dropna()
print(f"\nPart A: euk_float contains {len(euk_float)} complete rows.")


# PART B: Calculate proteins divided by genes and keep ratios >= 1.1.
# Exclude the missing counts and zero gene counts because a ratio cannot be calculated for those records.
protein_gene_ratio = euk["Number of proteins"].div(euk["Number of genes"])
euk_filtered = euk.loc[
    euk["Number of genes"].gt(0) & protein_gene_ratio.ge(1.1)
]
print(
    "Part B: euk_filtered contains "
    f"{len(euk_filtered)} rows with at least 1.1 proteins per gene."
)


# PART C: Select fungi with genome sizes strictly greater than 100 Mb.
large_fungi = euk.loc[
    euk["Kingdom"].eq("Fungi") & euk["Size (Mb)"].gt(100)
]
# List each distinct species/assembly label once, in alphabetical order.
fungal_species = (
    large_fungi["Species"].dropna().drop_duplicates().sort_values()
)
print(
    "\nPart C: "
    f"{len(fungal_species)} fungal species/assembly labels have genomes "
    "larger than 100 Mb:"
)
for species in fungal_species:
    print(f"- {species}")


# WRITTEN ANSWERS
#
# A. euk_float has 2,365 rows. The code first selects Size (Mb) values
#    below 4,000, then dropna() removes any selected row with a missing value.
#
# B. euk_filtered has 547 rows. These records each have at least 1.1
#    proteins per gene; records without a positive gene count are omitted
#    because their ratio is undefined.
#
# C. There are 57 distinct fungal species/assembly labels above 100 Mb. Their names are printed above.
#