"""
============================================================================
QUIZ ANSWER KEY - Foundation of Python Programming
============================================================================
AI-Driven Development Training
February 2026

This file provides a quick reference answer key for all 50 quiz questions
with detailed explanations/rationale for each answer.

Format: Question Number | Answer | Topic | Rationale
============================================================================
"""

# =============================================================================
# ANSWER KEY - Quick Reference Table
# =============================================================================

ANSWER_KEY = {
    # Section 1: Variables & Data Types (Q1-Q5)
    1:  {"answer": "B", "topic": "Data Types", 
         "rationale": "x is int, y is str. type(int) != type(str), so comparison returns False."},
    
    2:  {"answer": "A", "topic": "Variable Assignment", 
         "rationale": "a,b = b,a swaps values. After swap: a=2, b=1. So print(b) outputs 1."},
    
    3:  {"answer": "B", "topic": "Falsy Values", 
         "rationale": "None, 0, '', [] are all 'falsy' in Python. bool() on any of them returns False."},
    
    4:  {"answer": "A", "topic": "Type Conversion", 
         "rationale": "int() truncates toward zero. int(3.9)=3, int(-3.9)=-3. Sum: 3+(-3)=0."},
    
    5:  {"answer": "D", "topic": "Multi-line Strings", 
         "rationale": "All methods work: \\n escape, triple quotes (''' or \"\"\"). All are valid."},
    
    # Section 2: Operators (Q6-Q10)
    6:  {"answer": "A", "topic": "Division Operators", 
         "rationale": "// is floor division (3), % is modulo (2), / is true division (3.4)."},
    
    7:  {"answer": "A", "topic": "Logical Operators", 
         "rationale": "'and' has higher precedence. (True and True) or False = True or False = True."},
    
    8:  {"answer": "B", "topic": "Exponentiation", 
         "rationale": "** is right-associative. 2**3**2 = 2**(3**2) = 2**9 = 512."},
    
    9:  {"answer": "A", "topic": "Boolean Logic", 
         "rationale": "not True = False, not False = True. Double negation returns original."},
    
    10: {"answer": "B", "topic": "Identity vs Equality", 
         "rationale": "== compares values (equal), 'is' compares identity (different objects)."},
    
    # Section 3: Strings (Q11-Q15)
    11: {"answer": "A", "topic": "String Slicing", 
         "rationale": "s[1:4]='yth', s[-3:]='hon', s[::2]='Pto' (every 2nd char)."},
    
    12: {"answer": "A", "topic": "String Operations", 
         "rationale": "'Hello'*2 = 'HelloHello', then + 'World' = 'HelloHelloWorld'."},
    
    13: {"answer": "B", "topic": "String Methods", 
         "rationale": "split() returns list of words. List has no strip() method, causes AttributeError."},
    
    14: {"answer": "C", "topic": "F-strings", 
         "rationale": "f-string evaluates {10+20} to 30. Result: 'Result: 30'."},
    
    15: {"answer": "A", "topic": "String Immutability", 
         "rationale": "Strings are immutable. s[0]='p' raises TypeError, cannot modify in place."},
    
    # Section 4: Lists (Q16-Q20)
    16: {"answer": "B", "topic": "List Mutability", 
         "rationale": "a and b reference same list. Modifying via a affects b. b[0] becomes 10."},
    
    17: {"answer": "C", "topic": "List Methods", 
         "rationale": "extend() adds elements individually: [1,2] + [3,4] items = [1,2,3,4]."},
    
    18: {"answer": "A", "topic": "List Slicing", 
         "rationale": "del removes elements. After del lst[1:3], only indices 0,3,4 remain: [1,4,5]."},
    
    19: {"answer": "B", "topic": "List Comprehension", 
         "rationale": "[x**2 for x in range(4)] = [0,1,4,9]. Sum = 0+1+4+9 = 14."},
    
    20: {"answer": "A", "topic": "Nested Lists", 
         "rationale": "matrix[1][2] accesses row index 1 ([4,5,6]), then column index 2 (6)."},
    
    # Section 5: Tuples & Sets (Q21-Q25)
    21: {"answer": "A", "topic": "Tuple Immutability", 
         "rationale": "Tuples are immutable. t[0]=5 raises TypeError, cannot assign to tuple item."},
    
    22: {"answer": "B", "topic": "Tuple Unpacking", 
         "rationale": "*middle captures all elements between first (1) and last (5). middle=[2,3,4]."},
    
    23: {"answer": "C", "topic": "Set Operations", 
         "rationale": "& is intersection (common elements). {1,2,3} & {2,3,4} = {2,3}."},
    
    24: {"answer": "A", "topic": "Set Properties", 
         "rationale": "Sets remove duplicates automatically. len({1,1,2,2,3}) = len({1,2,3}) = 3."},
    
    25: {"answer": "B", "topic": "Set Difference", 
         "rationale": "- is set difference. {1,2,3} - {2,3,4} = elements in first not in second = {1}."},
    
    # Section 6: Dictionaries (Q26-Q30)
    26: {"answer": "B", "topic": "Dictionary Access", 
         "rationale": ".get('c', 0) returns default 0 if 'c' not found. 'd' doesn't exist, returns 0."},
    
    27: {"answer": "A", "topic": "Dictionary Methods", 
         "rationale": ".keys() returns dict_keys object, .values() returns dict_values. Both are views."},
    
    28: {"answer": "B", "topic": "Dictionary Iteration", 
         "rationale": "Iterating over dict iterates over keys only. Prints: 'a', 'b', 'c'."},
    
    29: {"answer": "C", "topic": "Dict Comprehension", 
         "rationale": "{x: x**2 for x in range(3)} = {0:0, 1:1, 2:4}. Sum of values: 0+1+4=5."},
    
    30: {"answer": "A", "topic": "Nested Dictionary", 
         "rationale": "d['a']['b'] first gets {'b':2}, then gets value 2 for key 'b'."},
    
    # Section 7: Control Flow (Q31-Q35)
    31: {"answer": "B", "topic": "If/Else", 
         "rationale": "x=0 is falsy. Condition is False, so else branch executes. Prints 'No'."},
    
    32: {"answer": "A", "topic": "For Loop with Range", 
         "rationale": "range(1,10,2) = [1,3,5,7,9]. Sum = 1+3+5+7+9 = 25."},
    
    33: {"answer": "C", "topic": "While Loop with Break", 
         "rationale": "Loop: i=0,1,2,3. When i=3, break executes before print. Last printed is 2."},
    
    34: {"answer": "B", "topic": "Continue Statement", 
         "rationale": "continue skips when i%2==0. Only odd numbers (1,3) are printed."},
    
    35: {"answer": "A", "topic": "Else with Loops", 
         "rationale": "else executes when loop completes normally (no break). Prints 'Done'."},
    
    # Section 8: Functions (Q36-Q40)
    36: {"answer": "B", "topic": "Default Parameters", 
         "rationale": "greet('World') uses default greeting='Hello'. Returns 'Hello, World!'."},
    
    37: {"answer": "A", "topic": "Return Values", 
         "rationale": "Function with no return statement returns None by default."},
    
    38: {"answer": "C", "topic": "*args", 
         "rationale": "*args collects all positional arguments into tuple. args = (1,2,3,4,5)."},
    
    39: {"answer": "B", "topic": "**kwargs", 
         "rationale": "**kwargs collects keyword arguments into dict. kwargs = {'a':1, 'b':2}."},
    
    40: {"answer": "A", "topic": "Lambda Functions", 
         "rationale": "lambda x,y: x+y creates anonymous function. (3,4) returns 3+4 = 7."},
    
    # Section 9: File Handling & Error Handling (Q41-Q45)
    41: {"answer": "B", "topic": "File Modes", 
         "rationale": "'r' is read mode. Writing to read-only file raises io.UnsupportedOperation."},
    
    42: {"answer": "A", "topic": "With Statement", 
         "rationale": "'with' context manager automatically closes file, even if exception occurs."},
    
    43: {"answer": "C", "topic": "Try/Except", 
         "rationale": "except catches ValueError. Prints 'Error' then continues to 'Done'."},
    
    44: {"answer": "B", "topic": "Finally Block", 
         "rationale": "finally always executes, even after return. Both 'Finally' and return value 1."},
    
    45: {"answer": "A", "topic": "Multiple Except", 
         "rationale": "1/0 raises ZeroDivisionError. First matching except block handles it."},
    
    # Section 10: Advanced Topics (Q46-Q50)
    46: {"answer": "B", "topic": "List vs Generator", 
         "rationale": "Generator expressions use () and are lazy (memory efficient). [] creates list."},
    
    47: {"answer": "A", "topic": "Map Function", 
         "rationale": "map(str, [1,2,3]) applies str to each element. list() converts to ['1','2','3']."},
    
    48: {"answer": "C", "topic": "Filter Function", 
         "rationale": "filter keeps elements where lambda returns True. Even numbers: [2,4]."},
    
    49: {"answer": "B", "topic": "Zip Function", 
         "rationale": "zip pairs elements: (1,'a'), (2,'b'), (3,'c'). list() creates list of tuples."},
    
    50: {"answer": "A", "topic": "Enumerate", 
         "rationale": "enumerate adds index. With start=1: (1,'a'), (2,'b'), (3,'c')."},
}


# =============================================================================
# DETAILED EXPLANATIONS BY SECTION
# =============================================================================

SECTION_EXPLANATIONS = """
============================================================================
SECTION 1: VARIABLES & DATA TYPES (Questions 1-5)
============================================================================

Key Concepts:
- Python has dynamic typing (variables can change type)
- type() returns the class of an object
- Falsy values: None, 0, 0.0, '', [], {}, set(), False
- int() truncates toward zero (not floor!)
- Multi-line strings: \\n, ''', \"\"\"

Common Mistakes:
- Confusing int() truncation with floor division
- Assuming 0 or empty containers are True
- Forgetting that type comparison uses class objects


============================================================================
SECTION 2: OPERATORS (Questions 6-10)
============================================================================

Key Concepts:
- // floor division (integer result)
- % modulo (remainder)
- / true division (always float)
- ** exponentiation (right-associative!)
- Operator precedence: ** > not > and > or
- == checks value equality, 'is' checks identity

Common Mistakes:
- Assuming ** is left-associative like other operators
- Confusing == and is for mutable objects
- Forgetting operator precedence in complex expressions


============================================================================
SECTION 3: STRINGS (Questions 11-15)
============================================================================

Key Concepts:
- Strings are immutable (cannot modify in place)
- Slicing: s[start:stop:step]
- Negative indices count from end
- String methods return new strings
- f-strings evaluate expressions inside {}

Common Mistakes:
- Trying to modify string characters directly
- Forgetting that split() returns a list
- Off-by-one errors in slicing


============================================================================
SECTION 4: LISTS (Questions 16-20)
============================================================================

Key Concepts:
- Lists are mutable
- Assignment creates references, not copies
- extend() vs append(): extend adds elements, append adds object
- List comprehensions: [expr for item in iterable if condition]
- del removes by index, remove() removes by value

Common Mistakes:
- Not understanding reference semantics
- Confusing extend() with append()
- Modifying list while iterating


============================================================================
SECTION 5: TUPLES & SETS (Questions 21-25)
============================================================================

Key Concepts:
- Tuples are immutable
- Extended unpacking with * (Python 3+)
- Sets: unordered, unique elements only
- Set operations: & (intersection), | (union), - (difference)

Common Mistakes:
- Trying to modify tuple elements
- Expecting sets to maintain order
- Confusing set operations with list operations


============================================================================
SECTION 6: DICTIONARIES (Questions 26-30)
============================================================================

Key Concepts:
- Keys must be hashable (immutable)
- .get(key, default) returns default if key missing
- Iterating over dict iterates over keys
- dict.items() returns key-value pairs
- Dict comprehensions: {k: v for k, v in items}

Common Mistakes:
- Using mutable objects as keys
- Forgetting .get() returns None by default
- Modifying dict while iterating


============================================================================
SECTION 7: CONTROL FLOW (Questions 31-35)
============================================================================

Key Concepts:
- Truthy/falsy evaluation in conditions
- range(start, stop, step) - stop is exclusive
- break exits loop, continue skips iteration
- else clause on loops executes if no break

Common Mistakes:
- Off-by-one errors with range()
- Forgetting break prevents else execution
- Confusing continue with break


============================================================================
SECTION 8: FUNCTIONS (Questions 36-40)
============================================================================

Key Concepts:
- Default parameters evaluated once at definition
- *args collects positional args as tuple
- **kwargs collects keyword args as dict
- Functions without return return None
- Lambda: anonymous single-expression functions

Common Mistakes:
- Using mutable default parameters
- Confusing *args and **kwargs
- Forgetting lambda is limited to expressions


============================================================================
SECTION 9: FILE HANDLING & ERROR HANDLING (Questions 41-45)
============================================================================

Key Concepts:
- File modes: 'r' (read), 'w' (write), 'a' (append)
- 'with' statement ensures proper cleanup
- try/except/else/finally structure
- finally always executes

Common Mistakes:
- Not closing files (use 'with'!)
- Catching too broad exceptions
- Forgetting finally runs even after return


============================================================================
SECTION 10: ADVANCED TOPICS (Questions 46-50)
============================================================================

Key Concepts:
- Generators are lazy (memory efficient)
- map() applies function to all elements
- filter() keeps elements where function returns True
- zip() pairs elements from multiple iterables
- enumerate() adds index to iteration

Common Mistakes:
- Forgetting map/filter return iterators in Python 3
- Not converting to list when needed
- zip() stops at shortest iterable
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
    print("\n" + "=" * 70)
    print("QUIZ ANSWER KEY - SUMMARY")
    print("=" * 70)
    print(f"{'Q#':<4} {'Ans':<4} {'Topic':<25} {'Rationale':<35}")
    print("-" * 70)
    
    for q_num in sorted(ANSWER_KEY.keys()):
        q = ANSWER_KEY[q_num]
        # Truncate rationale for display
        rationale = q['rationale'][:32] + "..." if len(q['rationale']) > 35 else q['rationale']
        print(f"{q_num:<4} {q['answer']:<4} {q['topic']:<25} {rationale}")


def print_answers_by_section():
    """Print answers grouped by section."""
    sections = {
        "Variables & Data Types": range(1, 6),
        "Operators": range(6, 11),
        "Strings": range(11, 16),
        "Lists": range(16, 21),
        "Tuples & Sets": range(21, 26),
        "Dictionaries": range(26, 31),
        "Control Flow": range(31, 36),
        "Functions": range(36, 41),
        "File & Error Handling": range(41, 46),
        "Advanced Topics": range(46, 51),
    }
    
    for section, q_range in sections.items():
        print(f"\n{'='*50}")
        print(f"  {section}")
        print(f"{'='*50}")
        for q_num in q_range:
            if q_num in ANSWER_KEY:
                q = ANSWER_KEY[q_num]
                print(f"  Q{q_num}: {q['answer']} - {q['rationale'][:50]}...")


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


# =============================================================================
# MAIN - Display Answer Key
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("   QUIZ ANSWER KEY - Foundation of Python Programming")
    print("   50 Questions with Answers and Rationale")
    print("=" * 70)
    
    # Print quick reference
    print_all_answers()
    
    # Print by section
    print("\n\n")
    print_answers_by_section()
    
    # Print section explanations
    print(SECTION_EXPLANATIONS)
    
    print("\n" + "=" * 70)
    print("   END OF ANSWER KEY")
    print("=" * 70)
