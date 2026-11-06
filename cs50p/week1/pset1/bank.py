"""This program gives the amount you owe based on the way you greeted"""

x= input("greetting: ")
if "hello" in x.lower():
    print("$0")
elif x.strip().lower()[0] =="h":
    print("$20")
else:
    print("$100")