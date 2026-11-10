# Week 2: Loops

## Key Concepts
- **loop**: lets you create a block of code that runs an action several times, as long as a condition is met
- **while**: a while loop works by repeatedly checking whether its condition is still true
- **list**: in Python, a list is like a list in real life, a sequence of elements, such as a to-do list
- **for**: a loop we use when we know in advance how many times we want to run a block of code
- **range**: this function returns a range of values; it expects at least one argument, e.g. `range(3)`
- **len**: a function that tells us the length of a list (it also works on strings, e.g. `len("cat")` is 3)
- **dict**: dicts are data structures that let us associate keys with values. It's like a dictionary in the real world
- **None**: `None` officially represents the absence of a value (for now I use it in dictionaries)

## What I learned
- When using a `while` loop, pay attention to the condition you give it, otherwise the loop will never stop (see the examples in the "Code examples" section).
- In programming you can increment a variable by writing `i += 1` instead of `i = i + 1`. They have the same meaning and do the same thing.
- When using `range()` with one number, we get a range of values starting at 0 and stopping just before **the number you specify** (`range(3)` gives 0, 1, 2).
- When using a `for` loop, you don't need to initialize the variable yourself: Python takes care of it.
- If we have a lot of information to store, we can use a list of dictionaries.
- We can use `.isdigit()` to check if all the characters of a string are digits. It only works on **strings**.
- We can use `.isalpha()` to check if all the characters of a string are letters. It only works on **strings**.
- We can use `.isalnum()` to check if a string is made only of letters and/or digits. It only works on **strings**.

## Code examples
```python
i = 1
while i != 0:
    print("meow")
```
In this case the loop will never end because `i` never changes, so it never reaches 0.

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```
In this case the loop stops after printing "meow" three times.

```python
for _ in range(3):
    print("meow")
```
This code is written in a "Pythonic" way. The `_` shows that the variable's name doesn't matter: we just need to print "meow" three times.

```python
students = ["Hermione", "Harry", "Ron"]
print(len(students))
```
Here the code prints 3.

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
```
This is how we create a dictionary and print the value associated with each key.

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
```
Here we use `None` to show that Draco has no patronus. This is different from not knowing what his patronus is.

## Mistakes and fixes
- None

## Questions to ask
- None

## Problem Set progress
- [x] camelCase
- [x] Coke Machine
- [x] Just setting up my twttr
- [x] Vanity Plates
- [x] Nutrition Facts

## Lecture progress
Lecture completed 