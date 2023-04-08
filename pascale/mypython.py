calc_to_minutes = 24 * 60

def toMinutes():
    print("This application converts days to minutes.")
    
    while True:
        user_input = input("Enter the number of days you want to convert to minutes and hit the 'Enter' button: \n")
        if user_input == "quit":
            break
        else:
            try:
                no_of_minutes = int(user_input) * calc_to_minutes
                print(f"There are {no_of_minutes} minutes in {user_input} days")
            except ValueError:
                print("You made an invalid entry. Please try again.")
        
toMinutes()
