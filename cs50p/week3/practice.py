"""#--- example 1 : SyntaxError---
print("hello world)

#---example 2 : ValueError---
x = int(input("what's x? "))
print(f"x is {x}")"""

#---example 3 : try and except---
try: 
    x = int(input("what's x? "))
    print(f"x is {x}")
except ValueError :
    print("x is not an integer")

#--- example 4 : NameError ---
try: 
    x = int(input("what's x? "))
except ValueError :
    print("x is not an integer")

print(f"x is {x}")
#--- example 5 : using of else---
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#--- example 6 : using loop with the code---

while True:
    try :
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

# --- example 7 : using fonction---
def main(): 
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print(" x ix not an integer")
        else:
            break
    return x

main()

#--- example 8 : imrpoving the code ---
def main(): 
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print(" x ix not an integer")
        else:
            return x
main()

#----example 9 : improving the code ---
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            print("x is not an integer")

main()

#--- example 10 : using pass ---
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
           pass

main()

# ---example 11 : improving the code ---
def main():
    x = get_int("what's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass

main()