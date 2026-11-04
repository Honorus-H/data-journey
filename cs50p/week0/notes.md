# Week 0: Functions and Variables

## Key concepts
- **Function**: a block of code that does one thing, e.g. `print()`
- **Variable**: a container for a value, e.g. `name = input("What's your name? ")`
- **Method**: a function linked to an object that lets it do a specific action e.g. `name.strip()`


## what I learned
- in the command `print("hello,"+name)` the `hello,+name` one arguments
- a function can have a lot of parameters that modify its behavior.
- there are special ways to display quotes: escape them with a backslash, or use single quotes outside
- methods do not change the original string, they return a new one, so I must store the result `name=name.strip()`
- `lower()` put all the characters of a string in lowercase

## Code examples
```python
name = input("What's your name? ")
print("hello,", name)
```
`input()` asks the user to type something. The answer is stored in `name`.
When we use the `,` in the `print()` it automaticly puts a **space** between the arguments.

```python
name= input("what's your name? ")
print("hello," , end="")
print(name)
```
the `end=` parameters modify what appear at the end of the function `print`. instead of going to the next line, the second **print** continues on the same line

```python
print("what's up my \"friend\"")
print('hello "friend"')
```
there are the two ways to add quotation mark in the function 

```python
name = input("what's your name?")
name=name.strip()
name=name.capitalize()
print(f"hello, {name}")
```
the `.strip()` removes spaces at the start and end of a string, not in the middle.
the,`.title()`method put all the first letter of each word of a string in capital letter.
`.capitalize()` changes only the first letter of the string, and lowercases the rest.

```python
name = input("what's your name?").strip().title()
first, last=name.split(" ")
print(f"hello, {first}", end=" ")
print(f"is your last name {last}?")
```
in this case the `.split()`method split the name wherever there is a **space** in the the string **name** and assign the new values to the new variables in order so it starts with the variable `first`.


## Mistakes and fixes
- `input()` did not work with the Code Runner button (Output panel is read-only). Fix: run the file in the terminal with "Run Python File" or remove the extension Code Runner 
- error CS50_TOKEN, impossible to submit or to checck the code int th e code space. Fix : we have just to reload the page.

## Questions to ask
- none

## Problem Set progress
- [x] indoor.py
- [ ] playback.py
- [ ] faces.py
- [ ] einstein.py
- [ ] tip.py

## location in the video
chapter :int , time: 0:59:01
2 november : 2H