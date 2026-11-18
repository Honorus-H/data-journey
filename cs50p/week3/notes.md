# Week 3: Exceptions

## Key concepts
- **Exceptions**: problems that arise while your program is running, things that go wrong within your code.
- **SyntaxError**: an error that happens when your code breaks Python's grammar rules, so Python can't understand or run the program at all.
- **ValueError**: an error that happens when a function receives an argument of the right type but with an inappropriate value (e.g. `int("cat")`).
- **NameError**: an error that happens when you use a variable that has not been defined.
- **try** and **except**: a way to handle errors. Python first runs the code in the `try` block; if an error happens there, it jumps to the matching `except` block instead of crashing the program.
- **else**: used after `try`/`except`, its block runs only if no exception was raised in the `try` block.
- **pass**: a statement that does nothing. It is used when Python requires a block of code but you don't want anything to happen (e.g. in an `except` block to silently ignore an error).

## What I learned
- **SyntaxErrors** can't be handled with `try`/`except`: you have to go back into your code, find the mistake and fix it.
- **break** is used to exit a **loop**. It can be placed inside a conditional or a `try`/`except`/`else` block, but only if that block is itself inside a loop.

## Code examples
```python
print("hello world)
```
Here a quote is missing in the `print`: if we run the code, we get a **SyntaxError**.

```python
x = int(input("What's x? "))
print(f"x is {x}")
```
Here, if you enter a string instead of an integer, you get a **ValueError**.

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
Here, `try` and `except` let us catch the error so the program doesn't crash, and display a message instead.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
Here there is a **NameError** if you enter something that is not an integer: `int()` raises a **ValueError**, and thanks to `try` and `except` the program doesn't crash, but `x` never receives a value. So at the end, when we ask Python to print `x`, we get a **NameError** because `x` was never defined.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
In the previous example, `print(f"x is {x}")` was executed no matter what, which could lead to a **NameError**. Here, `else` lets us run the last `print` only if no **ValueError** happened.

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
Here we added a loop that keeps asking the user for an integer until they enter one.

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        pass
    else:
        break
```
Same idea, but with `pass`: if the input is invalid, nothing is printed and the user is simply asked again.

## Mistakes and fixes


## Questions to ask
- None

## Problem Set progress
- [x] Fuel Gauge
- [x] Felipe's Taqueria
- [ ] Grocery List
- [ ] Outdated

## Location in the video
finished 