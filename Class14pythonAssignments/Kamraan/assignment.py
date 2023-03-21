calc_to_minutes = 24 * 60

def toMinutes():
    print("This script will convert days to minutes")
    print("To exit this script, type quit.")
    while True:
        user_input = input("Enter the number of days \n")
        if user_input == "quit":
            break
        try:
            number_of_minutes = int(user_input) + calc_to_minutes
            print(f"There are {number_of_minutes} minutes in {user_input} days.")
        except ValueError:
            print("You've entered invalid response.")

toMinutes()
