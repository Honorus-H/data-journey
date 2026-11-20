"""This program ask the user for name of the meal he wants and then check the list, if the meal is in the list it adds the price of the meal to the total price, you press control-d to stop the program"""

menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
t = 0
while True:
    try:
        plat = input("Item: ").strip().title()
        if plat in menu:
            t += menu.get(plat)
            print(f"Total: ${t:.2f}")
        else:
            continue
    except EOFError:
        print("\n")
        break