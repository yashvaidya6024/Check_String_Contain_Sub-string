# Checking if a string contains a substring in Python
"""This Is the first way to do this task,
main_string = "Hello, welcome to the world of programming!"
substring = "Python"
def contains_substring(main_string, substring):
    return substring in main_string 
# Example usagemain_string = "Hello, welcome to the world of Python programming!"
substring = "Python"        
result = contains_substring(main_string, substring)
if result:
    print(f"The substring '{substring}' is found in the main string.")
else:    
    print(f"The substring '{substring}' is not found in the main string.")"""

# This is the second way to do this task,

# in Python, Checking whether a string contain a specific substring is a common task
# More readable, and phonetic way to check if a string contains a substring is to use the `str.find()` method, which returns the lowest index of the substring if it is found in the string, and -1 if it is not found. Here is an example of how to use `str.find()` to check if a string contains a substring:
string = str(input("Enter the main string: "))

if string.find("Python") != -1:
    print("The substring 'Python' is found in the main string.")
elif string.find("world") != -1:
    print("The substring 'world' is found in the main string.")
else:
    print("The specified substring is not found in the main string.")

# for this, you must remember that find() return -1 or failure.
# less readable and slightly more verbase.
# The Bettter way : Using the in operator.
# Python allows you to directly use the in keyword to test for substring.
# presence - just with list, tuples, or dictionaries

if "world" in string:
    print("The substring 'world' is found in the main string.")
else:    
    print("The substring 'world' is not found in the main string.")

if "Python" in string:
    print("The substring 'Python' is found in the main string.")
else:
    print("The substring 'Python' is not found in the main string.")    