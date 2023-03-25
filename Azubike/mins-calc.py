convt_to_mins = 24 * 60

def minToDays():
    print("This application converts minutes to day(s)")
    while True:
        user_input = input("Enter the number of day(s) \n")
        if user_input == "quit":
            break
        try:
            no_of_mins = int(user_input) * convt_to_mins
            print(f"There are {no_of_mins} minutes in {user_input} day(s)")
        except ValueError:
            print("You have made an invalid input")


minToDays()
