# أكواد المحاضرة الأولى: مقدمة إلى علم البيانات (نظري)

## Example 1.1 (صفحة 10): Print "Hello World!"

print("Hello World!")


## Example 1.2 (صفحة 11): Variables

x = 10
y = "Hello"
print(x)
print(y)


## Example 1.3 (صفحة 12): Data Types

x = 10          # int
y = 20.5        # float
z = "Hello"   # str
a = True        # bool

print(type(x))
print(type(y))
print(type(z))
print(type(a))


## Example 1.4 (صفحة 13): Operators

a = 10
b = 3

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division


## Example 1.5 (صفحة 14): Conditional Statements (if-elif-else)

x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


## Example 1.6 (صفحة 15): Loops (for loop)

for i in range(5):
    print(i)


## Example 1.7 (صفحة 16): Loops (while loop)

i = 0
while i < 5:
    print(i)
    i += 1


## Example 1.8 (صفحة 17): Functions

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


## Example 1.9 (صفحة 18): Lists

my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # Accessing elements
my_list.append(6) # Adding elements
my_list.remove(2) # Removing elements
print(my_list)


## Example 1.10 (صفحة 19): Dictionaries

my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"]) # Accessing elements
my_dict["city"] = "New York" # Adding elements
del my_dict["age"] # Removing elements
print(my_dict)


## Example 1.11 (صفحة 20): Modules and Packages

import math

print(math.sqrt(16))


## Example 1.12 (صفحة 21): File I/O

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)


## Example 1.13 (صفحة 22): Classes and Objects

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()


## Example 1.14 (صفحة 23): Error Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

