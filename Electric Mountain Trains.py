"""
For IGCSE Computer Science course & IGCSE Computer Science Exam
Made by - Sooraj Sannabhadti
"""

# TASK 1
ticket_price = 25.00
seats_per_coach = 80
discount = 10

# Arrays and variables for up trains
train_times_per_up_train = ["09:00", "11:00", "13:00", "15:00"]
coaches_per_up_train = [6, 6, 6, 6]
total_seats_per_up_train = [480, 480, 480, 480]
passengers_per_up_train = [0, 0, 0, 0]
money_per_up_train = [0, 0, 0, 0]
available_seats_per_up_train = [(total_seats_per_up_train[0] - passengers_per_up_train[0]), (total_seats_per_up_train[1] - passengers_per_up_train[1]), (total_seats_per_up_train[2] - passengers_per_up_train[2]), (total_seats_per_up_train[3] - passengers_per_up_train[3])]

# Arrays and variables for down trains
train_times_per_down_train = ["10:00", "12:00", "14:00", "16:00"]
coaches_per_down_train = [6, 6, 6, 8]
total_seats_per_down_train = [480, 480, 480, 640]
passengers_per_down_train = [0, 0, 0, 0]
money_per_down_train = [0, 0, 0, 0]
available_seats_per_down_train = [(total_seats_per_down_train[0] - passengers_per_down_train[0]), (total_seats_per_down_train[1] - passengers_per_down_train[1]), (total_seats_per_down_train[2] - passengers_per_down_train[2]), (total_seats_per_down_train[3] - passengers_per_down_train[3])]

# Prints the times and seats available per train
def screen_display():
    print("")
    print("SCREEN DISPLAY")
    print("--------------------------------------------------------------")
    print("Departure times	        Seats   |	Return times	Seats")
    print(f"     {train_times_per_up_train[0]}               {available_seats_per_up_train[0]}	|	    {train_times_per_down_train[0]}        {available_seats_per_down_train[0]}")
    print(f"     {train_times_per_up_train[1]}               {available_seats_per_up_train[1]}	|	    {train_times_per_down_train[1]}        {available_seats_per_down_train[1]}")
    print(f"     {train_times_per_up_train[2]}               {available_seats_per_up_train[2]}	|	    {train_times_per_down_train[2]}        {available_seats_per_down_train[2]}")
    print(f"     {train_times_per_up_train[3]}               {available_seats_per_up_train[3]}	|	    {train_times_per_down_train[3]}        {available_seats_per_down_train[3]}")
    print("--------------------------------------------------------------")
    print("")

screen_display()

# TASK 2

valid_input = False
# Start a loop until the user enters a valid input
while valid_input == False:
    print("")

    # Ask which up train time and number of people
    chosen_up_train_time = input("What time do you want to go up the mountain? ")
    number_of_up_train_people = input("How many people are going on this train? ")

    # Try to convert the number_of_up_train_people input into an integer
    try:
        number_of_up_train_people = int(number_of_up_train_people)

        # Check if the train time input is one of these
        if chosen_up_train_time == "09:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[0]:
                chosen_up_train_time = 0
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[0]}")
        elif chosen_up_train_time == "11:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[1]:
                chosen_up_train_time = 1
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[1]}")
        elif chosen_up_train_time == "13:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[2]:
                chosen_up_train_time = 2
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[2]}")
        elif chosen_up_train_time == "15:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[3]:
                chosen_up_train_time = 3
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[3]}")
        else:
            print("Please input a valid time shown on the screen display.")
    except:
    # except ValueError or TypeError:
        print("Please input a valid number. eg: 2")

    # Check if discount is possible
    if number_of_up_train_people >= 10:
        number_of_tickets = number_of_up_train_people // 10

    # Calculates total price for going up the mountain
    price = ticket_price * number_of_tickets

    # Adds the current stored value and the inputted value
    total_number_of_people = number_of_up_train_people + passengers_per_up_train[chosen_up_train_time]

    # Removes the old up train values
    passengers_per_up_train.pop(chosen_up_train_time)
    available_seats_per_up_train.pop(chosen_up_train_time)

    # Adds the new up train values in the same place
    passengers_per_up_train.insert(chosen_up_train_time, total_number_of_people)
    available_seats_per_up_train.insert(chosen_up_train_time, (total_seats_per_up_train[chosen_up_train_time] - passengers_per_up_train[chosen_up_train_time]))




    print("")

    # Ask which train time and number of people
    chosen_up_train_time = input("What time do you want to go up the mountain? ")
    number_of_up_train_people = input("How many people are going on this train? ")

    # Try to convert the number_of_up_train_people input into an integer
    try:
        number_of_up_train_people = int(number_of_up_train_people)

        # Check if the train time input is one of these
        if chosen_up_train_time == "09:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[0]:
                chosen_up_train_time = 0
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[0]}")
        elif chosen_up_train_time == "11:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[1]:
                chosen_up_train_time = 1
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[1]}")
        elif chosen_up_train_time == "13:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[2]:
                chosen_up_train_time = 2
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[2]}")
        elif chosen_up_train_time == "15:00":
            # Check if the number of people is more than the seats available for the chosen train
            if number_of_up_train_people <= available_seats_per_up_train[3]:
                chosen_up_train_time = 3
                valid_input = True
            else:
                print(f"Please input a number less than {available_seats_per_up_train[3]}")
        else:
            print("Please input a valid time shown on the screen display.")
    except:
    # except ValueError or TypeError:
        print("Please input a valid number. eg: 2")






# Prints the times and seats available per train
screen_display()



"""
TEST DATA

09:00
5

The result should be the 09:00 train should have only 470 seats left.
"""