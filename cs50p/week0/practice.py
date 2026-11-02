#---example1 : hello world!---
print("hello world!")

#--- example2: using variables&input---
name = input("what's your name?")
print("hello, ")
print(name)

#---example 3: improving the code---
name = input("what's your name? ")
print("hello, " + name)

#--- example 4 :improving the code---
name= input("what's your name? ")
print("hello,",name)

#--- example 5: using end parameters in the print function---
name = input("what's your name?")
print("hello, ", end="")
print(name)

#--- example 6: using sep parameters in the print function---
name=input("what's your name?")
print("hello, ", name, sep="")

#--- example 7: quotation
print("what's up my \"freind\"")
print('hello "friend"')

#--- example 8: using f-string---
name=input("what's your name?")
print(f"hello, {name}")

#--- example 9: using method---
name =input("what's your name")
name=name.strip()
name= name.capitalize()
print(f"hello, {name}")

#--- example 10 :improving the using of method  ---
name=input("what's your name? ")
name= name.strip().title()
print(f"hello, {name}")

#--- example 11: improving the using of method(next)---
name= input("what's your name? ").strip().title()
print(f"hello, {name}")


#--- example 12: separating string inn multiples string with split
name= input("what's your name?").strip().title()
first, last=name.split(" ")
print(f"hello, {first}", end=" ")
print(f"is your last name {last}?")





