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

