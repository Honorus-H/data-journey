# Week 1: Conditionals

## Key concepts

- **`if`**: in Python, we can make decisions with `if`, `elif` and `else`
- **Boolean**: a condition gives a `bool`, which has only two values: `True` or `False`
- **Comparison operators**: `>`, `>=`, `<`, `<=`, `==` (equal), `!=` (not equal)
- **`=` vs `==`**: `=` assigns a value to a variable, `==` compares two values
- **`or`**: the condition is true if at least one side is true
- **`and`**: the condition is true only if both sides are true
- **`%` (modulo)**: gives the remainder of a division. `x % 2 == 0` means x is even
- **Pythonic**: something is "pythonic" when it is done the way Python programmers usually do it
- **`match`**: an alternative to a long chain of `if` / `elif` when we compare one value to many possible cases

## What I learned

- Several separate `if` statements are independent: the computer asks a new question each time, and every `if` whose condition is true is executed. With `if / elif / else`, only the first true branch runs.
- Indentation is part of the syntax: without it, the code won't work.
- A function can return a boolean (`True` / `False`) with `return`.
- The value returned by a function can be used like any other value (for example, if it returns a string, we can call `.strip()` on it).
- Pythonic version of a boolean function: `return n % 2 == 0` instead of an `if` / `else` that returns `True` or `False`.

## Code examples

Comparing two numbers:
```python
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

Same idea with `or` (works, but the version above is clearer):
```python
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

Grades with `elif` (only one branch runs):
```python
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

Same program with separate `if`s (several can run):
```python
score = int(input("Score: "))
if score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
if score >= 70:
    print("Grade: C")
if score >= 60:
    print("Grade: D")
```
With `score = 96`, this prints A, B, C **and** D, because all four conditions are true.

Even or odd, with a function that returns a boolean:
```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

`match`:
```python
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```
`|` means "or" between cases, and `_` is the default case (like `else`).

## Mistakes and fixes

- I thought all the `if`s run whatever happens. in fact, every `if` whose condition is true runs; `elif` stops after the first true branch

## Questions to ask

- none

## Problem set progress

- [x] deep
- [x] bank
- [x] extensions
- [ ] interpreter
- [ ] meal

## Location in the video

- finished