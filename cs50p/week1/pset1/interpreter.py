"""This program interprets an expression into the equation corresponding and give the result """

mot= input("Expression: ")
x, y, z = mot.split()
x= int(x)
z= int(z)
if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(round(x/z,1))