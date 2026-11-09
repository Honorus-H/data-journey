"""#--- example 1: first use of while---
i = 1
while i != 1:
    print("meow")
    i = i - 1

#--- example 2 : other way to use while---
i = 0 
while i < 3:
     print("meow")
     i = i + 1

#--- example 3: increment---
i = 0 
while i < 3:
     print("meow")
     i +=1

#--- example 4 : using for loop---

for i in [0, 1, 2]:
     print(" meow")

#--- example 5 : using range---
for i in range(3):
     print("meow")

#--- example 6 : using range pythonic variable version ---
for _ in range(3):
     print("meow")

#--- example 7 : other way to print "meow" times  
print("meow"*3)

#--- example 8 : improving the code---
print("meow\n"*3)

#---example 9 : improving the code---
print("meow\n"*3, end="")

#--- example 10 : asking for a number---
while True:
    n = int(input("what's n? "))
    if n < 0:
        continue
    else: 
        break

#--- example 11 : improving the code----
while True:
     n = int(input("what's n? "))
     if n > 0 :
          break 
for _ in range(3):
     print("meow")

#--- example 12 : improving the code---

def main():
     number = get_number()
     meow(number)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n
def meow(n):
    for _ in range(n):
        print("meow")

#--- example 13 : working with list---
students = ["Hermione", "Harry", "Ron"]
print(students[0])
print(students[1])
print(students[2])

#--- example 14 : improving the last code---
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)


#---example 15 : using of len---
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(students[i])

#--- example 16 : using dictionnary----
students={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#--- example 17 : improving the last code ---
students={
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
for student in students:
    print(student, students[student], sep = ", ")

#--- example 19 : list of dictionnary---
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
     {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier "},
     {"name":"Draco", "house":"Slytherin", "patronus":None}
]

#--- example 20 : displaying the content of the list of dictionnary---
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
     {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier "},
     {"name":"Draco", "house":"Slytherin", "patronus":None}
]
for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")


#---example 21 : Mario, print column---

def main ():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
        
        
main()


#--- exemple 22 : Mario , print column second verison ---

def main():
    print_column(3)

def print_column(height):
    print("#\n"*3, end="")

main()

#---example 23 : Mario, print row ---
def main():
    print_row(4)

def print_row(width):
    print("?"*width)

main()


#---- example 24 : Mario, print a square---

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
          for j in range(size):
               print("#", end="")
          print()

main()"""

#---example 25: Mario, print a square ---

def main():
    print_square(3)

def print_square(size):
     for i in range(size):
          print("#"*size)
main()