def main():
    x = input("camelCase: ")
    print(camelCase(x))

def camelCase(mot):
    new=""
    for lettre in mot:
        if lettre == lettre.upper():
            new = new + "_" +lettre.lower()
        else:
            new = new + lettre 
    return new 

main()