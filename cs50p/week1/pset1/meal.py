"""a function that the time in string  in input and output if this time is in a meal time """

def main():
    x = input("what time is it? ")
    x = convert(x)

    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):

    h, m = time.strip("a.m.").strip("p.m.").split(":")
    h = int(h)
    m = int(m)
    if "p.m." in time and 0 <= h <= 12:
        return ((12+h)+(round(m/6,2)/10))
    else:
        return(h+(round(m/6,2)/10))


if __name__ == "__main__":
    main()
