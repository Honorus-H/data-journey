"""#--- example 1 : SyntaxError---
print("hello world)

#---example 2 : ValueError---
x = int(input("what's x? "))
print(f"x is {x}")"""

#---example 3 : try ---
try: 
    x = int(input("what's x? "))
    print(f"x is {x}")
except ValueError :
    print("x is not an integer")

