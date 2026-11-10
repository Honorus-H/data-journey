"""A program representing a machine selling bottle of Coco-cola for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents. """
due = 50
while due >0:
    x = int((input("insert coin: ")))
    if x in [25, 10, 5] and due - x ==0 :
        due -= x
        break
    elif x in [25, 10, 5]:
        print("Amount Due:",(due - x))
        due -= x
    else:
        print("Amount Due:", due)

print("Change Owed:", (0-due))
