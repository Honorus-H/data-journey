"""This program permet to give the calories of a fruit """

def main():
   x = input("Calories: ")
   if calories(x) != None:
      print(f"Calories: {calories(x)}")
   else:
       print("")



def calories(word):
    fruits={"Apple":130,
          "Avocado":50,
           "Banana":110,
            "Cantaloupe":50,
            "Grapefruit":60,
            "Grapes":90,
            "Honeydew Melon":50,
            "Kiwifruit":90,
            "Lemon":15,
            "Lime":20,
            "Nectarine":60,
            "Pear":100,
            "Pineapple":50,
            "Plums":70,
            "Strawberries":50,
            "Sweet Cherries":100,
            "Tangerine":50,
            "Watermelon":80}
    for fruit in fruits:
        if word.strip().lower() == fruit.lower():
            return fruits[fruit]

main()
