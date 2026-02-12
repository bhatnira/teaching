# Teaching Materials Repository

**AI-Driven Development Training**

A comprehensive collection of teaching materials for programming and technology courses.

## 📚 Available Modules

| Module | Status | Description |
|--------|--------|-------------|
| [01-python-foundation](./01-python-foundation/) | ✅ Complete | Python fundamentals for beginners |

*More modules coming soon*

## 🎯 Target Audience

- Entry-level to intermediate programmers
- Corporate training programs
- Self-paced learners
- Bootcamp students

## 📁 Repository Structure

```
teaching/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
│
└── 01-python-foundation/        # Module 1: Python Basics
    ├── README.md
    ├── lession-lab-1-AIDD-Training.tex   # Lecture slides
    ├── lab-solutions.tex                  # Lab solutions
    ├── homework-assignment.tex            # Homework problems
    ├── homework-solutions.py              # Homework solutions
    ├── quiz-questions-answers.tex         # Quiz with answers
    └── quiz-answer-key.py                 # Quiz answer key
```

## 🚀 Quick Start

### For Instructors

1. Clone the repository:
   ```bash
   git clone https://github.com/bhatnira/teaching.git
   ```

2. Navigate to the desired module:
   ```bash
   cd teaching/01-python-foundation
   ```

3. Compile LaTeX files to PDF:
   ```bash
   pdflatex lession-lab-1-AIDD-Training.tex
   ```

### For Students

1. Access the module materials
2. Follow the lecture slides
3. Complete lab exercises
4. Submit homework assignments
5. Review with quizzes

## 📊 Module 1: Python Foundation

**Duration:** 2-3 weeks  
**Prerequisites:** Basic computer literacy  
**Topics:**
- Variables, data types, operators
- Control flow (if/else, loops)
- Data structures (lists, tuples, sets, dictionaries)
- Functions and error handling
- File I/O, JSON, regex
- Introduction to NumPy & Pandas

**Assessments:**
- 13 Lab exercises
- 20 Homework problems (100 points)
- 50 Quiz questions (100 points)

## 🛠️ Requirements

### For LaTeX Compilation
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Required packages: beamer, listings, tikz, xcolor

### For Python Exercises
```bash
pip install numpy pandas
```

## 📝 Contributing

To add a new module:
1. Create a folder: `XX-module-name/`
2. Follow the structure of `01-python-foundation/`
3. Update this README

## 📄 License

MIT License - See [LICENSE](./LICENSE) for details.

## 👤 Author

**AI-Driven Development Training Team**

---

*Last updated: February 2026*
