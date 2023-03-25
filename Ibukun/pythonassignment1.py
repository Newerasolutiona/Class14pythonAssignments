minutes_in_1day = 1440


def minutes():
    print("This app tells us how many minutes are in a day or days")
    print()
    print("NOTE!!! Please type quit to exit this calculator now!")
    print()
    while True:
        no_of_days = input("Please enter the number of days:\n")
        if no_of_days == "quit":
            break
        try:
            no_of_minutes = int(no_of_days) * minutes_in_1day
            print(f"There are", no_of_minutes, "minutes in", no_of_days, "days")
        except ValueError:
            print("Invalid entry, please try again")


minutes()
