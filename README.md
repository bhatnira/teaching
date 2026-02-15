# AI-Driven Drug Discovery (AIDD) Training

**Foundation of Python Programming for Cheminformatics & Bioinformatics**

Teaching materials for Python programming with a focus on drug discovery, cheminformatics, and bioinformatics applications.

## 📚 Course Module

| Module | Description |
|--------|-------------|
| [01-python-foundation](./01-python-foundation/) | Python fundamentals with cheminformatics & bioinformatics examples |

## 🎯 Target Audience

- Scientists entering computational drug discovery
- Biologists/Chemists learning programming
- Entry-level bioinformaticians/cheminformaticians
- Corporate AIDD training programs

## 📁 Repository Structure

```
teaching/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore rules
│
└── 01-python-foundation/              # Module 1: Python for AIDD
    ├── README.md                      # Module overview
    ├── build-pdfs.sh                  # Auto-compile all LaTeX → PDF
    │
    ├── lessons-AIDD-Training.tex      # Lecture slides (theory)
    ├── lessons-AIDD-Training.pdf      # Compiled lectures
    │
    ├── labs-AIDD-Training.tex         # Hands-on lab exercises
    ├── labs-AIDD-Training.pdf         # Compiled labs
    ├── lab-solutions.tex              # Lab solutions
    ├── lab-solutions.pdf              # Compiled solutions
    │
    ├── homework-assignment.tex        # 20 homework problems
    ├── homework-assignment.pdf        # Compiled homework
    ├── homework-solutions.py          # Complete Python solutions
    │
    ├── quiz-questions-answers.tex     # 50 quiz questions with answers
    ├── quiz-questions-answers.pdf     # Compiled quiz
    └── quiz-answer-key.py             # Quick reference answer key
```

## 🧬 Course Topics

**13 Lessons covering:**
- Python basics (variables, operators, strings)
- Control flow with drug discovery examples (pIC50 classification, potency)
- Data structures for molecular data (SMILES lists, compound dictionaries)
- Functions for cheminformatics workflows
- File I/O for molecular files (FASTA, SDF, CSV)
- Introduction to NumPy & Pandas for data analysis

**Special Topics:**
- Drug discovery data types (SMILES, activity data, sequences)
- Molecular representations (SMARTS, SELFIES, InChI, Fingerprints)
- Central Dogma of Molecular Biology
- Rosalind bioinformatics problems

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/bhatnira/teaching.git
cd teaching/01-python-foundation

# Build all PDFs (requires LaTeX)
./build-pdfs.sh

# Or compile individual files
pdflatex lessons-AIDD-Training.tex
```

## 📊 Assessments

| Type | Count | Points |
|------|-------|--------|
| Lab Exercises | 13 | Practice |
| Homework Problems | 20 | 100 pts |
| Quiz Questions | 50 | 100 pts |

## 🛠️ Requirements

**LaTeX Compilation:**
- BasicTeX, TeX Live, or MacTeX
- Packages: beamer, listings, tikz, xcolor, enumitem

**Python Exercises:**
```bash
pip install numpy pandas
```

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details.

---

*AI-Driven Development Training | February 2026*
