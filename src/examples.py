"""
Code Examples to demonstrate the use of Pytest parameterized tests.
"""

# Mathematical Functions
def addition(a: int | float, b: int | float) -> int | float:
    return a + b

def subtraction(a: int | float, b: int | float) -> int | float:
    return a - b

# String Functions
def reverse_string(string: str) -> str:
    return string[::-1]

def capitalize_string(string: str) -> str:
    return string.upper()

def clean_string(string: str) -> str:
    return string.strip().lower()


# Class Example
class Greeting:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hello(self) -> str:
        return f"Hello {self.name}"
    
    def say_goodbye(self) -> str:
        return f"Goodbye {self.name}"