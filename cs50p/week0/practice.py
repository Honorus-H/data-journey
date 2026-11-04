#---example1 : hello world!---
print("hello world!")

#---example2: using variables&input---
name = input("what's your name?")
print("hello, ")
print(name)

#---example 3: improving the code---
name = input("what's your name? ")
print("hello, " + name)

#---example 4 :improving the code---
name= input("what's your name? ")
print("hello,",name)

#---example 5: using end parameters in the print function---
name = input("what's your name?")
print("hello, ", end="")
print(name)

#---example 6: using sep parameters in the print function---
name=input("what's your name?")
print("hello, ", name, sep="")

#---example 7: quotation---
print("what's up my \"freind\"")
print('hello "friend"')

#---example 8: using f-string---
name=input("what's your name?")
print(f"hello, {name}")

#---example 9: using method---
name =input("what's your name")
name=name.strip()
name= name.capitalize()
print(f"hello, {name}")

#---example 10 :improving the using of method  ---
name=input("what's your name? ")
name= name.strip().title()
print(f"hello, {name}")

#---example 11: improving the using of method(next)---
name= input("what's your name? ").strip().title()
print(f"hello, {name}")


#---example 12: separating string inn multiples string with split
name= input("what's your name?").strip().title()
first, last=name.split(" ")
print(f"hello, {first}", end=" ")
print(f"is your last name {last}?")

#---example 13 : using of int, calculator---
x = 1 
y = 2
z = x + y
print(z)

#---example 14: calculator with input---
x = input("what's x ?? ")
y = input("what's y ?? ")
z = int(x)+ int(z)
print(z)

#---examle 15 : improving my calculator 
x = int(input("what's x ?"))
y = int(input("what's y ?"))
print(x+y)

#---example 16 : calculator with float 
x = float(input("what's x ? "))
y = float(input("what's y ? "))

print(x+y)

#---example 17: using of round()---
x = float(input("what's x ? "))
y = float(input("what's y ? "))

z = round(x + y)
print(z)

#---example 18 : using formated string to better read number---
x = float(input("what's x ?"))
y = float(input("what's y ? "))
z = (x+y)
print(f"{z:,}")

#---example 19 : float rounded division ---
x = float(input("what's x ? "))
y = float(input("what's y ? "))
z = round(x/y,2)

#---example 20: f-string rounded division---

x= float(input("what's x ? "))
y = float(input("wat's y ? "))
z = x/y
print(f"{z:.2f}")

#---example 21 : creation of function with def---
def hello():
    print("hello")

name= input("what's your name ?")
hello()
print(name)

#---example 22 : creation of function with one parameters ---
def hello(to):
    print("hello",to)
name = input("what's your name ?")
hello(name)

#---example 23 : creatiion of fucntion with a default value set to parameters
def hello(to = "world"):
    print("hello", to)

hello()
name = input("what's yout name? ")
hello(name)

#---example 24 : separating the code in function ---
def main():
    name = input("what's your name ?")
    hello(name)

def hello(to ="world"):
    print("hello", to)
main()

#---example 25 using: return in a fucntion ---
def main():
    x = int(input("what's x ? "))
    print("x squared is :", square(x))

def square(y):
    return y*y
