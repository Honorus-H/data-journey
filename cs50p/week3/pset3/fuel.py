"this code permet us to display the percentage of fuel based on the fraction given by the user"
def main():
    f = get_frac()
    if round(f*100) <= 1:
        print("E")
    elif round(f*100) >= 99:
        print("F")
    else:
        print(f"{round(f*100)}%")

def get_frac():
    while True:
        try:
            mot =input("Fraction: ")
            x, y = mot.strip().split("/")
            x = int(x)
            y = int(y)
            if x>y or x < 0:
                continue
            return x/y
        except (ValueError, ZeroDivisionError):
            pass

main()
