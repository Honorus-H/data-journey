# week 2 : Loops 

## Key Concepts 
- **loops** premet you to creat a block of code which executes an action many times with some conditions
- **while**: while loops work by repeatedly asking if the condition of the loop has been fulfilled
- **list**: In python a list is as in our life a list of element or a to do list
- **for**: for is a loop we use when we know in advance how many times we want to execute a code 
- **range**: this focntion returns us a range of value, its expects as input atleast one argument e.g. `range(3)`
- **len***: len is a fucntion that tell us the length of a list 



## What I learned
- when using the loop `while` you should pay attention to the bool you pass to the loop otherwise the loop will never stop(example in the part: codes example).
- in programmation you can increment it's the fact of writting `i += 1`instead of writting `i = i+1` , they have the same meaning and do the same thing.
- when using the function `range()` we are going to have a range of value starting from 0 and stoping at the number just before **the number you specify** 
- when using the loop for you do not need to initialize the variable, python takes care of initializing the variable 

## Codes example 
```python
i = 1 
while i != 0:
    print("meow")
```
In this case the loop will never end beacause the `i`variable is never going to reach 0.
```python
i = 1
while i != 1:
    print("meow")
    i = i - 1
```
In this case the loop will stop after displaying "meow" three times 

```python 
for _ in range(3):
     print("meow")
```
This code is written in pythonic, here the `_` is used to specify that the name of the variable has no importance, we jsut need to print three times "meow"

# Mistakes and fixes
- none
## Questions to ask
- none

## Problem Set progress
- [ ] camelCase
- [ ] Coke Machine
- [ ] Just setting up my twttr
- [ ] Vanity Plates
- [ ]Nutrition Facts 

## Location in the video

time : 0:41:58
chapter : len 