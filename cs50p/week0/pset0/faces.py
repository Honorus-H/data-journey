"""This code permet us to convert the emoticones :) and :( into emojis ."""
def main():
    x = input()
    print(convert(x))

def convert(phrase):
    phrase = phrase.replace(":)","🙂")
    phrase = phrase.replace(":(","🙁")
    return phrase

main()
