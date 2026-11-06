#--- example 1 : basic comparison---
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x < y :
    print(" x is less than y")

#--- example 2 : more basics comparison---
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x < y :
    print("x is less than y")
if x > y :
    print("x is more than y")
if x == y :
    print("x is equal to y")

#---  example 4 : using elif to improv the syntax---
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x < y :
    print("x is less than y")
elif x > y :
    print("x is more than y ")
elif x == y :
    print("x is equal to y ")

#--- example 5 : using else to improv the syntax---
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x < y :
    print("x is less than y")
elif x > y :
    print("x is more than y ")
else :
    print("x is equal to y ")

#--- example 6 : using of or ----
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x < y or x > y :
    print("x is not equal to y ")
else :
    print("x is equal to y ")

#--- example 7 : using equal---
x = int(input("what's x ? "))
y = int(input("what's y ? "))
if x == y :
    print("x is equal to y ")
else :
    print("x is not equal to y")

#--- example 8 : using of and---
score = int(input("score: "))
if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70 :
    print("Grade: E")
else:
    print("grade: F")

#---example 9: improving the last code---
score = int(input("score: "))
if 90 <= score <=100:
    print("Grade A")
elif 80 <= score <= 90 :
    print("Grade B")
elif 70 <= score <= 80 :
    print("Grade C")
elif 60 <= score <= 70 :
    print("Grade D")
else:
    print("Grade F")

#--- example 10 : improving the last code---
score = int(input("score: "))
if score >= 90 :
    print("Grade A")
elif score >= 80 :
    print("Grade B")
elif score >= 70 :
    print("Grade C")
elif score >= 60 :
    print("Grade D")
else:
    print("Grade F")

#---example 11 : test with if---
score = int(input("score: "))
if score >= 90 :
    print("Grade A")
if score >= 80 :
    print("Grade B")
if score >= 70 :
    print("Grade C")
if score >= 60 :
    print("Grade D")

#---example 12 : parity---
x = int(input("what's x ? "))
if x % 2 == 0 :
    print("Even")
else:
    print("Odd")

#--- example 13 : improving the function---
def main():
    x = int(input("what's x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even (n):
    if n % 2 == 0 :
        return True 
    else:
        return False
main()

#--- example 14 : improving our code with pythonic---
def main():
    x = int(input("what's x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False 
main()

#---example 15 : improving our code with pythonic---
def main():
    x = int(input("what's x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 ==0
main()

#--- example 16 : using match---
name = input("what's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")

#--- example 17 : other syntax for the match---
name = input("what's your ? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _:
            print("who?")