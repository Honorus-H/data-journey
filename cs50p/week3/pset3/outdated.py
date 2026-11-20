"""a program which changes the formt of the date"""
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try :
        date =input("Date: ")
        month, day, year= date.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
        else:
            print(f"{year}-{month:02}-{day:02}")
            break

    except ValueError:
        try:
            month, day , year = date.strip().split()
            if (day.endswith(",")):
                day = day.replace(",", "")
                day=int(day)
                year = int(year)
                if (month in months) and (1 <= day <= 31):
                    print(f"{year}-{months.index(month)+1:02}-{day:02}")
                    break
        except ValueError:
            pass