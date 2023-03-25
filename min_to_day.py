#!/usr/bin/python3
#A script to calculate the number of minutes in a number of days

min_in_day = 24 * 60


def calc_of_mins(num_of_days):
    if num_of_days > 0:
        return f"there are {num_of_days * min_in_day} minutes in {num_of_days} day"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"
    else:
        return "you entered an invalid number of days, please confirm your entry"

#for the input to be only numbers (int) and not strings or number less than zero
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        total_min = calc_of_mins(user_input_number)
        print(total_min)
    else:
        print("your input is not a valid number, please enter a valid number")


#for the calcution to run continuously until user types "exit"
user_input = ""
while user_input != "exit":
    user_input = input("pls add the number of days to convert to mins \n")
    validate_and_execute()

