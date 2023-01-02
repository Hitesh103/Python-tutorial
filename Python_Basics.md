# Python Basics

## Basic Python Syntax and Concepts

1. Python is a high-level, dynamically-typed, interpreted language. This means that you don't need to specify the data type of a variable when you declare it, and that you can run Python code without compiling it first.

2. Python uses indentation to indicate blocks of code. This is different from languages like C, C++, and Java, which use curly braces to indicate code blocks.

```base
def greet(name):
  print("Hello, " + name + "!")

greet("Alice")  # prints "Hello, Alice!"
```
3. To define a class in Python, use the `class` keyword, followed by the name of the class and a colon:

```base
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def bark(self):
    print("Woof!")

dog1 = Dog("Fido", "Labrador")
dog1.bark()  # prints "Woof!"
```
4. Python uses the `if`, `elif`, and `else` keywords to create conditional statements:

```base
x = 10
if x > 5:
  print("x is greater than 5")
elif x < 5:
  print("x is less than 5")
else:
  print("x is 5")
```

5. Python has a number of built-in data types, including integers (`int`), floating point numbers (`float`), and strings (`str`). You can create a list by enclosing a comma-separated sequence of values in square brackets:

```base
a = 5
print("Type of a: ", type(a))
  
b = 5.0
print("\nType of b: ", type(b))
  
c = 2 + 4j
print("\nType of c: ", type(c))
```

Output :

```base
Type of a:  <class 'int'>

Type of b:  <class 'float'>

Type of c:  <class 'complex'>
```
