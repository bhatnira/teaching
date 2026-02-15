"""
============================================================================
HOMEWORK SOLUTIONS - Python for Cheminformatics & Bioinformatics
============================================================================
AI-Driven Drug Development Training
February 2026

Complete solutions for all 20 homework problems with explanations.
============================================================================
"""

import math
import re
import numpy as np
import pandas as pd

# =============================================================================
# PART 1: BIOINFORMATICS - DNA/RNA/PROTEIN (25 points)
# =============================================================================

# -----------------------------------------------------------------------------
# Problem 1: Counting DNA Nucleotides (5 points)
# Rosalind ID: DNA
# -----------------------------------------------------------------------------
def count_nucleotides(dna):
    """
    Count occurrences of each nucleotide in a DNA string.
    
    Args:
        dna: DNA string containing A, C, G, T
        
    Returns:
        Dictionary with counts of each nucleotide
    """
    # Convert to uppercase for consistency
    dna = dna.upper()
    
    # Validate input
    valid_nucleotides = set("ACGT")
    if not all(nuc in valid_nucleotides for nuc in dna):
        raise ValueError("Invalid nucleotides found. DNA should only contain A, C, G, T")
    
    # Count nucleotides
    counts = {
        "A": dna.count("A"),
        "C": dna.count("C"),
        "G": dna.count("G"),
        "T": dna.count("T")
    }
    
    return counts


# Test Problem 1
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print("Problem 1: Count Nucleotides")
print(f"DNA: {dna[:30]}...")
print(f"Result: {count_nucleotides(dna)}")
# Expected: {"A": 20, "C": 12, "G": 17, "T": 21}
print()


# -----------------------------------------------------------------------------
# Problem 2: Transcribing DNA to RNA (5 points)
# Rosalind ID: RNA
# -----------------------------------------------------------------------------
def transcribe(dna):
    """
    Transcribe DNA to RNA by replacing T with U.
    
    Args:
        dna: DNA string
        
    Returns:
        RNA string
    """
    # Handle edge case
    if not dna:
        return ""
    
    dna = dna.upper()
    
    # Validate input
    valid_nucleotides = set("ACGT")
    if not all(nuc in valid_nucleotides for nuc in dna):
        raise ValueError("Invalid DNA sequence")
    
    # Replace T with U
    return dna.replace("T", "U")


# Test Problem 2
dna = "GATGGAACTTGACTACGTAAATT"
print("Problem 2: Transcribe DNA to RNA")
print(f"DNA: {dna}")
print(f"RNA: {transcribe(dna)}")
# Expected: "GAUGGAACUUGACUACGUAAAUU"
print()


# -----------------------------------------------------------------------------
# Problem 3: Reverse Complement (5 points)
# Rosalind ID: REVC
# -----------------------------------------------------------------------------
def reverse_complement(dna):
    """
    Return the reverse complement of a DNA string.
    
    Args:
        dna: DNA string
        
    Returns:
        Reverse complement string
    """
    dna = dna.upper()
    
    # Complement mapping
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    
    # Validate and complement
    try:
        complemented = "".join(complement[nuc] for nuc in dna)
    except KeyError:
        raise ValueError("Invalid nucleotide in DNA sequence")
    
    # Reverse
    return complemented[::-1]


# Test Problem 3
dna = "AAAACCCGGT"
print("Problem 3: Reverse Complement")
print(f"DNA: {dna}")
print(f"Reverse Complement: {reverse_complement(dna)}")
# Expected: "ACCGGGTTTT"
print()


# -----------------------------------------------------------------------------
# Problem 4: Computing GC Content (5 points)
# Rosalind ID: GC
# -----------------------------------------------------------------------------
def gc_content(dna):
    """
    Calculate the GC content of a DNA sequence.
    
    Args:
        dna: DNA string
        
    Returns:
        GC percentage with 2 decimal places
    """
    dna = dna.upper()
    
    if len(dna) == 0:
        return 0.0
    
    gc_count = dna.count("G") + dna.count("C")
    return round((gc_count / len(dna)) * 100, 2)


def highest_gc(fasta_dict):
    """
    Find the sequence with highest GC content.
    
    Args:
        fasta_dict: Dictionary of {sequence_id: sequence}
        
    Returns:
        Tuple of (sequence_id, gc_percentage)
    """
    max_gc = -1
    max_id = None
    
    for seq_id, sequence in fasta_dict.items():
        gc = gc_content(sequence)
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id
    
    return max_id, max_gc


# Test Problem 4
sequences = {
    "Rosalind_0001": "AGCTATAG",
    "Rosalind_0002": "GCGCGCGC",
    "Rosalind_0003": "ATATATATAT"
}
print("Problem 4: GC Content")
for seq_id, seq in sequences.items():
    print(f"{seq_id}: {gc_content(seq)}%")
print(f"Highest GC: {highest_gc(sequences)}")
print()


# -----------------------------------------------------------------------------
# Problem 5: Translating RNA to Protein (5 points)
# Rosalind ID: PROT
# -----------------------------------------------------------------------------
CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def translate(rna):
    """
    Translate RNA sequence to protein.
    
    Args:
        rna: RNA string
        
    Returns:
        Protein sequence (stops at stop codon)
    """
    rna = rna.upper()
    protein = []
    
    # Process codons (groups of 3)
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        
        if codon in CODON_TABLE:
            amino_acid = CODON_TABLE[codon]
            if amino_acid == "*":  # Stop codon
                break
            protein.append(amino_acid)
        else:
            break  # Invalid codon
    
    return "".join(protein)


# Test Problem 5
rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print("Problem 5: RNA Translation")
print(f"RNA: {rna[:30]}...")
print(f"Protein: {translate(rna)}")
# Expected: "MAMAPRTEINSTRING"
print()


# =============================================================================
# PART 2: CHEMINFORMATICS - MOLECULES & PROPERTIES (25 points)
# =============================================================================

# -----------------------------------------------------------------------------
# Problem 6: Molecular Formula Parser (5 points)
# -----------------------------------------------------------------------------
def parse_formula(formula):
    """
    Parse a molecular formula and return element counts.
    
    Args:
        formula: Molecular formula string (e.g., "H2O", "C6H12O6")
        
    Returns:
        Dictionary of element counts
    """
    def parse_group(formula, multiplier=1):
        """Recursively parse formula groups."""
        counts = {}
        i = 0
        
        while i < len(formula):
            if formula[i] == '(':
                # Find matching closing parenthesis
                depth = 1
                j = i + 1
                while depth > 0:
                    if formula[j] == '(':
                        depth += 1
                    elif formula[j] == ')':
                        depth -= 1
                    j += 1
                
                # Get the number after closing paren
                k = j
                while k < len(formula) and formula[k].isdigit():
                    k += 1
                
                group_mult = int(formula[j:k]) if j < k else 1
                
                # Recursively parse the group
                group_counts = parse_group(formula[i+1:j-1], group_mult * multiplier)
                for elem, count in group_counts.items():
                    counts[elem] = counts.get(elem, 0) + count
                
                i = k
                
            elif formula[i].isupper():
                # Element symbol
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                
                element = formula[i:j]
                
                # Get the count
                k = j
                while k < len(formula) and formula[k].isdigit():
                    k += 1
                
                count = int(formula[j:k]) if j < k else 1
                counts[element] = counts.get(element, 0) + count * multiplier
                
                i = k
            else:
                i += 1
        
        return counts
    
    return parse_group(formula)


# Test Problem 6
formulas = ["H2O", "C6H12O6", "C2H5OH", "NaCl", "Ca(OH)2"]
print("Problem 6: Molecular Formula Parser")
for f in formulas:
    print(f"  {f}: {parse_formula(f)}")
print()


# -----------------------------------------------------------------------------
# Problem 7: Molecular Weight Calculator (5 points)
# -----------------------------------------------------------------------------
ATOMIC_WEIGHTS = {
    "H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999,
    "S": 32.065, "P": 30.974, "Na": 22.990, "Cl": 35.453,
    "Ca": 40.078, "Fe": 55.845, "Mg": 24.305, "K": 39.098
}


def calculate_mw(formula):
    """
    Calculate molecular weight from formula.
    
    Args:
        formula: Molecular formula string
        
    Returns:
        Molecular weight rounded to 3 decimal places
    """
    counts = parse_formula(formula)
    mw = 0
    
    for element, count in counts.items():
        if element not in ATOMIC_WEIGHTS:
            raise ValueError(f"Unknown element: {element}")
        mw += ATOMIC_WEIGHTS[element] * count
    
    return round(mw, 3)


# Test Problem 7
test_compounds = [
    ("Aspirin", "C9H8O4"),
    ("Caffeine", "C8H10N4O2"),
    ("Glucose", "C6H12O6"),
    ("Water", "H2O")
]
print("Problem 7: Molecular Weight Calculator")
for name, formula in test_compounds:
    print(f"  {name} ({formula}): {calculate_mw(formula)} g/mol")
print()


# -----------------------------------------------------------------------------
# Problem 8: SMILES String Analyzer (5 points)
# -----------------------------------------------------------------------------
def count_atoms(smiles):
    """Count heavy atoms (C, N, O, S) in SMILES (simplified)."""
    # Count uppercase letters (atoms)
    c_count = smiles.count('C') + smiles.count('c')
    n_count = smiles.count('N') + smiles.count('n')
    o_count = smiles.count('O') + smiles.count('o')
    s_count = smiles.count('S') + smiles.count('s')
    
    return {"C": c_count, "N": n_count, "O": o_count, "S": s_count}


def has_ring(smiles):
    """Check if molecule has a ring (contains digits)."""
    return bool(re.search(r'\d', smiles))


def count_double_bonds(smiles):
    """Count double bonds (= occurrences)."""
    return smiles.count('=')


def is_aromatic(smiles):
    """Check for aromatic atoms (lowercase letters c, n, o, s)."""
    return bool(re.search(r'[cnos]', smiles))


# Test Problem 8
smiles_list = [
    ("Ethanol", "CCO"),
    ("Acetic acid", "CC(=O)O"),
    ("Benzene", "c1ccccc1"),
    ("Aspirin", "CC(=O)Oc1ccccc1C(=O)O")
]
print("Problem 8: SMILES String Analyzer")
for name, smiles in smiles_list:
    print(f"  {name} ({smiles}):")
    print(f"    Atoms: {count_atoms(smiles)}")
    print(f"    Has ring: {has_ring(smiles)}")
    print(f"    Double bonds: {count_double_bonds(smiles)}")
    print(f"    Is aromatic: {is_aromatic(smiles)}")
print()


# -----------------------------------------------------------------------------
# Problem 9: Drug-likeness Calculator (5 points)
# -----------------------------------------------------------------------------
def check_lipinski(properties):
    """
    Check Lipinski's Rule of Five.
    
    Args:
        properties: Dict with MW, LogP, HBD, HBA
        
    Returns:
        Number of violations
    """
    violations = 0
    
    if properties.get("MW", 0) > 500:
        violations += 1
    if properties.get("LogP", 0) > 5:
        violations += 1
    if properties.get("HBD", 0) > 5:
        violations += 1
    if properties.get("HBA", 0) > 10:
        violations += 1
    
    return violations


def classify_drugs(drugs_dict):
    """
    Classify drugs as drug-like or not.
    
    Args:
        drugs_dict: Dict of {drug_name: properties}
        
    Returns:
        Dict of {drug_name: classification}
    """
    results = {}
    for drug, props in drugs_dict.items():
        violations = check_lipinski(props)
        results[drug] = "Drug-like" if violations <= 1 else "Not Drug-like"
    return results


# Test Problem 9
drugs = {
    "Aspirin": {"MW": 180.16, "LogP": 1.19, "HBD": 1, "HBA": 4},
    "Ibuprofen": {"MW": 206.29, "LogP": 3.97, "HBD": 1, "HBA": 2},
    "Metformin": {"MW": 129.16, "LogP": -1.43, "HBD": 3, "HBA": 5},
    "Atorvastatin": {"MW": 558.64, "LogP": 6.36, "HBD": 4, "HBA": 7}
}
print("Problem 9: Lipinski's Rule of Five")
for drug, props in drugs.items():
    violations = check_lipinski(props)
    print(f"  {drug}: {violations} violation(s)")
print(f"Classification: {classify_drugs(drugs)}")
print()


# -----------------------------------------------------------------------------
# Problem 10: IC50 to pIC50 Converter (5 points)
# -----------------------------------------------------------------------------
def ic50_to_pic50(ic50_nm):
    """
    Convert IC50 (nM) to pIC50.
    
    pIC50 = -log10(IC50 in M) = 9 - log10(IC50 in nM)
    """
    if ic50_nm <= 0:
        raise ValueError("IC50 must be positive")
    return 9 - math.log10(ic50_nm)


def classify_potency(pic50):
    """Classify compound potency based on pIC50."""
    if pic50 >= 8:
        return "Highly Active"
    elif pic50 >= 6:
        return "Active"
    elif pic50 >= 5:
        return "Moderately Active"
    else:
        return "Inactive"


def analyze_series(ic50_list):
    """Calculate statistics for a series of IC50 values."""
    pic50_values = [ic50_to_pic50(ic50) for ic50 in ic50_list]
    
    return {
        "min_pIC50": round(min(pic50_values), 2),
        "max_pIC50": round(max(pic50_values), 2),
        "mean_pIC50": round(sum(pic50_values) / len(pic50_values), 2)
    }


# Test Problem 10
ic50_values = [0.5, 1.0, 10.0, 100.0, 1000.0, 5000.0]
print("Problem 10: IC50 to pIC50 Converter")
for ic50 in ic50_values:
    pic50 = ic50_to_pic50(ic50)
    print(f"  IC50={ic50} nM -> pIC50={pic50:.2f} ({classify_potency(pic50)})")
print(f"Series analysis: {analyze_series(ic50_values)}")
print()


# =============================================================================
# PART 3: ADVANCED SEQUENCE ANALYSIS (25 points)
# =============================================================================

# -----------------------------------------------------------------------------
# Problem 11: Finding Motifs in DNA (5 points)
# Rosalind ID: SUBS
# -----------------------------------------------------------------------------
def find_motif(dna, motif):
    """
    Find all starting positions of motif in DNA (1-indexed).
    Handles overlapping matches.
    """
    dna = dna.upper()
    motif = motif.upper()
    
    positions = []
    start = 0
    
    while True:
        pos = dna.find(motif, start)
        if pos == -1:
            break
        positions.append(pos + 1)  # 1-indexed
        start = pos + 1  # Allow overlapping
    
    return positions


# Test Problem 11
dna = "GATATATGCATATACTT"
motif = "ATAT"
print("Problem 11: Finding Motifs")
print(f"DNA: {dna}")
print(f"Motif: {motif}")
print(f"Positions: {find_motif(dna, motif)}")
# Expected: [2, 4, 10]
print()


# -----------------------------------------------------------------------------
# Problem 12: Hamming Distance (5 points)
# Rosalind ID: HAMM
# -----------------------------------------------------------------------------
def hamming_distance(s1, s2):
    """
    Count point mutations between two sequences.
    """
    if len(s1) != len(s2):
        raise ValueError("Sequences must have equal length")
    
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def similarity_percentage(s1, s2):
    """Calculate percentage similarity between sequences."""
    if len(s1) != len(s2):
        raise ValueError("Sequences must have equal length")
    
    matches = sum(c1 == c2 for c1, c2 in zip(s1, s2))
    return round((matches / len(s1)) * 100, 2)


# Test Problem 12
s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"
print("Problem 12: Hamming Distance")
print(f"S1: {s1}")
print(f"S2: {s2}")
print(f"Hamming Distance: {hamming_distance(s1, s2)}")
print(f"Similarity: {similarity_percentage(s1, s2)}%")
# Expected: 7
print()


# -----------------------------------------------------------------------------
# Problem 13: FASTA File Parser (5 points)
# Rosalind ID: GC
# -----------------------------------------------------------------------------
def parse_fasta(fasta_string):
    """
    Parse FASTA format string into dictionary.
    
    Args:
        fasta_string: Multi-line FASTA formatted string
        
    Returns:
        Dict of {sequence_id: sequence}
    """
    sequences = {}
    current_id = None
    current_seq = []
    
    for line in fasta_string.strip().split('\n'):
        line = line.strip()
        if line.startswith('>'):
            # Save previous sequence
            if current_id is not None:
                sequences[current_id] = ''.join(current_seq)
            # Start new sequence
            current_id = line[1:].split()[0]  # Get ID (first word after >)
            current_seq = []
        else:
            current_seq.append(line)
    
    # Save last sequence
    if current_id is not None:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences


# Test Problem 13
fasta_string = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC"""

print("Problem 13: FASTA Parser")
parsed = parse_fasta(fasta_string)
for seq_id, seq in parsed.items():
    print(f"  {seq_id}: {seq[:30]}... (len={len(seq)})")
print()


# -----------------------------------------------------------------------------
# Problem 14: Protein Mass Calculator (5 points)
# Rosalind ID: PRTM
# -----------------------------------------------------------------------------
AA_MASS = {
    "A": 71.04, "R": 156.10, "N": 114.04, "D": 115.03, "C": 103.01,
    "E": 129.04, "Q": 128.06, "G": 57.02, "H": 137.06, "I": 113.08,
    "L": 113.08, "K": 128.09, "M": 131.04, "F": 147.07, "P": 97.05,
    "S": 87.03, "T": 101.05, "W": 186.08, "Y": 163.06, "V": 99.07
}


def protein_mass(sequence):
    """
    Calculate protein mass from amino acid sequence.
    
    Args:
        sequence: Amino acid sequence string
        
    Returns:
        Mass in Daltons (rounded to 3 decimal places)
    """
    sequence = sequence.upper()
    mass = 0
    
    for aa in sequence:
        if aa not in AA_MASS:
            raise ValueError(f"Invalid amino acid: {aa}")
        mass += AA_MASS[aa]
    
    return round(mass, 3)


# Test Problem 14
protein_seq = "SKADYEK"
print("Problem 14: Protein Mass")
print(f"Sequence: {protein_seq}")
print(f"Mass: {protein_mass(protein_seq)} Da")
# Expected: 821.392 Da
print()


# -----------------------------------------------------------------------------
# Problem 15: Consensus and Profile (5 points)
# Rosalind ID: CONS
# -----------------------------------------------------------------------------
def build_profile(sequences):
    """
    Build a profile matrix from multiple aligned sequences.
    
    Returns:
        Dict of {nucleotide: [counts at each position]}
    """
    seq_len = len(sequences[0])
    
    profile = {
        "A": [0] * seq_len,
        "C": [0] * seq_len,
        "G": [0] * seq_len,
        "T": [0] * seq_len
    }
    
    for seq in sequences:
        for i, nuc in enumerate(seq.upper()):
            if nuc in profile:
                profile[nuc][i] += 1
    
    return profile


def consensus_sequence(profile):
    """
    Generate consensus sequence from profile matrix.
    Breaks ties alphabetically.
    """
    seq_len = len(profile["A"])
    consensus = []
    
    for i in range(seq_len):
        max_count = -1
        max_nuc = "A"
        
        for nuc in sorted(profile.keys()):  # Alphabetical order for ties
            if profile[nuc][i] > max_count:
                max_count = profile[nuc][i]
                max_nuc = nuc
        
        consensus.append(max_nuc)
    
    return "".join(consensus)


# Test Problem 15
sequences_list = [
    "ATCCAGCT",
    "GGGCAACT",
    "ATGGATCT",
    "AAGCAACC",
    "TTGGAACT",
    "ATGCCATT",
    "ATGGCACT"
]
print("Problem 15: Consensus and Profile")
profile = build_profile(sequences_list)
consensus = consensus_sequence(profile)
print(f"Consensus: {consensus}")
print("Profile Matrix:")
for nuc in ["A", "C", "G", "T"]:
    print(f"  {nuc}: {profile[nuc]}")
print()


# =============================================================================
# PART 4: SCIENTIFIC DATA ANALYSIS (25 points)
# =============================================================================

# -----------------------------------------------------------------------------
# Problem 16: Bioactivity Data Processing (5 points)
# -----------------------------------------------------------------------------
def process_bioactivity(data):
    """Process bioactivity dataset."""
    # Add pIC50 values
    for entry in data:
        entry["pIC50"] = round(ic50_to_pic50(entry["IC50_nM"]), 2)
    
    return data


def filter_by_target(data, target):
    """Filter compounds by target."""
    return [entry for entry in data if entry["target"] == target]


def most_potent_per_target(data):
    """Find most potent compound for each target."""
    targets = set(entry["target"] for entry in data)
    results = {}
    
    for target in targets:
        target_compounds = filter_by_target(data, target)
        most_potent = max(target_compounds, key=lambda x: x["pIC50"])
        results[target] = most_potent["compound"]
    
    return results


def avg_pic50_per_target(data):
    """Calculate average pIC50 per target."""
    targets = set(entry["target"] for entry in data)
    results = {}
    
    for target in targets:
        target_compounds = filter_by_target(data, target)
        avg = sum(c["pIC50"] for c in target_compounds) / len(target_compounds)
        results[target] = round(avg, 2)
    
    return results


# Test Problem 16
bioactivity_data = [
    {"compound": "CPD001", "target": "EGFR", "IC50_nM": 5.2, "MW": 423.5},
    {"compound": "CPD002", "target": "EGFR", "IC50_nM": 120.0, "MW": 389.2},
    {"compound": "CPD003", "target": "VEGFR", "IC50_nM": 8.7, "MW": 512.3},
    {"compound": "CPD004", "target": "EGFR", "IC50_nM": 2.1, "MW": 445.6},
    {"compound": "CPD005", "target": "VEGFR", "IC50_nM": 450.0, "MW": 378.9},
]

print("Problem 16: Bioactivity Data Processing")
processed = process_bioactivity(bioactivity_data)
for entry in processed:
    print(f"  {entry['compound']}: pIC50={entry['pIC50']}")
print(f"Most potent per target: {most_potent_per_target(processed)}")
print(f"Avg pIC50 per target: {avg_pic50_per_target(processed)}")
print()


# -----------------------------------------------------------------------------
# Problem 17: Sequence Statistics with NumPy (5 points)
# -----------------------------------------------------------------------------
def encode_sequences(sequences):
    """Convert DNA sequences to numerical encoding (A=0, C=1, G=2, T=3)."""
    encoding = {"A": 0, "C": 1, "G": 2, "T": 3}
    
    encoded = []
    for seq in sequences:
        encoded.append([encoding[nuc] for nuc in seq.upper()])
    
    return np.array(encoded)


def nucleotide_frequencies(encoded_array):
    """Calculate nucleotide frequencies per position."""
    n_sequences, seq_len = encoded_array.shape
    frequencies = np.zeros((4, seq_len))
    
    for pos in range(seq_len):
        for nuc in range(4):
            frequencies[nuc, pos] = np.sum(encoded_array[:, pos] == nuc) / n_sequences
    
    return frequencies


def position_variability(frequencies):
    """Find positions with highest variability (entropy)."""
    # Simple variability: 1 - max frequency (higher = more variable)
    variability = 1 - np.max(frequencies, axis=0)
    return variability


# Test Problem 17
sequences_np = ["ATGCGATCGATCG", "ATGCATGCATGCA", "GCGCGCGCGCGCG"]
print("Problem 17: Sequence Statistics with NumPy")
encoded = encode_sequences(sequences_np)
print(f"Encoded shape: {encoded.shape}")
freqs = nucleotide_frequencies(encoded)
print(f"Frequencies shape: {freqs.shape}")
var = position_variability(freqs)
print(f"Most variable position: {np.argmax(var) + 1} (variability={var.max():.2f})")
print()


# -----------------------------------------------------------------------------
# Problem 18: Compound Library Analysis with Pandas (5 points)
# -----------------------------------------------------------------------------
def analyze_compound_library():
    """Create and analyze compound library with Pandas."""
    compounds = pd.DataFrame({
        "ID": ["CPD001", "CPD002", "CPD003", "CPD004", "CPD005"],
        "MW": [423.5, 389.2, 512.3, 445.6, 378.9],
        "LogP": [3.2, 2.8, 4.5, 3.8, 2.1],
        "HBD": [2, 1, 3, 2, 1],
        "HBA": [5, 4, 6, 5, 3],
        "IC50_nM": [5.2, 120.0, 8.7, 2.1, 450.0]
    })
    
    # Add pIC50 column
    compounds["pIC50"] = compounds["IC50_nM"].apply(lambda x: round(9 - math.log10(x), 2))
    
    # Add Lipinski violations column
    def count_violations(row):
        violations = 0
        if row["MW"] > 500: violations += 1
        if row["LogP"] > 5: violations += 1
        if row["HBD"] > 5: violations += 1
        if row["HBA"] > 10: violations += 1
        return violations
    
    compounds["Lipinski_Violations"] = compounds.apply(count_violations, axis=1)
    
    # Filter drug-like compounds
    drug_like = compounds[compounds["Lipinski_Violations"] <= 1].copy()
    
    # Rank by potency
    drug_like = drug_like.sort_values("pIC50", ascending=False)
    
    return compounds, drug_like


# Test Problem 18
print("Problem 18: Compound Library Analysis")
all_compounds, drug_like = analyze_compound_library()
print("All compounds:")
print(all_compounds[["ID", "pIC50", "Lipinski_Violations"]])
print("\nDrug-like compounds (ranked by potency):")
print(drug_like[["ID", "pIC50", "Lipinski_Violations"]])
# drug_like.to_csv("drug_like_compounds.csv", index=False)
print()


# -----------------------------------------------------------------------------
# Problem 19: Dose-Response Analysis (5 points)
# -----------------------------------------------------------------------------
def estimate_ic50(doses, responses):
    """Estimate IC50 by linear interpolation."""
    # Find where response crosses 50%
    for i in range(len(responses) - 1):
        if responses[i] <= 50 <= responses[i+1]:
            # Linear interpolation
            slope = (responses[i+1] - responses[i]) / (math.log10(doses[i+1]) - math.log10(doses[i]))
            ic50_log = math.log10(doses[i]) + (50 - responses[i]) / slope
            return 10 ** ic50_log
    return None


def calculate_hill_slope(doses, responses):
    """Estimate Hill slope from dose-response data."""
    # Simplified: use points around IC50
    log_doses = [math.log10(d) for d in doses]
    
    # Find steepest part of curve (around 50%)
    max_slope = 0
    for i in range(len(responses) - 1):
        if 20 < responses[i] < 80 or 20 < responses[i+1] < 80:
            slope = (responses[i+1] - responses[i]) / (log_doses[i+1] - log_doses[i])
            if abs(slope) > abs(max_slope):
                max_slope = slope
    
    # Normalize to Hill slope (approximately)
    hill_slope = max_slope / 25  # Rough normalization
    return round(hill_slope, 2)


def classify_hill_slope(hill_slope):
    """Classify curve steepness."""
    if hill_slope > 1.5:
        return "Steep"
    elif hill_slope >= 0.8:
        return "Normal"
    else:
        return "Shallow"


# Test Problem 19
doses = [0.001, 0.01, 0.1, 1, 10, 100, 1000]  # uM
responses = [2, 5, 15, 45, 78, 95, 99]  # % inhibition

print("Problem 19: Dose-Response Analysis")
ic50 = estimate_ic50(doses, responses)
print(f"Estimated IC50: {ic50:.3f} uM" if ic50 else "IC50 not found")
hill = calculate_hill_slope(doses, responses)
print(f"Hill slope: {hill} ({classify_hill_slope(hill)})")
print()


# -----------------------------------------------------------------------------
# Problem 20: Molecular Descriptor Analysis (5 points)
# -----------------------------------------------------------------------------
def analyze_descriptors():
    """Analyze molecular descriptor correlations."""
    descriptors = pd.DataFrame({
        "MW": [423, 389, 512, 445, 378, 520, 410, 395],
        "LogP": [3.2, 2.8, 4.5, 3.8, 2.1, 5.1, 3.0, 2.5],
        "TPSA": [78, 65, 95, 82, 55, 102, 70, 60],
        "RotBonds": [5, 4, 8, 6, 3, 9, 5, 4],
        "pIC50": [8.3, 6.9, 8.1, 8.7, 6.3, 5.8, 7.5, 7.0]
    })
    
    # Calculate correlation matrix
    corr_matrix = descriptors.corr()
    
    # Find descriptor most correlated with pIC50
    pic50_corr = corr_matrix["pIC50"].drop("pIC50")
    best_predictor = pic50_corr.abs().idxmax()
    best_corr = pic50_corr[best_predictor]
    
    # Find highly correlated pairs (|r| > 0.7)
    high_corr_pairs = []
    cols = descriptors.columns.tolist()
    for i, col1 in enumerate(cols):
        for col2 in cols[i+1:]:
            corr = corr_matrix.loc[col1, col2]
            if abs(corr) > 0.7 and col1 != "pIC50" and col2 != "pIC50":
                high_corr_pairs.append((col1, col2, round(corr, 3)))
    
    # Simple linear regression for best predictor
    x = descriptors[best_predictor]
    y = descriptors["pIC50"]
    
    # Calculate slope and intercept
    x_mean, y_mean = x.mean(), y.mean()
    slope = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean) ** 2)
    intercept = y_mean - slope * x_mean
    
    return {
        "correlation_matrix": corr_matrix,
        "best_predictor": best_predictor,
        "best_correlation": round(best_corr, 3),
        "high_corr_pairs": high_corr_pairs,
        "regression": {"slope": round(slope, 4), "intercept": round(intercept, 4)}
    }


# Test Problem 20
print("Problem 20: Molecular Descriptor Analysis")
results = analyze_descriptors()
print(f"Best predictor of pIC50: {results['best_predictor']} (r={results['best_correlation']})")
print(f"Highly correlated pairs: {results['high_corr_pairs']}")
print(f"Linear regression: pIC50 = {results['regression']['slope']} * {results['best_predictor']} + {results['regression']['intercept']}")
print()


# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 70)
print("HOMEWORK SOLUTIONS COMPLETE")
print("=" * 70)
print("Part 1: Bioinformatics (Problems 1-5) - DNA/RNA/Protein")
print("Part 2: Cheminformatics (Problems 6-10) - Molecules & Properties")
print("Part 3: Advanced Sequences (Problems 11-15) - Motifs & Analysis")
print("Part 4: Data Analysis (Problems 16-20) - NumPy & Pandas")
print("=" * 70)
