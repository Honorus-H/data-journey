# Week 0: Functions and Variables

## Key concepts
- **Function**: a block of code that does one thing, e.g. `print()`
- **Variable**: a container for a value, e.g. `name = input("What's your name? ")`
- **Method**: a function linked to an object that lets it perform a specific action, e.g. `name.strip()`
- **string**: a string (str) is a sequence of characters used to represent or manipulate text, e.g. `"alice"` or `"momo"` or `'12R4'`
- **int**: an integer is a whole number, like 0, 1 or -1
- **float**: a real number, a number with a decimal point, e.g. `1.09`
- In Python it is possible to create your own function with the keyword `def`


## What I learned
- in the command `print("hello,"+name)`, `"hello,"+name` is one argument.
- a function can have many parameters that modify its behavior.
- there are special ways to display quotes: escape them with a backslash, or use single quotes outside
- methods do not change the original string, they return a new one, so I must store the result: `name = name.strip()`
- `lower()` puts all the characters of a string in lowercase
- **int** and **float** are kinds of data in Python, like **str**
- we can use formatted strings to format the output of a long number, going from `1000` to `1,000`
- **scope**: a variable only exists in the context in which it was defined.
- we use `return` to return a value at the end of a function
- we can use the command `"separator".join(list_of_strings)` to join a list of strings into one string
- we can use the method `.replace()` to change a specific word in a string

## Code examples
```python
name = input("What's your name? ")
print("hello,", name)
```
`input()` asks the user to type something. The answer is stored in `name`.
When we use the `,` in `print()`, it automatically puts a **space** between the arguments.

```python
name= input("what's your name? ")
print("hello," , end="")
print(name)
```
the `end=` parameter modifies what appears at the end of the `print` function. Instead of going to the next line, the second **print** continues on the same line.

```python
print("what's up my \"friend\"")
print('hello "friend"')
```
there are two ways to add quotation marks in a string.

```python
name = input("what's your name?")
name=name.strip()
name=name.capitalize()
print(f"hello, {name}")
```
the `.strip()` method removes spaces at the start and end of a string, not in the middle.
the `.title()` method puts the first letter of each word of a string in capital letters.
`.capitalize()` changes only the first letter of the string, and lowercases the rest.

```python
name = input("what's your name?").strip().title()
first, last=name.split(" ")
print(f"hello, {first}", end=" ")
print(f"is your last name {last}?")
```
in this case the `.split()` method splits the name wherever there is a **space** in the string **name** and assigns the new values to the new variables in order, so it starts with the variable `first`.

```python 
x = float(input("what's x ? "))
y = float(input("what's y ? "))
z = round(x+y)
print(f"{z:,}")
```
Here the command `print(f"{z:,}")` allows us to get outputs like 3,000 or 2,230 or 1,000, with a comma separating every thousand.

```python
def hello(to = "world"):
    print("hello",to)
name = input("what's your name ?")
hello(name)
```
when we are creating a function, we can assign a default value to a parameter, e.g. `to = "world"`. Here the default value of the parameter `to` is `"world"`.

```python
def main():
    name = input("what's your name? ")
    hello(name)

def hello():
    print("hello", name)
```
here there is a scope problem: the `name` variable used in the function `hello()` is not defined in this function.



## Mistakes and fixes
- `input()` did not work with the Code Runner button (the Output panel is read-only). Fix: run the file in the terminal with "Run Python File", or remove the Code Runner extension.
- CS50_TOKEN error: impossible to submit or to check the code in the codespace. Fix: restart the codespace (cs50.dev/restart).
- when we use `input()`, the information entered by the user is always a string. Fix: to change it to an int, we have to use `int()`.

## Questions to ask
- none

## Problem Set progress
- [x] indoor.py
- [x] playback.py
- [x] faces.py
- [x] einstein.py
- [x] tip.py

## Location in the video
video finished