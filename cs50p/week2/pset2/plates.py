"""this program permets to verify a plate based on the rules:
All vanity plates must start with at least two letters.
vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a "0"
No periods, spaces, or punctuation marks are allowed."""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def check_length(word):
     return 2 <= len(word) <= 6

def start_with_two_letters(word):
    if word[0].lower() == word[0] or word[1].lower() == word[1]:
        return False
    return True

def only_letters_and_diggits(word):
    return word.isalnum()


def check_numbers(word):
    for i in range(len(word)):
        if word[i].isdigit():
            if word[i] == "0":
                return False
            return word[i:].isdigit()
    return True

def is_valid(s):
    return(check_length(s)and
           start_with_two_letters(s)and
           only_letters_and_diggits(s)and
           check_numbers(s))

main()
