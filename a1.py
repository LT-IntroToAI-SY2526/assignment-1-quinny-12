# Assignment 1: AI-Generated Python Problems
# Name: Quinn Downey

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience 
with JavaScript and Java (but have not used Java in some time). I have taken a programming 
1 class in Java and AP Computer Science Principles in JavaScript, and am currently taking 
AP Computer Science A in Java. I have never before used Java. Can you create 5-7 practice 
problems that cover: > - Variables and basic data types > - Conditionals (if/elif/else) > 
- Loops (for and while) > - Functions > - Basic list operations >  > Make them 
progressively more challenging. Make sure each problem has clear instructions and example 
inputs/outputs.
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
# Python Practice Problems: Variables to Lists

## Problem 1: Temperature Converter (Variables & Conditionals)
**Concepts**: Variables, basic data types, if/elif/else statements, input/output

Write a program that converts temperatures between Celsius and Fahrenheit. The program should:
1. Ask the user for a temperature value and the unit (C or F)
2. Convert the temperature to the other unit
3. Display the result with appropriate formatting

**Formulas:**
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9

**Example Input/Output:**
```
Enter temperature: 25
Enter unit (C/F): C
25.0°C is equal to 77.0°F

Enter temperature: 68
Enter unit (C/F): F
68.0°F is equal to 20.0°C


```

---

## Problem 2: Number Guessing Game (Loops & Conditionals)
**Concepts**: while loops, conditionals, variables, random numbers

Create a number guessing game where:
1. The program generates a random number between 1 and 100
2. The user has to guess the number
3. After each guess, provide feedback ("Too high", "Too low", or "Correct!")
4. Count and display the number of attempts when the user wins
5. The game continues until the correct number is guessed

**Example Input/Output:**
```
I'm thinking of a number between 1 and 100!
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 31
Correct! You guessed it in 4 attempts!
```

**Hint:** Use `import random` and `random.randint(1, 100)`

---

## Problem 3: Grade Calculator (Functions & Lists)
**Concepts**: Functions, lists, for loops, conditionals

Write a program with the following functions:
1. `calculate_average(grades)` - takes a list of grades and returns the average
2. `get_letter_grade(average)` - converts a numerical average to a letter grade
3. `main()` - handles user input and displays results

**Grading Scale:**
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

**Example Input/Output:**
```
How many grades do you want to enter? 4
Enter grade 1: 85
Enter grade 2: 92
Enter grade 3: 78
Enter grade 4: 88

Grades: [85, 92, 78, 88]
Average: 85.75
Letter Grade: B
```

---

## Problem 4: Word Frequency Counter (Lists & Loops)
**Concepts**: Lists, dictionaries, for loops, string methods, functions

Create a program that analyzes text and counts word frequency:
1. Ask the user to enter a sentence
2. Convert the sentence to lowercase and split into words
3. Remove punctuation from words
4. Count how many times each word appears
5. Display the results sorted by frequency (highest first)

**Example Input/Output:**
```
Enter a sentence: The quick brown fox jumps over the lazy dog. The dog was very lazy!

Word Frequency:
the: 3
lazy: 2
dog: 2
quick: 1
brown: 1
fox: 1
jumps: 1
over: 1
was: 1
very: 1
```

**Hints:** 
- Use `.lower()`, `.split()`, and `.strip(".,!?")` methods
- Consider using a dictionary to store word counts

---

## Problem 5: Shopping List Manager (Functions & List Operations)
**Concepts**: Lists, functions, while loops, conditionals, list methods

Create a shopping list program with a menu system:
1. Add item to list
2. Remove item from list
3. View current list
4. Clear entire list
5. Search for an item
6. Exit

The program should handle invalid menu choices and continue running until the user chooses to exit.

**Example Input/Output:**
```
=== Shopping List Manager ===
1. Add item
2. Remove item
3. View list
4. Clear list
5. Search for item
6. Exit

Choose an option (1-6): 1
Enter item to add: apples
Added 'apples' to your list.

Choose an option (1-6): 1
Enter item to add: bread
Added 'bread' to your list.

Choose an option (1-6): 3
Your shopping list:
1. apples
2. bread

Choose an option (1-6): 5
Enter item to search for: apples
'apples' is in your list at position 1.

Choose an option (1-6): 6
Goodbye!
```

---

## Problem 6: Prime Number Finder (Advanced Loops & Functions)
**Concepts**: Functions, nested loops, conditionals, lists, mathematical logic

Write a program that finds all prime numbers up to a given limit:
1. Create a function `is_prime(n)` that returns True if n is prime, False otherwise
2. Create a function `find_primes(limit)` that returns a list of all primes up to the limit
3. Display the primes and count how many were found
4. Also show the largest prime found

**Example Input/Output:**
```
Enter the upper limit: 30

Prime numbers up to 30:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

Total primes found: 10
Largest prime: 29
```

**Challenge Extension:** Implement the "Sieve of Eratosthenes" algorithm for better efficiency!

---

## Problem 7: Text Adventure Game (All Concepts Combined)
**Concepts**: All previous concepts integrated - functions, lists, loops, conditionals, variables

Create a simple text-based adventure game:
1. Player starts with 100 health and an empty inventory
2. Present choices that affect health and inventory
3. Use functions for different game scenarios
4. Game ends when health reaches 0 or player finds the treasure
5. Track and display game statistics

**Example Structure:**
```python
def display_status(health, inventory):
    # Show current health and inventory

def forest_encounter(health, inventory):
    # Handle forest scenario
    
def cave_encounter(health, inventory):
    # Handle cave scenario
    
def main():
    # Main game loop
```

**Example Input/Output:**
```
=== Welcome to the Adventure Game! ===
Health: 100 | Inventory: []

You find yourself at a crossroads.
1. Enter the dark forest
2. Explore the mysterious cave
3. Rest by the river
4. Check inventory
5. Quit game

Choose your action (1-5): 1

You enter the dark forest and encounter a wolf!
1. Fight the wolf (-20 health, gain 'wolf pelt')
2. Run away (-5 health)

Choose your action (1-2): 1
You fought bravely! Health: 80 | Inventory: ['wolf pelt']

[Game continues...]
```

## Tips for Success:
1. Start with Problem 1 and work your way up
2. Test your code with different inputs
3. Use meaningful variable names
4. Add comments to explain your logic
5. Don't be afraid to break complex problems into smaller functions
6. Remember that Python is case-sensitive and uses indentation for code blocks

Good luck with your Python practice!
"""

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
PROBLEM 1
"""
