"""
============================================================================
QUIZ ANSWER KEY - Python for Cheminformatics & Bioinformatics
============================================================================
AI-Driven Drug Development Training
February 2026

This file provides a quick reference answer key for all 50 quiz questions
with detailed explanations/rationale for each answer.

All questions use cheminformatics and bioinformatics contexts:
- SMILES strings and molecular properties
- IC50/pIC50 conversions
- DNA/RNA sequence manipulation
- Lipinski Rule of Five
- Compound library management
- FASTA file handling

Format: Question Number | Answer | Topic | Rationale
============================================================================
"""

import math

# =============================================================================
# ANSWER KEY - Quick Reference Table
# =============================================================================

ANSWER_KEY = {
    # Section 1: Variables & Data Types (Q1-Q5)
    1:  {"answer": "B", "topic": "Data Types - Compound Storage", 
         "rationale": "mw is float, pic50 stored as str. type(float) != type(str), so False. Always store numeric data as numbers in QSAR."},
    
    2:  {"answer": "C", "topic": "Tuple Unpacking - Molecular Data", 
         "rationale": "Tuple unpacking assigns in order: name='Ibuprofen', mw=206.28, logp=3.97. logp is 3.97."},
    
    3:  {"answer": "B", "topic": "Falsy Values - Drug Data", 
         "rationale": "None, 0, '' are all falsy. These often indicate missing measurements in drug discovery data."},
    
    4:  {"answer": "A", "topic": "Type Conversion - IC50", 
         "rationale": "int() truncates toward zero. int(5.8)=5, int(-2.3)=-2. Sum: 5+(-2)=3."},
    
    5:  {"answer": "D", "topic": "Multi-line Strings - Sequences", 
         "rationale": "All methods work: \\n escape, triple quotes. Useful for FASTA sequences and long SMILES."},
    
    # Section 2: Operators (Q6-Q10)
    6:  {"answer": "A", "topic": "Division - Atom Counting", 
         "rationale": "// floor division (3), % modulo (2), / true division (3.4). Useful for codon counting."},
    
    7:  {"answer": "A", "topic": "Logical Operators - Lipinski", 
         "rationale": "Both MW<=500 and LogP<=5 are True. True and True = True. Used for Rule of Five."},
    
    8:  {"answer": "B", "topic": "Exponentiation - pIC50", 
         "rationale": "10**(9-8) = 10**1 = 10. Formula for IC50_nM from pIC50."},
    
    9:  {"answer": "A", "topic": "GC Content Calculation", 
         "rationale": "ATGCGC has 4 G/C out of 6. (4/6)*100 = 66.67%. Important for primer design."},
    
    10: {"answer": "B", "topic": "Identity vs Equality - SMILES", 
         "rationale": "== compares values (equal), 'is' compares identity (different list objects)."},
    
    # Section 3: Strings - DNA/SMILES (Q11-Q15)
    11: {"answer": "A", "topic": "DNA Slicing - Codons", 
         "rationale": "[:3]='ATG' (start codon), [-3:]='TCG', [::3]='AGC'. Essential for codon extraction."},
    
    12: {"answer": "A", "topic": "DNA Transcription", 
         "rationale": "replace('T','U') converts DNA to RNA. ATGC -> AUGC."},
    
    13: {"answer": "A", "topic": "SMILES Ring Detection", 
         "rationale": "Digits in SMILES indicate ring closure. 'c1ccccc1' has '1', so has_ring=True."},
    
    14: {"answer": "B", "topic": "F-strings - Compound Data", 
         "rationale": ":.1f rounds to 1 decimal. 5.28 -> 5.3. Useful for formatted reports."},
    
    15: {"answer": "A", "topic": "String Immutability - Sequences", 
         "rationale": "Strings cannot be modified in place. TypeError raised. Create new string for 'mutations'."},
    
    # Section 4: Lists (Q16-Q20)
    16: {"answer": "B", "topic": "List References - Libraries", 
         "rationale": "library_b = library_a creates reference. Modifying one affects both. Use .copy() for independence."},
    
    17: {"answer": "C", "topic": "extend() vs append()", 
         "rationale": "extend() adds elements individually: 2 + 2 = 4 elements total."},
    
    18: {"answer": "B", "topic": "List Comprehension - Filtering", 
         "rationale": "Filter pIC50 >= 6.0: [6.8, 7.3, 8.1]. 3 active compounds pass threshold."},
    
    19: {"answer": "C", "topic": "Nested Lists - Descriptors", 
         "rationale": "descriptors[1] = Ibuprofen row, [1] = LogP = 3.97."},
    
    20: {"answer": "B", "topic": "Sorting - Potency Ranking", 
         "rationale": "Sort by pIC50 descending puts Drug_X (8.1) first. Most potent compound."},
    
    # Section 5: Tuples & Sets (Q21-Q25)
    21: {"answer": "A", "topic": "Tuple Immutability", 
         "rationale": "Tuples cannot be modified. TypeError raised. Use for fixed compound records."},
    
    22: {"answer": "B", "topic": "Extended Unpacking", 
         "rationale": "*middle captures [2,3,4,5,6] = 5 elements. Useful for variable-length records."},
    
    23: {"answer": "C", "topic": "Set Intersection - Common Compounds", 
         "rationale": "& finds common elements: {CMP002, CMP003}. Useful for library comparison."},
    
    24: {"answer": "B", "topic": "Set Uniqueness - Scaffolds", 
         "rationale": "Sets remove duplicates. Only 3 unique scaffolds remain."},
    
    25: {"answer": "B", "topic": "Set Difference - Untested", 
         "rationale": "all - tested = {A, C}. Useful for tracking untested compounds."},
    
    # Section 6: Dictionaries (Q26-Q30)
    26: {"answer": "B", "topic": "dict.get() - Missing Properties", 
         "rationale": "get(key, default) returns 'N/A' if LogP missing. Avoids KeyError."},
    
    27: {"answer": "B", "topic": "Dict Iteration - Properties", 
         "rationale": "Iterating over dict yields keys only: MW, LogP, HBD."},
    
    28: {"answer": "B", "topic": "Nested Dict - Compound DB", 
         "rationale": "compounds['Aspirin']['pIC50'] = 5.2. Common pattern for compound databases."},
    
    29: {"answer": "B", "topic": "Dict Comprehension - IC50 Conversion", 
         "rationale": "pIC50 = 9 - log10(10) = 8.0. Efficient batch conversion."},
    
    30: {"answer": "A", "topic": "Codon Table Lookup", 
         "rationale": "AUG->M, UGG->W. Protein = 'MW'. Used for translation."},
    
    # Section 7: Control Flow (Q31-Q35)
    31: {"answer": "B", "topic": "Activity Classification", 
         "rationale": "pIC50 7.5 < 8 (not highly active) but >= 6 (active)."},
    
    32: {"answer": "A", "topic": "Range Loop - Processing", 
         "rationale": "range(0,10,2) = [0,2,4,6,8]. Sum = 20."},
    
    33: {"answer": "B", "topic": "Break - First Potent", 
         "rationale": "break exits at first pIC50 >= 7.0. Prints 7.5, not 8.1."},
    
    34: {"answer": "B", "topic": "Continue - Skip Invalid", 
         "rationale": "continue skips None and ''. Prints: valid active potent."},
    
    35: {"answer": "A", "topic": "Loop Else - No Actives", 
         "rationale": "else executes when no break. All values < 6.0, so 'No actives found'."},
    
    # Section 8: Functions (Q36-Q40)
    36: {"answer": "B", "topic": "Default Parameters - Activity", 
         "rationale": "threshold defaults to 6.0. pIC50 5.5 < 6.0, returns 'Inactive'."},
    
    37: {"answer": "A", "topic": "Return Values - Validation", 
         "rationale": "Empty string is falsy, returns early (None). No print executed."},
    
    38: {"answer": "B", "topic": "*args - Average pIC50", 
         "rationale": "*args collects into tuple. (5.2+6.8+7.3)/3 = 6.43."},
    
    39: {"answer": "B", "topic": "**kwargs - Properties", 
         "rationale": "**kwargs collects keyword args into dict. Type is dict."},
    
    40: {"answer": "A", "topic": "Lambda - IC50 to pIC50", 
         "rationale": "9 - log10(100) = 9 - 2 = 7.0."},
    
    # Section 9: File & Error Handling (Q41-Q45)
    41: {"answer": "A", "topic": "Context Manager - FASTA", 
         "rationale": "'with' automatically closes file after block. Ensures cleanup."},
    
    42: {"answer": "B", "topic": "File Modes - CSV", 
         "rationale": "'r' is read-only. Writing raises UnsupportedOperation."},
    
    43: {"answer": "C", "topic": "Try/Except - Invalid SMILES", 
         "rationale": "ValueError caught, 'Error' printed, then continues to 'Done'."},
    
    44: {"answer": "C", "topic": "Finally - Cleanup", 
         "rationale": "finally always executes, even after return. Prints 'Cleanup' first."},
    
    45: {"answer": "A", "topic": "Specific Exceptions - IC50", 
         "rationale": "float('invalid') raises ValueError, not TypeError."},
    
    # Section 10: Advanced Topics (Q46-Q50)
    46: {"answer": "B", "topic": "Generators - Memory", 
         "rationale": "Generators use lazy evaluation. Much less memory for large libraries."},
    
    47: {"answer": "A", "topic": "Map - Batch Conversion", 
         "rationale": "map applies conversion to all. [8.0, 7.0, 6.0]."},
    
    48: {"answer": "C", "topic": "Filter - Potent Compounds", 
         "rationale": "filter keeps pIC50 >= 7.0: [7.3, 8.1]."},
    
    49: {"answer": "C", "topic": "Zip - Compound Pairing", 
         "rationale": "zip pairs elements into tuples: ('Aspirin', 5.2)."},
    
    50: {"answer": "B", "topic": "Enumerate - Indexing", 
         "rationale": "start=1 begins count at 1. Output: '1: CCO'."},
}


# =============================================================================
# SECTION EXPLANATIONS - Cheminformatics & Bioinformatics Context
# =============================================================================

SECTION_EXPLANATIONS = """
============================================================================
SECTION 1: VARIABLES & DATA TYPES (Questions 1-5)
============================================================================

Key Concepts for Drug Discovery:
- Store molecular properties correctly (MW as float, not string)
- Tuple unpacking for compound data (name, SMILES, properties)
- Handle missing data (None, 0, empty strings are falsy)
- Type conversion for IC50/pIC50 values
- Multi-line strings for FASTA sequences

Common Mistakes:
- Storing numeric properties as strings (breaks calculations)
- Not handling None values in bioactivity data
- Confusing int() truncation with floor()


============================================================================
SECTION 2: OPERATORS (Questions 6-10)
============================================================================

Key Concepts for Molecular Calculations:
- Floor division for codon counting (// gives integer)
- Modulo for sequence position calculations
- Logical operators for Lipinski Rule checking
- Exponentiation for IC50/pIC50 conversion
- GC content = (G+C)/total * 100

Common Formulas:
- pIC50 = 9 - log10(IC50_nM)
- IC50_nM = 10**(9 - pIC50)
- GC% = (count_G + count_C) / length * 100


============================================================================
SECTION 3: STRINGS - DNA/SMILES (Questions 11-15)
============================================================================

Key Concepts for Sequences:
- Slicing for codon extraction: seq[:3], seq[3:6], etc.
- Transcription: DNA -> RNA via replace('T', 'U')
- SMILES ring detection: digits indicate ring closure
- F-strings for formatted property reports
- Strings are immutable (simulate mutations via new strings)

Bioinformatics Patterns:
- Extract codons: [seq[i:i+3] for i in range(0, len(seq), 3)]
- Reverse complement: complement + reverse
- Count nucleotides: seq.count('A'), etc.


============================================================================
SECTION 4: LISTS (Questions 16-20)
============================================================================

Key Concepts for Compound Libraries:
- List references vs copies (use .copy() for independence)
- extend() adds elements, append() adds as single item
- List comprehension for filtering active compounds
- Nested lists for descriptor matrices
- Sort by property (key=lambda) for potency ranking

QSAR Patterns:
- Filter actives: [c for c in compounds if c['pIC50'] >= 6.0]
- Rank by potency: compounds.sort(key=lambda x: x['pIC50'], reverse=True)


============================================================================
SECTION 5: TUPLES & SETS (Questions 21-25)
============================================================================

Key Concepts:
- Tuples for immutable compound records
- Extended unpacking for variable-length data
- Set intersection for finding common compounds
- Set uniqueness for counting scaffolds
- Set difference for tracking untested compounds

Library Analysis Patterns:
- Common hits: library_a & library_b
- Unique to A: library_a - library_b
- All unique: library_a | library_b


============================================================================
SECTION 6: DICTIONARIES (Questions 26-30)
============================================================================

Key Concepts for Compound Databases:
- get(key, default) handles missing properties
- Iterate keys, values, or items
- Nested dicts for compound records
- Dict comprehension for batch transformations
- Codon tables for translation

Database Patterns:
- compounds['Aspirin']['pIC50']
- {name: props for name, props in data.items() if props['pIC50'] >= 6}


============================================================================
SECTION 7: CONTROL FLOW (Questions 31-35)
============================================================================

Key Concepts for Data Processing:
- if/elif/else for activity classification
- range() with step for batch processing
- break to find first match (first potent compound)
- continue to skip invalid data
- for-else to detect "not found" conditions

Activity Classification:
- pIC50 >= 8: Highly Active
- pIC50 >= 6: Active  
- pIC50 < 6: Inactive


============================================================================
SECTION 8: FUNCTIONS (Questions 36-40)
============================================================================

Key Concepts for Molecular Utilities:
- Default parameters for flexible thresholds
- Return None for invalid inputs
- *args for variable number of compounds
- **kwargs for flexible property containers
- Lambda for simple conversions

Utility Function Examples:
- ic50_to_pic50(ic50_nm)
- check_lipinski(mw, logp, hbd, hba)
- gc_content(sequence)


============================================================================
SECTION 9: FILE & ERROR HANDLING (Questions 41-45)
============================================================================

Key Concepts for Data Files:
- 'with' statement for automatic file closing
- File modes: 'r' read, 'w' write, 'a' append
- try/except for handling invalid SMILES
- finally for cleanup (database connections)
- Specific exceptions for clear error messages

File Formats:
- FASTA: >header\\nSEQUENCE
- CSV: name,smiles,pic50
- SDF: structured molecule files


============================================================================
SECTION 10: ADVANCED TOPICS (Questions 46-50)
============================================================================

Key Concepts for Large-Scale Analysis:
- Generators for memory-efficient processing
- map() for batch property calculation
- filter() for compound selection
- zip() for pairing names with properties
- enumerate() for indexed processing

Performance Patterns:
- Use generators for large libraries
- Vectorize with NumPy for speed
- Use Pandas for tabular data
"""


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def print_answer(question_num):
    """Print answer and rationale for a specific question."""
    if question_num in ANSWER_KEY:
        q = ANSWER_KEY[question_num]
        print(f"\nQuestion {question_num}:")
        print(f"  Answer: {q['answer']}")
        print(f"  Topic: {q['topic']}")
        print(f"  Rationale: {q['rationale']}")
    else:
        print(f"Question {question_num} not found.")


def print_all_answers():
    """Print all answers in a summary table."""
    print("\n" + "=" * 80)
    print("QUIZ ANSWER KEY - Python for Cheminformatics & Bioinformatics")
    print("=" * 80)
    print(f"{'Q#':<4} {'Ans':<4} {'Topic':<35} {'Rationale':<35}")
    print("-" * 80)
    
    for q_num in sorted(ANSWER_KEY.keys()):
        q = ANSWER_KEY[q_num]
        topic = q['topic'][:32] + "..." if len(q['topic']) > 35 else q['topic']
        rationale = q['rationale'][:32] + "..." if len(q['rationale']) > 35 else q['rationale']
        print(f"{q_num:<4} {q['answer']:<4} {topic:<35} {rationale}")


def print_answers_by_section():
    """Print answers grouped by section."""
    sections = {
        "Variables & Data Types (Compound Storage)": range(1, 6),
        "Operators (Molecular Calculations)": range(6, 11),
        "Strings (DNA/SMILES)": range(11, 16),
        "Lists (Compound Libraries)": range(16, 21),
        "Tuples & Sets (Molecular Data)": range(21, 26),
        "Dictionaries (Compound Databases)": range(26, 31),
        "Control Flow (Data Processing)": range(31, 36),
        "Functions (Molecular Utilities)": range(36, 41),
        "File & Error Handling": range(41, 46),
        "Advanced Topics (Large-Scale Analysis)": range(46, 51),
    }
    
    for section, q_range in sections.items():
        print(f"\n{'='*60}")
        print(f"  {section}")
        print(f"{'='*60}")
        for q_num in q_range:
            if q_num in ANSWER_KEY:
                q = ANSWER_KEY[q_num]
                print(f"  Q{q_num}: {q['answer']} - {q['rationale'][:55]}...")


def get_answers_only():
    """Return just the answers as a simple dict."""
    return {q: data['answer'] for q, data in ANSWER_KEY.items()}


def check_answer(question_num, user_answer):
    """Check if user's answer is correct."""
    if question_num not in ANSWER_KEY:
        return None, "Question not found"
    
    correct = ANSWER_KEY[question_num]['answer']
    is_correct = user_answer.upper() == correct
    
    if is_correct:
        return True, "Correct!"
    else:
        return False, f"Incorrect. The answer is {correct}. {ANSWER_KEY[question_num]['rationale']}"


def demo_questions():
    """Demonstrate key cheminformatics calculations from the quiz."""
    print("\n" + "=" * 60)
    print("DEMO: Key Cheminformatics Calculations")
    print("=" * 60)
    
    # IC50 to pIC50 conversion
    print("\n1. IC50 to pIC50 Conversion:")
    ic50_values = [10, 100, 1000]  # nM
    for ic50 in ic50_values:
        pic50 = 9 - math.log10(ic50)
        print(f"   IC50 = {ic50} nM -> pIC50 = {pic50:.1f}")
    
    # GC Content
    print("\n2. GC Content Calculation:")
    seq = "ATGCGC"
    gc_count = seq.count("G") + seq.count("C")
    gc_percent = gc_count / len(seq) * 100
    print(f"   Sequence: {seq}")
    print(f"   GC Content: {gc_percent:.1f}%")
    
    # Lipinski Rule Check
    print("\n3. Lipinski Rule of Five:")
    compound = {"MW": 450, "LogP": 4.5, "HBD": 2, "HBA": 8}
    violations = 0
    violations += 1 if compound["MW"] > 500 else 0
    violations += 1 if compound["LogP"] > 5 else 0
    violations += 1 if compound["HBD"] > 5 else 0
    violations += 1 if compound["HBA"] > 10 else 0
    print(f"   MW={compound['MW']}, LogP={compound['LogP']}, HBD={compound['HBD']}, HBA={compound['HBA']}")
    print(f"   Violations: {violations} -> {'Drug-like' if violations <= 1 else 'Not drug-like'}")
    
    # DNA Transcription
    print("\n4. DNA Transcription:")
    dna = "ATGCGATCG"
    rna = dna.replace("T", "U")
    print(f"   DNA: {dna}")
    print(f"   RNA: {rna}")


# =============================================================================
# MAIN - Display Answer Key
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("   QUIZ ANSWER KEY - Python for Cheminformatics & Bioinformatics")
    print("   50 Questions with Answers and Rationale")
    print("   AI-Driven Drug Development Training")
    print("=" * 80)
    
    # Print quick reference
    print_all_answers()
    
    # Print by section
    print("\n\n")
    print_answers_by_section()
    
    # Demo calculations
    demo_questions()
    
    # Print section explanations
    print(SECTION_EXPLANATIONS)
    
    print("\n" + "=" * 80)
    print("   END OF ANSWER KEY")
    print("=" * 80)
