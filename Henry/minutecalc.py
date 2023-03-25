#Importing color library

import colorama
from colorama import Fore, Style

#Variable for the value of minutes in 1 day

minDay = 24 * 60

#Introduction Script

print("This application converts days to minutes.")
print("Type 'quit' to exit")

#Function for Asking for the amount of days and returning the number of minutes in a day
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
