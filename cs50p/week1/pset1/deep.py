"""This program prints a YES no matter how you enter forty two """

x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if x.strip() =="42" or x.lower() =="forty two" or x =="forty-two" :
    print("YES")
else:
    print("NO")