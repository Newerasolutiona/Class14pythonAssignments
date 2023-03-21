import colorama
from colorama import Fore, Style

minDay = 24 * 60

print("This application converts days to minutes.")
print("Type 'quit' to exit")


def toMinutes():
    try:
        no_of_minutes = int(daycount) * minDay
        print(f"There are {no_of_minutes} minutes in {daycount} days.")
    except:
        print(Fore.RED + "PLEASE INPUT INTEGERS ONLY" + Style.RESET_ALL)
while True:
    print()
    daycount = input("Enter the number of days: \n")
    if daycount == "quit":
        break
    toMinutes()
