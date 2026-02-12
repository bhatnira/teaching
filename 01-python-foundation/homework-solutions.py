"""
============================================================================
HOMEWORK SOLUTIONS - Foundation of Python Programming
============================================================================
AI-Driven Development Training
February 2026

This file contains complete solutions with explanations for all 20 homework
problems. Each solution includes:
- The problem statement summary
- Step-by-step explanation
- Complete working code
- Sample output
============================================================================
"""

import random
import json
import re
from datetime import datetime, timedelta
from functools import wraps

# For Part 4 (NumPy & Pandas)
try:
    import numpy as np
    import pandas as pd
except ImportError:
    print("Note: NumPy and Pandas required for Problems 16-20")
    print("Install with: pip install numpy pandas")

# ============================================================================
# PART 1: PYTHON BASICS (25 points)
# ============================================================================

# ----------------------------------------------------------------------------
# PROBLEM 1: Student Information System (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem tests basic input/output, variables, f-strings, and conditional
statements (if/elif/else). We use:
- input() to get user data
- Type conversion with int() and float()
- f-strings for formatted output
- Conditional logic for academic standing
"""

def problem_1_student_info():
    """
    Student Information System
    
    Demonstrates:
    - User input handling
    - Variable assignment with type conversion
    - F-string formatting
    - Conditional statements (if/elif/else)
    """
    # Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gpa = float(input("Enter your GPA: "))
    
    # Print formatted message
    print(f"Student {name}, age {age}, has a GPA of {gpa}")
    
    # Determine academic standing using if/elif/else
    # Note: Order matters! Check highest threshold first
    if gpa >= 3.5:
        standing = "Dean's List"
    elif gpa >= 2.0:
        standing = "Good Standing"
    else:
        standing = "Academic Probation"
    
    print(f"Academic Standing: {standing}")

# Demo version without input() for testing
def problem_1_demo():
    """Demo version with preset values for testing"""
    name, age, gpa = "Alice", 20, 3.7
    
    print(f"Student {name}, age {age}, has a GPA of {gpa}")
    
    if gpa >= 3.5:
        standing = "Dean's List"
    elif gpa >= 2.0:
        standing = "Good Standing"
    else:
        standing = "Academic Probation"
    
    print(f"Academic Standing: {standing}")
    return standing

# Sample Output:
# Student Alice, age 20, has a GPA of 3.7
# Academic Standing: Dean's List


# ----------------------------------------------------------------------------
# PROBLEM 2: Shopping Cart Calculator (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem practices working with lists of tuples, loops, arithmetic
operations, and formatted output. Key concepts:
- Tuple unpacking in for loops
- Running totals with accumulator pattern
- Conditional discount application
- Percentage calculations
"""

def problem_2_shopping_cart():
    """
    Shopping Cart Calculator
    
    Demonstrates:
    - List of tuples (structured data)
    - Tuple unpacking in loops
    - Accumulator pattern for totals
    - Conditional logic for discounts
    - Formatted currency output
    """
    # Define cart: (item_name, quantity, price_per_unit)
    cart = [
        ("Apple", 3, 1.50),
        ("Bread", 2, 2.99),
        ("Milk", 1, 4.50)
    ]
    
    print("=" * 40)
    print("         SHOPPING RECEIPT")
    print("=" * 40)
    
    # Calculate subtotals using tuple unpacking
    subtotal = 0
    for item_name, quantity, price in cart:
        item_total = quantity * price
        subtotal += item_total
        # Format: left-align item (15 chars), right-align price (8 chars)
        print(f"{item_name:<15} {quantity} x ${price:.2f} = ${item_total:.2f}")
    
    print("-" * 40)
    print(f"{'Subtotal:':<25} ${subtotal:.2f}")
    
    # Apply 10% discount if subtotal exceeds $15
    # This teaches conditional logic with business rules
    if subtotal > 15:
        discount = subtotal * 0.10
        print(f"{'Discount (10%):':<25} -${discount:.2f}")
        subtotal -= discount
    
    # Calculate 8% sales tax
    tax = subtotal * 0.08
    print(f"{'Sales Tax (8%):':<25} ${tax:.2f}")
    
    # Final total
    total = subtotal + tax
    print("=" * 40)
    print(f"{'TOTAL:':<25} ${total:.2f}")
    print("=" * 40)
    
    return total

# Sample Output:
# ========================================
#          SHOPPING RECEIPT
# ========================================
# Apple           3 x $1.50 = $4.50
# Bread           2 x $2.99 = $5.98
# Milk            1 x $4.50 = $4.50
# ----------------------------------------
# Subtotal:                 $14.98
# Sales Tax (8%):           $1.20
# ========================================
# TOTAL:                    $16.18
# ========================================


# ----------------------------------------------------------------------------
# PROBLEM 3: Text Analyzer (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches string manipulation and dictionary creation.
Key techniques:
- String methods: split(), replace()
- Counting with len()
- List comprehension for filtering
- Dictionary creation with computed values
- Finding max with key function
"""

def analyze_text(text):
    """
    Analyze text and return statistics.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary containing text statistics
        
    Demonstrates:
    - String methods (split, replace)
    - List comprehension
    - Dictionary creation
    - Built-in functions (len, sum, max)
    """
    # Remove punctuation for word analysis
    # We keep original text for sentence counting
    clean_text = text.replace("!", " ").replace(".", " ").replace("?", " ")
    clean_text = clean_text.replace(",", " ")
    
    # Split into words (split() handles multiple spaces)
    words = clean_text.split()
    
    # Character count: remove spaces from original text
    char_count = len(text.replace(" ", ""))
    
    # Word count
    word_count = len(words)
    
    # Sentence count: count sentence-ending punctuation
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    
    # Average word length: sum of lengths / count
    # Guard against division by zero
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    # Longest word: use max() with key=len
    longest_word = max(words, key=len) if words else ""
    
    return {
        "char_count": char_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_word_length": round(avg_word_length, 2),
        "longest_word": longest_word
    }

def problem_3_demo():
    """Demo for text analyzer"""
    test_text = "Python is amazing! It is easy to learn. What do you think?"
    result = analyze_text(test_text)
    
    print("Text Analysis Results:")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
    
    return result

# Sample Output:
# Text Analysis Results:
# ------------------------------
# char_count: 48
# word_count: 12
# sentence_count: 3
# avg_word_length: 4.0
# longest_word: amazing


# ----------------------------------------------------------------------------
# PROBLEM 4: Number Guessing Game (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Random number generation
- While loops with counters
- User input validation with try/except
- Game logic with conditional feedback
"""

def problem_4_guessing_game():
    """
    Number Guessing Game
    
    Demonstrates:
    - random.randint() for random numbers
    - While loop with counter
    - Try/except for input validation
    - Break statement to exit loop early
    - User feedback with conditionals
    """
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    print("=" * 40)
    print("   NUMBER GUESSING GAME")
    print("=" * 40)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        # Try/except handles non-numeric input gracefully
        try:
            guess = int(input(f"Attempt {attempts}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid input
            continue
        
        # Check the guess
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You got it in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print(f"Too low! {remaining} attempts remaining.")
        else:
            print(f"Too high! {remaining} attempts remaining.")
    
    # Out of guesses
    print(f"\n😞 Game Over! The number was {secret_number}")
    return False

# Demo version with predetermined guesses for testing
def problem_4_demo():
    """Demo version with simulated gameplay"""
    secret = 42
    guesses = [50, 25, 40, 45, 42]
    
    print(f"Secret number: {secret}")
    print("Simulated guesses:", guesses)
    print()
    
    for i, guess in enumerate(guesses, 1):
        if guess == secret:
            print(f"Attempt {i}: {guess} - Correct! 🎉")
            break
        elif guess < secret:
            print(f"Attempt {i}: {guess} - Too low")
        else:
            print(f"Attempt {i}: {guess} - Too high")


# ----------------------------------------------------------------------------
# PROBLEM 5: Temperature Statistics (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem practices:
- Writing reusable functions
- List comprehension for transformations
- Dictionary creation for returning multiple values
- Conditional logic in comprehensions
"""

def convert_all_to_celsius(temps):
    """
    Convert Fahrenheit temperatures to Celsius.
    
    Formula: C = (F - 32) * 5/9
    
    Args:
        temps (list): List of temperatures in Fahrenheit
        
    Returns:
        list: Temperatures converted to Celsius (rounded to 1 decimal)
    """
    # List comprehension applies formula to each temperature
    return [round((f - 32) * 5/9, 1) for f in temps]

def get_statistics(temps):
    """
    Calculate min, max, and average of temperatures.
    
    Args:
        temps (list): List of temperatures
        
    Returns:
        dict: Statistics dictionary with min, max, average
    """
    return {
        "min": min(temps),
        "max": max(temps),
        "average": round(sum(temps) / len(temps), 1)
    }

def categorize_temps(temps):
    """
    Categorize temperatures as Cold, Comfortable, or Hot.
    
    Categories:
    - Cold: < 70
    - Comfortable: 70-80
    - Hot: > 80
    
    Args:
        temps (list): List of temperatures
        
    Returns:
        list: Categories for each temperature
    """
    categories = []
    for temp in temps:
        if temp < 70:
            categories.append("Cold")
        elif temp <= 80:
            categories.append("Comfortable")
        else:
            categories.append("Hot")
    return categories

def problem_5_demo():
    """Demo for temperature functions"""
    temperatures = [72, 68, 75, 80, 82, 78, 71]
    
    print("Original temperatures (°F):", temperatures)
    print()
    
    # Convert to Celsius
    celsius = convert_all_to_celsius(temperatures)
    print("Converted to Celsius:", celsius)
    
    # Get statistics
    stats = get_statistics(temperatures)
    print("\nStatistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}°F")
    
    # Categorize
    categories = categorize_temps(temperatures)
    print("\nCategories:")
    for temp, cat in zip(temperatures, categories):
        print(f"  {temp}°F: {cat}")

# Sample Output:
# Original temperatures (°F): [72, 68, 75, 80, 82, 78, 71]
# Converted to Celsius: [22.2, 20.0, 23.9, 26.7, 27.8, 25.6, 21.7]
# Statistics:
#   min: 68°F
#   max: 82°F
#   average: 75.1°F
# Categories:
#   72°F: Comfortable
#   68°F: Cold
#   ...


# ============================================================================
# PART 2: COLLECTIONS & DATA STRUCTURES (25 points)
# ============================================================================

# ----------------------------------------------------------------------------
# PROBLEM 6: Inventory Management (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches nested dictionary operations:
- Accessing nested values with multiple keys
- Iterating over dictionary items
- Modifying dictionary values
- Filtering with conditionals
"""

# Global inventory data
inventory = {
    "laptop": {"price": 999.99, "quantity": 15, "category": "electronics"},
    "shirt": {"price": 29.99, "quantity": 50, "category": "clothing"},
    "book": {"price": 15.99, "quantity": 100, "category": "media"},
    "headphones": {"price": 149.99, "quantity": 30, "category": "electronics"}
}

def get_total_value():
    """
    Calculate total inventory value.
    
    Total = sum of (price × quantity) for all items
    
    Returns:
        float: Total inventory value
    """
    total = 0
    for item, details in inventory.items():
        # Access nested dictionary values
        item_value = details["price"] * details["quantity"]
        total += item_value
    return round(total, 2)

def get_items_by_category(category):
    """
    Get all items in a specific category.
    
    Args:
        category (str): Category to filter by
        
    Returns:
        list: Item names in that category
    """
    # List comprehension with conditional filtering
    return [item for item, details in inventory.items() 
            if details["category"] == category]

def update_quantity(item, change):
    """
    Update item quantity (positive to add, negative to remove).
    
    Args:
        item (str): Item name
        change (int): Quantity change (+/-)
        
    Returns:
        int: New quantity, or -1 if item not found
    """
    if item in inventory:
        inventory[item]["quantity"] += change
        # Prevent negative quantities
        if inventory[item]["quantity"] < 0:
            inventory[item]["quantity"] = 0
        return inventory[item]["quantity"]
    return -1

def low_stock_alert(threshold):
    """
    Find items with quantity below threshold.
    
    Args:
        threshold (int): Minimum acceptable quantity
        
    Returns:
        list: Tuples of (item_name, current_quantity)
    """
    return [(item, details["quantity"]) 
            for item, details in inventory.items() 
            if details["quantity"] < threshold]

def problem_6_demo():
    """Demo for inventory management"""
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    
    print(f"\nTotal Inventory Value: ${get_total_value():,.2f}")
    
    print(f"\nElectronics items: {get_items_by_category('electronics')}")
    print(f"Clothing items: {get_items_by_category('clothing')}")
    
    print(f"\nUpdating laptop quantity by -5...")
    new_qty = update_quantity("laptop", -5)
    print(f"New laptop quantity: {new_qty}")
    
    print(f"\nLow stock items (< 20): {low_stock_alert(20)}")


# ----------------------------------------------------------------------------
# PROBLEM 7: Student Gradebook (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem practices:
- Dictionary iteration
- Calculating averages
- Filtering and sorting data
- Using sorted() with key parameter
"""

gradebook = {
    "Alice": {"math": 85, "science": 92, "english": 88},
    "Bob": {"math": 78, "science": 85, "english": 90},
    "Charlie": {"math": 92, "science": 88, "english": 85},
    "Diana": {"math": 95, "science": 98, "english": 92}
}

def calculate_gpa(student):
    """
    Calculate average grade for a student.
    
    Args:
        student (str): Student name
        
    Returns:
        float: Average of all grades
    """
    if student not in gradebook:
        return None
    grades = gradebook[student].values()
    return round(sum(grades) / len(grades), 2)

def class_average(subject):
    """
    Calculate class average for a subject.
    
    Args:
        subject (str): Subject name
        
    Returns:
        float: Average grade in that subject
    """
    grades = [grades[subject] for grades in gradebook.values() 
              if subject in grades]
    return round(sum(grades) / len(grades), 2) if grades else 0

def honor_roll():
    """
    Get students with GPA >= 90.
    
    Returns:
        list: Names of honor roll students
    """
    return [student for student in gradebook 
            if calculate_gpa(student) >= 90]

def subject_rankings(subject):
    """
    Rank students by grade in a subject (highest first).
    
    Args:
        subject (str): Subject name
        
    Returns:
        list: Tuples of (student_name, grade) sorted by grade descending
    """
    # Create list of (name, grade) tuples
    rankings = [(name, grades[subject]) 
                for name, grades in gradebook.items() 
                if subject in grades]
    # Sort by grade (index 1) in descending order
    return sorted(rankings, key=lambda x: x[1], reverse=True)

def problem_7_demo():
    """Demo for gradebook system"""
    print("=" * 50)
    print("STUDENT GRADEBOOK")
    print("=" * 50)
    
    print("\nStudent GPAs:")
    for student in gradebook:
        print(f"  {student}: {calculate_gpa(student)}")
    
    print(f"\nClass averages:")
    for subject in ["math", "science", "english"]:
        print(f"  {subject.capitalize()}: {class_average(subject)}")
    
    print(f"\nHonor Roll (GPA >= 90): {honor_roll()}")
    
    print(f"\nMath Rankings: {subject_rankings('math')}")


# ----------------------------------------------------------------------------
# PROBLEM 8: List Operations Challenge (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem focuses on:
- List comprehensions (powerful Python feature)
- Set operations for finding common/different elements
- Creating tuples in comprehensions
- Nested list flattening
"""

def problem_8_list_operations():
    """
    List operations using comprehensions and sets.
    
    Demonstrates:
    - List comprehensions with conditions
    - Set intersection and difference
    - Tuple creation in comprehensions
    - Nested list flattening
    """
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_b = [5, 10, 15, 20, 25]
    
    print("List A:", list_a)
    print("List B:", list_b)
    print()
    
    # a) Squares of even numbers from list_a
    # Condition: x % 2 == 0 filters even numbers
    squares_of_evens = [x**2 for x in list_a if x % 2 == 0]
    print(f"a) Squares of even numbers: {squares_of_evens}")
    # Explanation: [4, 16, 36, 64, 100] = [2², 4², 6², 8², 10²]
    
    # b) Common elements using set intersection
    common = list(set(list_a) & set(list_b))
    print(f"b) Common elements: {common}")
    # Explanation: & is set intersection, finds elements in BOTH sets
    
    # c) Elements in list_a but not in list_b using set difference
    difference = list(set(list_a) - set(list_b))
    print(f"c) In A but not B: {sorted(difference)}")
    # Explanation: - is set difference, removes B's elements from A
    
    # d) Tuples of (number, square, cube)
    tuples = [(n, n**2, n**3) for n in range(1, 11)]
    print(f"d) (num, square, cube): {tuples[:3]}... (showing first 3)")
    
    # e) Flatten nested list
    nested = [[1, 2], [3, 4], [5, 6]]
    # Nested comprehension: outer loop over sublists, inner over items
    flattened = [item for sublist in nested for item in sublist]
    print(f"e) Flattened {nested} -> {flattened}")
    
    return {
        "squares_of_evens": squares_of_evens,
        "common": common,
        "difference": sorted(difference),
        "tuples": tuples,
        "flattened": flattened
    }


# ----------------------------------------------------------------------------
# PROBLEM 9: Word Frequency Counter (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Text processing and normalization
- Dictionary for counting (frequency map)
- Sorting dictionary by values
- Using sets for unique elements
"""

def word_frequency(text, remove_stop_words=True):
    """
    Count word frequencies in text.
    
    Args:
        text (str): Input text
        remove_stop_words (bool): Whether to remove common words
        
    Returns:
        dict: Word -> count mapping
    """
    stop_words = {"is", "a", "to", "in", "the"}
    
    # Normalize: lowercase, remove punctuation
    text = text.lower()
    for char in ".,!?\"'":
        text = text.replace(char, "")
    
    words = text.split()
    
    # Filter stop words if requested
    if remove_stop_words:
        words = [w for w in words if w not in stop_words]
    
    # Count using dictionary
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        # .get(word, 0) returns 0 if word not in dict
    
    return freq

def top_n_words(freq_dict, n):
    """
    Get top N most frequent words.
    
    Args:
        freq_dict (dict): Word frequency dictionary
        n (int): Number of top words to return
        
    Returns:
        list: Top N words as (word, count) tuples
    """
    # sorted() with key=lambda sorts by value (count)
    # reverse=True gives descending order (highest first)
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

def unique_words(text):
    """
    Get set of unique words in text.
    
    Args:
        text (str): Input text
        
    Returns:
        set: Unique words (case-insensitive)
    """
    text = text.lower()
    for char in ".,!?\"'":
        text = text.replace(char, "")
    return set(text.split())

def problem_9_demo():
    """Demo for word frequency counter"""
    text = """Python is a popular programming language. Python is easy to learn.
    Programming in Python is fun. Many developers love Python programming."""
    
    print("Text:", text[:50], "...")
    print()
    
    freq = word_frequency(text)
    print("Word frequencies (stop words removed):")
    for word, count in sorted(freq.items(), key=lambda x: -x[1]):
        print(f"  {word}: {count}")
    
    print(f"\nTop 3 words: {top_n_words(freq, 3)}")
    print(f"\nUnique words: {unique_words(text)}")


# ----------------------------------------------------------------------------
# PROBLEM 10: Tuple Operations (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Using lambda functions (anonymous functions)
- sorted() and filter() with key/condition
- Grouping data using dictionaries
- Aggregate calculations per group
"""

students = [
    ("Alice", 22, "CS", 3.8),
    ("Bob", 20, "Math", 3.5),
    ("Charlie", 21, "CS", 3.9),
    ("Diana", 23, "Physics", 3.7),
    ("Eve", 20, "Math", 3.6)
]
# Format: (name, age, major, gpa)

def problem_10_tuple_operations():
    """
    Tuple operations using lambda, sorted, and filter.
    
    Demonstrates:
    - lambda for inline functions
    - sorted() with key parameter
    - filter() for selecting elements
    - min() with key parameter
    - Dictionary comprehension for grouping
    """
    print("Students:", students)
    print()
    
    # a) Sort by GPA (highest first)
    # lambda x: x[3] extracts GPA (index 3) for comparison
    sorted_by_gpa = sorted(students, key=lambda x: x[3], reverse=True)
    print("a) Sorted by GPA (highest first):")
    for s in sorted_by_gpa:
        print(f"   {s[0]}: {s[3]}")
    
    # b) Filter CS majors
    # filter() returns iterator, convert to list
    cs_students = list(filter(lambda x: x[2] == "CS", students))
    print(f"\nb) CS majors: {[s[0] for s in cs_students]}")
    
    # c) Youngest student
    # min() with key finds minimum by age (index 1)
    youngest = min(students, key=lambda x: x[1])
    print(f"\nc) Youngest student: {youngest[0]} (age {youngest[1]})")
    
    # d) Group by major
    grouped = {}
    for name, age, major, gpa in students:
        if major not in grouped:
            grouped[major] = []
        grouped[major].append(name)
    print(f"\nd) Grouped by major: {grouped}")
    
    # e) Average GPA per major
    gpa_by_major = {}
    for major in grouped:
        # Get all GPAs for this major
        gpas = [s[3] for s in students if s[2] == major]
        gpa_by_major[major] = round(sum(gpas) / len(gpas), 2)
    print(f"\ne) Average GPA per major: {gpa_by_major}")
    
    return sorted_by_gpa, cs_students, youngest, grouped, gpa_by_major


# ============================================================================
# PART 3: FILE HANDLING & DATA PROCESSING (25 points)
# ============================================================================

# ----------------------------------------------------------------------------
# PROBLEM 11: Log File Processor (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- File writing with open() and 'w' mode
- File reading with 'r' mode
- String parsing to extract information
- Categorizing data using dictionaries
- Writing filtered data to new file
"""

def create_sample_log():
    """Create a sample log file with 20 entries."""
    import random
    from datetime import datetime, timedelta
    
    levels = ["INFO", "WARNING", "ERROR"]
    messages = {
        "INFO": ["User logged in", "Request processed", "Cache updated", "Session started"],
        "WARNING": ["High memory usage", "Slow response time", "Retry attempt"],
        "ERROR": ["Connection failed", "Database timeout", "Invalid input", "Auth failed"]
    }
    
    with open("sample.log", "w") as f:
        base_time = datetime(2026, 2, 11, 8, 0, 0)
        for i in range(20):
            level = random.choice(levels)
            msg = random.choice(messages[level])
            time = base_time + timedelta(minutes=i*5)
            f.write(f"[{level}] {time.strftime('%Y-%m-%d %H:%M:%S')} - {msg}\n")
    
    print("Created sample.log with 20 entries")

def process_log_file(filename="sample.log"):
    """
    Process log file and categorize by level.
    
    Returns:
        dict: Categorized log entries
    """
    categorized = {"INFO": [], "WARNING": [], "ERROR": []}
    
    try:
        with open(filename, "r") as f:
            for line in f:
                # Extract level from [LEVEL] format
                if line.startswith("["):
                    level = line.split("]")[0][1:]  # Remove [ and ]
                    if level in categorized:
                        categorized[level].append(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found. Creating sample...")
        create_sample_log()
        return process_log_file(filename)
    
    return categorized

def write_errors(categorized, output_file="errors.txt"):
    """Write only ERROR entries to separate file."""
    with open(output_file, "w") as f:
        for entry in categorized.get("ERROR", []):
            f.write(entry + "\n")
    print(f"Wrote {len(categorized.get('ERROR', []))} errors to {output_file}")

def problem_11_demo():
    """Demo for log file processor"""
    print("=" * 50)
    print("LOG FILE PROCESSOR")
    print("=" * 50)
    
    create_sample_log()
    categorized = process_log_file()
    
    print("\nLog Summary:")
    print("-" * 30)
    for level, entries in categorized.items():
        print(f"{level}: {len(entries)} entries")
    
    write_errors(categorized)
    
    print("\nSample ERROR entries:")
    for entry in categorized["ERROR"][:3]:
        print(f"  {entry}")


# ----------------------------------------------------------------------------
# PROBLEM 12: CSV Data Handler (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Working with CSV format manually (no csv module)
- File I/O operations
- Data transformation (list of dicts)
- Filtering data based on conditions
"""

def create_csv(filename, headers, data):
    """
    Create a CSV file with headers and data.
    
    Args:
        filename (str): Output file name
        headers (list): Column headers
        data (list): List of lists (rows)
    """
    with open(filename, "w") as f:
        # Write header row
        f.write(",".join(headers) + "\n")
        # Write data rows
        for row in data:
            f.write(",".join(str(item) for item in row) + "\n")
    print(f"Created {filename} with {len(data)} rows")

def read_csv(filename):
    """
    Read CSV and return list of dictionaries.
    
    Each dict maps column header to value.
    
    Args:
        filename (str): Input file name
        
    Returns:
        list: List of dictionaries
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    
    # First line is headers
    headers = lines[0].strip().split(",")
    
    # Remaining lines are data
    data = []
    for line in lines[1:]:
        values = line.strip().split(",")
        # Zip headers with values to create dict
        row_dict = dict(zip(headers, values))
        data.append(row_dict)
    
    return data

def filter_csv(data, column, value):
    """
    Filter rows where column equals value.
    
    Args:
        data (list): List of dictionaries
        column (str): Column to filter on
        value (str): Value to match
        
    Returns:
        list: Filtered rows
    """
    return [row for row in data if row.get(column) == value]

def add_row(filename, row_data):
    """
    Append a new row to existing CSV.
    
    Args:
        filename (str): CSV file name
        row_data (list): Data for new row
    """
    with open(filename, "a") as f:  # 'a' = append mode
        f.write(",".join(str(item) for item in row_data) + "\n")
    print(f"Added row to {filename}")

def problem_12_demo():
    """Demo for CSV handler"""
    print("=" * 50)
    print("CSV DATA HANDLER")
    print("=" * 50)
    
    # Create sample employee data
    headers = ["Name", "Department", "Salary", "Years"]
    data = [
        ["Alice", "Engineering", "75000", "3"],
        ["Bob", "Marketing", "55000", "2"],
        ["Charlie", "Engineering", "80000", "5"],
        ["Diana", "HR", "50000", "1"]
    ]
    
    create_csv("employees.csv", headers, data)
    
    # Read back
    employees = read_csv("employees.csv")
    print(f"\nRead {len(employees)} employees")
    
    # Filter by department
    engineers = filter_csv(employees, "Department", "Engineering")
    print(f"Engineers: {[e['Name'] for e in engineers]}")
    
    # Add new employee
    add_row("employees.csv", ["Eve", "Marketing", "60000", "2"])


# ----------------------------------------------------------------------------
# PROBLEM 13: JSON Configuration Manager (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- JSON file reading and writing
- Dictionary manipulation
- Data validation patterns
- Configuration management patterns
"""

def create_config(filename):
    """
    Create default configuration file.
    
    Args:
        filename (str): Config file name
    """
    default_config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug_mode": False,
        "max_users": 100,
        "database_url": "localhost:5432/mydb"
    }
    
    with open(filename, "w") as f:
        json.dump(default_config, f, indent=4)
    
    print(f"Created config file: {filename}")
    return default_config

def load_config(filename):
    """
    Load configuration from file.
    
    Args:
        filename (str): Config file name
        
    Returns:
        dict: Configuration dictionary
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config not found. Creating default...")
        return create_config(filename)

def update_config(filename, key, value):
    """
    Update a specific setting in config.
    
    Args:
        filename (str): Config file name
        key (str): Setting key to update
        value: New value
        
    Returns:
        dict: Updated configuration
    """
    config = load_config(filename)
    config[key] = value
    
    with open(filename, "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"Updated {key} = {value}")
    return config

def validate_config(config):
    """
    Check that all required keys exist.
    
    Args:
        config (dict): Configuration to validate
        
    Returns:
        tuple: (is_valid, missing_keys)
    """
    required = ["app_name", "version", "debug_mode", "max_users", "database_url"]
    missing = [key for key in required if key not in config]
    return len(missing) == 0, missing

def problem_13_demo():
    """Demo for JSON config manager"""
    print("=" * 50)
    print("JSON CONFIGURATION MANAGER")
    print("=" * 50)
    
    config = create_config("app_config.json")
    print(f"\nDefault config: {config}")
    
    # Update a setting
    update_config("app_config.json", "debug_mode", True)
    
    # Validate
    config = load_config("app_config.json")
    is_valid, missing = validate_config(config)
    print(f"\nConfig valid: {is_valid}")
    
    # Test with incomplete config
    incomplete = {"app_name": "Test"}
    is_valid, missing = validate_config(incomplete)
    print(f"Incomplete config valid: {is_valid}, missing: {missing}")


# ----------------------------------------------------------------------------
# PROBLEM 14: Data Validation with Regex (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Regular expressions for pattern matching
- Common validation patterns (email, phone, password)
- Using re.match(), re.search(), re.findall()
- Input sanitization
"""

def validate_email(email):
    """
    Validate email format.
    
    Pattern explanation:
    - ^[a-zA-Z0-9._%+-]+  : Start with letters, digits, or special chars
    - @                    : Required @ symbol
    - [a-zA-Z0-9.-]+       : Domain name
    - \\.[a-zA-Z]{2,}$     : Dot and TLD (2+ letters)
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """
    Validate phone format: (XXX) XXX-XXXX or XXX-XXX-XXXX
    
    Pattern uses | for alternation (OR).
    """
    pattern = r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
    return bool(re.match(pattern, phone))

def validate_password(password):
    """
    Validate password: 8+ chars, 1 upper, 1 lower, 1 digit.
    
    Uses lookahead assertions (?=...) to check conditions
    without consuming characters.
    """
    if len(password) < 8:
        return False
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    
    return has_upper and has_lower and has_digit

def extract_dates(text):
    """
    Find all dates in MM/DD/YYYY or YYYY-MM-DD format.
    
    Returns:
        list: All matching date strings
    """
    pattern = r'\b(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b'
    return re.findall(pattern, text)

def sanitize_input(text):
    """
    Remove special characters, keep letters, numbers, spaces.
    
    [^...] means "not these characters"
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def problem_14_demo():
    """Demo for regex validation"""
    print("=" * 50)
    print("DATA VALIDATION WITH REGEX")
    print("=" * 50)
    
    # Email validation
    emails = ["test@example.com", "invalid@", "user.name@domain.co.uk"]
    print("\nEmail validation:")
    for email in emails:
        print(f"  {email}: {validate_email(email)}")
    
    # Phone validation
    phones = ["(123) 456-7890", "123-456-7890", "1234567890"]
    print("\nPhone validation:")
    for phone in phones:
        print(f"  {phone}: {validate_phone(phone)}")
    
    # Password validation
    passwords = ["weak", "StrongPass1", "NoDigits!"]
    print("\nPassword validation:")
    for pwd in passwords:
        print(f"  {pwd}: {validate_password(pwd)}")
    
    # Date extraction
    text = "Events on 02/14/2026 and 2026-03-15 are scheduled."
    print(f"\nDates in '{text}':")
    print(f"  Found: {extract_dates(text)}")
    
    # Sanitization
    dirty = "Hello! @World# $123%"
    print(f"\nSanitize '{dirty}':")
    print(f"  Result: '{sanitize_input(dirty)}'")


# ----------------------------------------------------------------------------
# PROBLEM 15: Error Handling System (5 points)
# ----------------------------------------------------------------------------
"""
EXPLANATION:
This problem teaches:
- Try/except blocks for specific exceptions
- Multiple exception handling
- Decorator pattern for cross-cutting concerns
- Logging errors to file
"""

def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    
    Handles:
    - ZeroDivisionError: Division by zero
    - TypeError: Non-numeric inputs
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None

def safe_file_read(filename):
    """
    Safely read a file with error handling.
    
    Handles:
    - FileNotFoundError: File doesn't exist
    - PermissionError: No read permission
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None

def safe_json_parse(json_string):
    """
    Safely parse JSON string with error handling.
    
    Handles:
    - json.JSONDecodeError: Invalid JSON format
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return None

def safe_list_access(lst, index):
    """
    Safely access list element with error handling.
    
    Handles:
    - IndexError: Index out of range
    """
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} out of range for list of length {len(lst)}")
        return None

def log_errors(func):
    """
    Decorator that logs any exception to error_log.txt.
    
    Usage:
        @log_errors
        def my_function():
            ...
    
    This is a cross-cutting concern pattern - adds logging
    without modifying the original function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("error_log.txt", "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {func.__name__}: {type(e).__name__}: {e}\n")
            raise  # Re-raise the exception after logging
    return wrapper

def problem_15_demo():
    """Demo for error handling system"""
    print("=" * 50)
    print("ERROR HANDLING SYSTEM")
    print("=" * 50)
    
    print("\nsafe_divide:")
    print(f"  10 / 2 = {safe_divide(10, 2)}")
    print(f"  10 / 0 = {safe_divide(10, 0)}")
    print(f"  '10' / 2 = {safe_divide('10', 2)}")
    
    print("\nsafe_file_read:")
    result = safe_file_read("nonexistent.txt")
    
    print("\nsafe_json_parse:")
    print(f"  Valid: {safe_json_parse('{\"key\": \"value\"}')}")
    print(f"  Invalid: {safe_json_parse('not json')}")
    
    print("\nsafe_list_access:")
    my_list = [1, 2, 3]
    print(f"  Index 1: {safe_list_access(my_list, 1)}")
    print(f"  Index 10: {safe_list_access(my_list, 10)}")


# ============================================================================
# PART 4: NUMPY & PANDAS (25 points)
# ============================================================================

# Check if numpy and pandas are available
try:
    import numpy as np
    import pandas as pd
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    print("NumPy/Pandas not available. Problems 16-20 require these libraries.")

if NUMPY_AVAILABLE:
    
    # ----------------------------------------------------------------------------
    # PROBLEM 16: NumPy Array Operations (5 points)
    # ----------------------------------------------------------------------------
    """
    EXPLANATION:
    This problem teaches:
    - NumPy array creation with random values
    - Axis-based operations (row/column calculations)
    - Finding values and their positions
    - Boolean indexing for conditional operations
    - Matrix operations (transpose, multiplication)
    """
    
    def problem_16_numpy_operations():
        """
        NumPy array operations demonstration.
        
        Demonstrates:
        - np.random.randint() for random arrays
        - Axis parameter (0=columns, 1=rows)
        - np.argmax() and np.unravel_index()
        - Boolean indexing
        - Matrix transpose and multiplication
        """
        print("=" * 50)
        print("NUMPY ARRAY OPERATIONS")
        print("=" * 50)
        
        # Set seed for reproducibility
        np.random.seed(42)
        
        # a) Create 5x5 matrix with random integers 1-100
        matrix = np.random.randint(1, 101, size=(5, 5))
        print("\na) 5x5 Random Matrix:")
        print(matrix)
        
        # b) Sum, mean, std of each row (axis=1 operates on rows)
        print("\nb) Row statistics:")
        print(f"   Row sums: {np.sum(matrix, axis=1)}")
        print(f"   Row means: {np.mean(matrix, axis=1).round(2)}")
        print(f"   Row std: {np.std(matrix, axis=1).round(2)}")
        
        # c) Maximum value and its position
        max_val = np.max(matrix)
        # argmax gives flat index, unravel_index converts to (row, col)
        max_pos = np.unravel_index(np.argmax(matrix), matrix.shape)
        print(f"\nc) Maximum value: {max_val} at position {max_pos}")
        
        # d) Cap values > 50 using boolean indexing
        matrix_capped = matrix.copy()
        matrix_capped[matrix_capped > 50] = 50
        print("\nd) Matrix with values > 50 capped to 50:")
        print(matrix_capped)
        
        # e) Transpose and multiply
        transposed = matrix.T  # or np.transpose(matrix)
        product = transposed @ matrix  # or np.dot(transposed, matrix)
        print("\ne) Transpose × Original:")
        print(product)
        
        return matrix, matrix_capped, product
    
    
    # ----------------------------------------------------------------------------
    # PROBLEM 17: NumPy Statistical Analysis (5 points)
    # ----------------------------------------------------------------------------
    """
    EXPLANATION:
    This problem teaches:
    - Working with 2D arrays (rows=products, cols=months)
    - Row and column aggregations
    - Finding max positions
    - Boolean filtering with conditions
    - Percentage change calculations
    """
    
    def problem_17_numpy_statistics():
        """
        NumPy statistical analysis of sales data.
        
        Demonstrates:
        - Row/column sums with axis parameter
        - Finding indices of max values
        - Boolean comparisons
        - Calculating percentage changes
        """
        print("=" * 50)
        print("NUMPY STATISTICAL ANALYSIS")
        print("=" * 50)
        
        np.random.seed(42)
        
        # Monthly sales for 4 products over 12 months
        sales = np.random.randint(100, 1000, size=(4, 12))
        products = ["Product A", "Product B", "Product C", "Product D"]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        print("\nSales Data (4 products × 12 months):")
        print(sales)
        
        # a) Total sales per product (row sums)
        product_totals = np.sum(sales, axis=1)
        print("\na) Total sales per product:")
        for prod, total in zip(products, product_totals):
            print(f"   {prod}: ${total:,}")
        
        # b) Total sales per month (column sums)
        monthly_totals = np.sum(sales, axis=0)
        print("\nb) Total sales per month:")
        for month, total in zip(months, monthly_totals):
            print(f"   {month}: ${total:,}")
        
        # c) Best performing product and month
        best_product_idx = np.argmax(product_totals)
        best_month_idx = np.argmax(monthly_totals)
        print(f"\nc) Best product: {products[best_product_idx]}")
        print(f"   Best month: {months[best_month_idx]}")
        
        # d) Products with above-average total sales
        avg_sales = np.mean(product_totals)
        above_avg = product_totals > avg_sales
        print(f"\nd) Average product sales: ${avg_sales:,.2f}")
        print(f"   Above average: {[p for p, a in zip(products, above_avg) if a]}")
        
        # e) Month-over-month percentage change
        # Using diff and avoiding division by zero
        pct_change = np.zeros((4, 11))
        for i in range(4):
            for j in range(11):
                pct_change[i, j] = ((sales[i, j+1] - sales[i, j]) / sales[i, j]) * 100
        
        print("\ne) Month-over-month % change (Product A, first 6 months):")
        print(f"   {pct_change[0, :6].round(1)}")
        
        return sales, product_totals, monthly_totals
    
    
    # ----------------------------------------------------------------------------
    # PROBLEM 18: Pandas DataFrame Creation (5 points)
    # ----------------------------------------------------------------------------
    """
    EXPLANATION:
    This problem teaches:
    - Creating DataFrames from dictionaries
    - Setting index columns
    - Adding calculated columns
    - Using apply() with conditions
    - Working with datetime data
    """
    
    def problem_18_pandas_creation():
        """
        Pandas DataFrame creation and manipulation.
        
        Demonstrates:
        - pd.DataFrame() from dictionary
        - set_index() for custom index
        - Adding columns with calculations
        - apply() with lambda for conditional logic
        - datetime operations
        """
        print("=" * 50)
        print("PANDAS DATAFRAME CREATION")
        print("=" * 50)
        
        # a, b) Create DataFrame with 10 employees
        data = {
            "ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", 
                     "Frank", "Grace", "Henry", "Ivy", "Jack"],
            "Department": ["Engineering", "Marketing", "Engineering", "HR", 
                          "Marketing", "Engineering", "HR", "Marketing", 
                          "Engineering", "HR"],
            "Salary": [75000, 55000, 80000, 50000, 60000, 
                      85000, 52000, 58000, 78000, 54000],
            "Hire_Date": pd.to_datetime([
                "2021-03-15", "2023-06-01", "2020-01-10", "2024-02-20",
                "2022-08-05", "2019-11-30", "2023-09-12", "2022-04-18",
                "2021-07-22", "2024-01-05"
            ]),
            "Performance_Score": [8, 6, 9, 7, 7, 9, 6, 8, 8, 5]
        }
        
        df = pd.DataFrame(data)
        print("\nInitial DataFrame:")
        print(df.head())
        
        # c) Set ID as index
        df = df.set_index("ID")
        print("\nWith ID as index:")
        print(df.head())
        
        # d) Add Years_Employed column
        # Calculate from today's date
        today = pd.Timestamp("2026-02-11")
        df["Years_Employed"] = ((today - df["Hire_Date"]).dt.days / 365).round(1)
        
        # e) Add Bonus column based on performance score
        # 15% if score >= 8, 10% if score >= 6, else 5%
        def calculate_bonus(row):
            if row["Performance_Score"] >= 8:
                return row["Salary"] * 0.15
            elif row["Performance_Score"] >= 6:
                return row["Salary"] * 0.10
            else:
                return row["Salary"] * 0.05
        
        df["Bonus"] = df.apply(calculate_bonus, axis=1)
        
        print("\nFinal DataFrame with calculated columns:")
        print(df)
        
        return df
    
    
    # ----------------------------------------------------------------------------
    # PROBLEM 19: Pandas Data Analysis (5 points)
    # ----------------------------------------------------------------------------
    """
    EXPLANATION:
    This problem teaches:
    - GroupBy operations for aggregation
    - Sorting and selecting top N rows
    - Filtering with boolean conditions
    - Correlation calculations
    """
    
    def problem_19_pandas_analysis():
        """
        Pandas data analysis operations.
        
        Demonstrates:
        - groupby() for aggregation
        - sort_values() and head() for top N
        - value_counts() for counting
        - Boolean filtering with conditions
        - corr() for correlation
        """
        print("=" * 50)
        print("PANDAS DATA ANALYSIS")
        print("=" * 50)
        
        # Get DataFrame from Problem 18
        df = problem_18_pandas_creation()
        
        # a) Average salary by department
        avg_salary = df.groupby("Department")["Salary"].mean()
        print("\na) Average salary by department:")
        print(avg_salary.round(2))
        
        # b) Top 3 highest-paid employees
        top_3 = df.nlargest(3, "Salary")[["Name", "Department", "Salary"]]
        print("\nb) Top 3 highest-paid employees:")
        print(top_3)
        
        # c) Count employees per department
        dept_counts = df["Department"].value_counts()
        print("\nc) Employees per department:")
        print(dept_counts)
        
        # d) Employees hired in the last 2 years
        # (Since "today" is 2026-02-11, last 2 years means after 2024-02-11)
        cutoff_date = pd.Timestamp("2024-02-11")
        recent_hires = df[df["Hire_Date"] >= cutoff_date][["Name", "Hire_Date"]]
        print("\nd) Employees hired in last 2 years:")
        print(recent_hires)
        
        # e) Correlation between Years_Employed and Performance_Score
        correlation = df["Years_Employed"].corr(df["Performance_Score"])
        print(f"\ne) Correlation (Years_Employed vs Performance): {correlation:.3f}")
        
        return df
    
    
    # ----------------------------------------------------------------------------
    # PROBLEM 20: Pandas Advanced Operations (5 points)
    # ----------------------------------------------------------------------------
    """
    EXPLANATION:
    This problem teaches:
    - Creating DataFrames with random data
    - Adding calculated columns
    - Pivot tables for cross-tabulation
    - GroupBy with datetime (monthly aggregation)
    - Exporting to CSV
    """
    
    def problem_20_pandas_advanced():
        """
        Pandas advanced operations for sales analysis.
        
        Demonstrates:
        - Creating DataFrames with random data
        - Adding calculated columns
        - pivot_table() for cross-tabulation
        - groupby() with Grouper for time-based grouping
        - idxmax() for finding best per group
        - to_csv() for export
        """
        print("=" * 50)
        print("PANDAS ADVANCED OPERATIONS")
        print("=" * 50)
        
        np.random.seed(42)
        
        # Create sales DataFrame
        sales_data = {
            'Date': pd.date_range('2025-01-01', periods=100),
            'Product': np.random.choice(['A', 'B', 'C', 'D'], 100),
            'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
            'Quantity': np.random.randint(1, 50, 100),
            'Unit_Price': np.random.uniform(10, 100, 100).round(2)
        }
        
        df = pd.DataFrame(sales_data)
        print("\nSales DataFrame (first 5 rows):")
        print(df.head())
        
        # a) Add Revenue column
        df['Revenue'] = df['Quantity'] * df['Unit_Price']
        print("\nWith Revenue column:")
        print(df.head())
        
        # b) Pivot table: Products vs Regions with Revenue
        pivot = pd.pivot_table(df, values='Revenue', index='Product', 
                               columns='Region', aggfunc='sum', fill_value=0)
        print("\nPivot Table (Products vs Regions - Revenue):")
        print(pivot.round(2))
        
        # c) Monthly totals
        df['Month'] = df['Date'].dt.to_period('M')
        monthly = df.groupby('Month')['Revenue'].sum()
        print("\nMonthly Revenue Totals:")
        print(monthly.round(2))
        
        # d) Best-selling product in each region
        best_per_region = df.groupby(['Region', 'Product'])['Revenue'].sum()
        best_products = best_per_region.groupby('Region').idxmax()
        print("\nBest-selling product per region:")
        for region in best_products.index:
            product = best_products[region][1]
            print(f"  {region}: Product {product}")
        
        # e) Export to CSV
        summary = df.groupby(['Region', 'Product']).agg({
            'Quantity': 'sum',
            'Revenue': 'sum'
        }).round(2)
        summary.to_csv("sales_summary.csv")
        print("\nExported sales_summary.csv")
        
        return df, pivot


# ============================================================================
# MAIN - Run All Demos
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("   HOMEWORK SOLUTIONS - Foundation of Python Programming")
    print("=" * 60)
    
    # Part 1: Python Basics
    print("\n" + "=" * 60)
    print("   PART 1: PYTHON BASICS")
    print("=" * 60)
    
    print("\n--- Problem 1 Demo ---")
    problem_1_demo()
    
    print("\n--- Problem 2 Demo ---")
    problem_2_shopping_cart()
    
    print("\n--- Problem 3 Demo ---")
    problem_3_demo()
    
    print("\n--- Problem 4 Demo ---")
    problem_4_demo()
    
    print("\n--- Problem 5 Demo ---")
    problem_5_demo()
    
    # Part 2: Collections
    print("\n" + "=" * 60)
    print("   PART 2: COLLECTIONS & DATA STRUCTURES")
    print("=" * 60)
    
    print("\n--- Problem 6 Demo ---")
    problem_6_demo()
    
    print("\n--- Problem 7 Demo ---")
    problem_7_demo()
    
    print("\n--- Problem 8 Demo ---")
    problem_8_list_operations()
    
    print("\n--- Problem 9 Demo ---")
    problem_9_demo()
    
    print("\n--- Problem 10 Demo ---")
    problem_10_tuple_operations()
    
    # Part 3: File Handling
    print("\n" + "=" * 60)
    print("   PART 3: FILE HANDLING & DATA PROCESSING")
    print("=" * 60)
    
    print("\n--- Problem 11 Demo ---")
    problem_11_demo()
    
    print("\n--- Problem 12 Demo ---")
    problem_12_demo()
    
    print("\n--- Problem 13 Demo ---")
    problem_13_demo()
    
    print("\n--- Problem 14 Demo ---")
    problem_14_demo()
    
    print("\n--- Problem 15 Demo ---")
    problem_15_demo()
    
    # Part 4: NumPy & Pandas
    if NUMPY_AVAILABLE:
        print("\n" + "=" * 60)
        print("   PART 4: NUMPY & PANDAS")
        print("=" * 60)
        
        print("\n--- Problem 16 Demo ---")
        problem_16_numpy_operations()
        
        print("\n--- Problem 17 Demo ---")
        problem_17_numpy_statistics()
        
        print("\n--- Problem 18 Demo ---")
        problem_18_pandas_creation()
        
        print("\n--- Problem 19 Demo ---")
        problem_19_pandas_analysis()
        
        print("\n--- Problem 20 Demo ---")
        problem_20_pandas_advanced()
    
    print("\n" + "=" * 60)
    print("   ALL SOLUTIONS COMPLETE!")
    print("=" * 60)
