
# Module 01: Python Foundation for AIDD

**AI-Driven Drug Discovery Training**  
**February 2026**

## Overview

Python fundamentals with a focus on **cheminformatics** and **bioinformatics** applications. Examples use molecular data (SMILES, sequences, activity values) and drug discovery workflows.

## 📚 Course Materials

| File | Description |
|------|-------------|
| `lessons-AIDD-Training.tex/pdf` | Lecture slides (13 lessons, theory) |
| `labs-AIDD-Training.tex/pdf` | Hands-on lab exercises |
| `lab-solutions.tex/pdf` | Lab exercise solutions |
| `homework-assignment.tex/pdf` | 20 homework problems (100 pts) |
| `homework-solutions.py` | Complete Python solutions |
| `quiz-questions-answers.tex/pdf` | 50 quiz questions with answers |
| `quiz-answer-key.py` | Quick reference answer key |
| `build-pdfs.sh` | Auto-compile all LaTeX → PDF |

## 🔬 Course Topics

### Lessons 1-3: Python Basics
- Variables, data types, operators
- Drug discovery data types (SMILES, pIC50, sequences)
- Molecular representations (SMARTS, SELFIES, InChI, Fingerprints)

### Lesson 4: Conditionals
- if/elif/else with potency classification
- Compound activity categorization

### Lesson 5: Loops
- for/while loops with molecular data
- Nucleotide counting, SMILES iteration

### Lessons 6-7: Strings
- String manipulation for sequences
- FASTA parsing basics

### Lessons 8-10: Data Structures
- Lists of compounds, tuples of coordinates
- Sets for unique molecules
- Dictionaries for compound databases

### Lessons 11-12: Functions
- Cheminformatics helper functions
- Lambda functions, list comprehensions

### Lesson 13: Advanced Topics
- File I/O (CSV, FASTA, SDF)
- JSON for compound data
- Regex for sequence patterns
- NumPy & Pandas introduction

## 🧬 Special Topics (Introductory Slides)

- Central Dogma of Molecular Biology
- Drug Discovery Data Types
- Molecular Representations comparison
- Rosalind bioinformatics problems
- Regular expressions
- Introduction to NumPy & Pandas

## 📊 Assessment Structure

| Assessment | Points | Count |
|------------|--------|-------|
| Lab Exercises | Practice | 13 labs |
| Homework | 100 pts | 20 problems |
| Quiz | 100 pts | 50 questions |

## 🚀 Quick Start

```bash
# Build all PDFs at once (auto-cleans aux files)
./build-pdfs.sh

# Or compile individual files
pdflatex lessons-AIDD-Training.tex
pdflatex labs-AIDD-Training.tex
```

## 🛠️ Requirements

**LaTeX:** BasicTeX, TeX Live, or MacTeX  
**Python:** `pip install numpy pandas`

---

*[Back to main repository](../README.md)*

**Next Module**: Plan 2 (Coming Soon)
