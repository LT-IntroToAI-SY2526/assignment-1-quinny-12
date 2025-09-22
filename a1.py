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
I'm learning Python basics in a high school programming class. 
I have some experience  with JavaScript and Java (but have not 
used Java in some time). I have taken a programming  1 class in
Java and AP Computer Science Principles in JavaScript, and am 
currently taking  AP Computer Science A in Java. I have never 
before used Java. Can you create 5-7 practice  problems that cover: 
> - Variables and basic data types > - Conditionals (if/elif/else) >  
- Loops (for and while) > - Functions > - Basic list operations >  > 
Make them relatively simple because I'm completely new to Python, but
still complex enough that I can gain a deeper understanding of Python. 
Make sure each problem has clear instructions and example inputs/outputs. 
Each problem should make me write the program as a function with or 
without parameters.
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

# Python Basics Practice Problems

# 1. Variables and Basic Data Types
# Write a function that takes a string parameter `name` and returns a greeting message:
# "Hello, <name>!"
def greet_user(name):
    return "Hello, " + name + "!"
    
    # Example:
    # greet_user("Alice")  -> "Hello, Alice!"
    # greet_user("Bob")    -> "Hello, Bob!"

# 2. Conditionals (if/elif/else)
# Write a function that takes a number `num` and returns:
# "Positive" if num > 0,
# "Negative" if num < 0,
# "Zero" if num == 0
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

    # Example:
    # check_number(10)  -> "Positive"
    # check_number(-3)  -> "Negative"
    # check_number(0)   -> "Zero"

# 3. For Loop
# Write a function that takes a positive integer `n` and returns the sum of numbers from 1 to n.
def sum_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

    # Example:
    # sum_numbers(5) -> 15 (1+2+3+4+5)
    # sum_numbers(3) -> 6  (1+2+3)

# 4. While Loop
# Write a function that takes a positive integer `n` and returns a list counting down from n to 1.
def count_down(n):
    result = []
    while n > 0:
        result.append(n)
        n = n - 1
    return result

    # Example:
    # count_down(5) -> [5, 4, 3, 2, 1]
    # count_down(3) -> [3, 2, 1]


# 5. Functions and Return Values
# Write a function that returns True if a number is even, False if odd.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
    # Example:
    # is_even(4) -> True
    # is_even(7) -> False

# 6. Basic List Operations
# Write a function that doubles each number in a list and returns the new list.
def double_list(nums):
    newList = []
    for i in nums:
        newList.append(i*2)
    return newList
    # Example:
    # double_list([1, 2, 3]) -> [2, 4, 6]
    # double_list([4, 0, -1]) -> [8, 0, -2]

# 7. Combining Lists and Conditionals
# Write a function that returns a new list containing only the positive numbers from the input list.
def filter_positive(nums):
    newList = []
    for i in nums:
        if i > 0:
            newList.append(i)
    return newList
    # Example:
    # filter_positive([1, -2, 3, 0, -5]) -> [1, 3]
    # filter_positive([-1, -2]) -> []

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================

# --- Test cases ---

# 1. greet_user
assert greet_user("Alice") == "Hello, Alice!"
assert greet_user("Bob") == "Hello, Bob!"
assert greet_user("") == "Hello, !"

# 2. check_number
assert check_number(10) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"

# 3. sum_numbers
assert sum_numbers(5) == 15   # 1+2+3+4+5=15
assert sum_numbers(1) == 1
assert sum_numbers(0) == 0    # if you handle zero input

# 4. count_down
assert count_down(5) == [5, 4, 3, 2, 1]
assert count_down(3) == [3, 2, 1]
assert count_down(1) == [1]

# 5. is_even
assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True

# 6. double_list
assert double_list([1, 2, 3]) == [2, 4, 6]
assert double_list([0, -1]) == [0, -2]
assert double_list([]) == []

# 7. filter_positive
assert filter_positive([1, -2, 3, 0, -5]) == [1, 3]
assert filter_positive([-1, -2]) == []
assert filter_positive([0, 5, 10]) == [5, 10]

print("All tests passed!")

