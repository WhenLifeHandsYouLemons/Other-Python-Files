"""
For IGCSE Computer Science course & IGCSE Computer Science Exam
Made by - Sooraj Sannabhadti
"""

# TASK 1
ticket_price = 25.00
seats_per_coach = 80
discount = 10
up_train_price = 0
down_train_price = 0

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

# Checks if the train is full
def check_fill():
    i = 0
    while i != 4:
        if available_seats_per_up_train[i] == "Closed" or available_seats_per_up_train[i] <= 0:
            available_seats_per_up_train.pop(i)
            available_seats_per_up_train.insert(i, "Closed")
        i = i + 1

    i = 0
    while i != 4:
        if available_seats_per_down_train[i] == "Closed" or available_seats_per_down_train[i] <= 0:
            available_seats_per_down_train.pop(i)
            available_seats_per_down_train.insert(i, "Closed")
        i = i + 1

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
day_end = False

# Starts a loop until the day has ended
while day_end == False:
    # Resetting the variables
    total_free_tickets = 0
    total_price = 0
    up_train_price = 0
    down_train_price = 0

    print("")
    input("Do you want to start booking? Press 'Enter' to start. ")
    print("")

    # Start a loop until the user enters a valid input for up trains
    valid_input = False
    while valid_input == False:
        # Ask which up train time and number of people
        chosen_up_train_time = input("What time do you want to go up the mountain? ")
        number_of_up_train_people = input("How many people are going on this train? ")

        # Does this part if the first two inputs are "Day end"
        if chosen_up_train_time == "Day end" and number_of_up_train_people == "Day end":
            valid_input = True
            day_end = True
        # Skips this part if the first two inputs are "Day end"
        else:
            # Try to convert the number_of_up_train_people input into an integer
            try:
                number_of_up_train_people = int(number_of_up_train_people)
                # Check if the train time input is one of these
                if chosen_up_train_time == "09:00":
                    # Check that the chosen train has empty seats
                    if available_seats_per_up_train[0] != "Closed":
                        # Check if the number of people is more than the seats available for the chosen train
                        if number_of_up_train_people <= available_seats_per_up_train[0]:
                            chosen_up_train_time = 0
                            valid_input = True
                        else:
                            print(f"Please input a number less than or equal to {available_seats_per_up_train[0]}")
                    else:
                        print("")
                        print("The selected train is full. Please choose a different train time.")
                        print("")
                elif chosen_up_train_time == "11:00":
                    # Check that the chosen train has empty seats
                    if available_seats_per_up_train[1] != "Closed":
                        # Check if the number of people is more than the seats available for the chosen train
                        if number_of_up_train_people <= available_seats_per_up_train[1]:
                            chosen_up_train_time = 1
                            valid_input = True
                        else:
                            print(f"Please input a number less than or equal to {available_seats_per_up_train[1]}")
                    else:
                        print("")
                        print("The selected train is full. Please choose a different train time.")
                        print("")
                elif chosen_up_train_time == "13:00":
                    # Check that the chosen train has empty seats
                    if available_seats_per_up_train[2] != "Closed":
                        # Check if the number of people is more than the seats available for the chosen train
                        if number_of_up_train_people <= available_seats_per_up_train[2]:
                            chosen_up_train_time = 2
                            valid_input = True
                        else:
                            print(f"please input a number less than or equal to {available_seats_per_up_train[2]}")
                    else:
                        print("")
                        print("The selected train is full. Please choose a different train time.")
                        print("")
                elif chosen_up_train_time == "15:00":
                    # Check that the chosen train has empty seats
                    if available_seats_per_up_train[3] != "Closed":
                        # Check if the number of people is more than the seats available for the chosen train
                        if number_of_up_train_people <= available_seats_per_up_train[3]:
                            chosen_up_train_time = 3
                            valid_input = True
                        else:
                            print(f"please input a number less than or equal to {available_seats_per_up_train[3]}")
                    else:
                        print("")
                        print("The selected train is full. Please choose a different train time.")
                        print("")
                else:
                    print("Please input a valid time shown on the screen display.")
            except:
                print("Please input a valid number. eg: 2")

    # Skips this part if the first two inputs are "Day end"
    if day_end == False:
        # Saves the total number of tickets for later use
        total_number_of_tickets = number_of_up_train_people
        print(f"The total_number_of_tickets = {total_number_of_tickets}")

        # Check if discount is possible
        if number_of_up_train_people >= 10:
            number_of_tickets = number_of_up_train_people - (number_of_up_train_people // 10)
            total_free_tickets = number_of_up_train_people // 10
            print(f"The number_of_tickets = {number_of_tickets}")
            print(f"The total_free_tickets = {total_free_tickets}")
        else:
            number_of_tickets = number_of_up_train_people
            print(f"The number_of_tickets = {number_of_tickets}")

        # Calculates total price for going up the mountain
        up_train_price = ticket_price * number_of_tickets
        # Adds the current stored value and the inputted value
        total_number_of_people = number_of_up_train_people + passengers_per_up_train[chosen_up_train_time]
        total_money_per_chosen_train = up_train_price + money_per_up_train[chosen_up_train_time]
        # Removes the old up train values
        passengers_per_up_train.pop(chosen_up_train_time)
        available_seats_per_up_train.pop(chosen_up_train_time)
        money_per_up_train.pop(chosen_up_train_time)
        # Adds the new up train values in the same place
        passengers_per_up_train.insert(chosen_up_train_time, total_number_of_people)
        available_seats_per_up_train.insert(chosen_up_train_time, (total_seats_per_up_train[chosen_up_train_time] - passengers_per_up_train[chosen_up_train_time]))
        money_per_up_train.insert(chosen_up_train_time, total_money_per_chosen_train)

        valid_input = False
        # Start a loop until the user buys tickets for everyone who went up
        while valid_input == False:
            # Start a loop until the user enters a valid input for down trains
            while valid_input == False:
                print("")

                # Ask which down train time and number of people
                chosen_down_train_time = input("What time do you want to go down the mountain? ")
                number_of_down_train_people = input("How many people are going on this train? ")

                # Try to convert the number_of_down_train_people input into an integer
                try:
                    number_of_down_train_people = int(number_of_down_train_people)
                    # Check if the train time input is one of these
                    if chosen_down_train_time == "10:00":
                        # Check that the chosen train has empty seats
                        if available_seats_per_down_train[0] != "Closed":
                            # Check if the number of people is less than the seats available for the chosen train and less than the total going up
                            if number_of_down_train_people <= number_of_up_train_people and number_of_down_train_people <= total_seats_per_down_train[0]:
                                chosen_down_train_time = 0
                                valid_input = True
                            elif number_of_down_train_people > total_seats_per_down_train[0]:
                                print("There are not enough seats on this train, please choose a different train.")
                            else:
                                print(f"Please input a number less than or equal to {number_of_up_train_people}")
                        else:
                            print("")
                            print("The selected train is full. Please choose a different train time.")
                            print("")
                    elif chosen_down_train_time == "12:00":
                        # Check that the chosen train has empty seats
                        if available_seats_per_down_train[1] != "Closed":
                            # Check if the number of people is less than the seats available for the chosen train and less than the total going up
                            if number_of_down_train_people <= number_of_up_train_people and number_of_down_train_people <= total_seats_per_down_train[1]:
                                chosen_down_train_time = 1
                                valid_input = True
                            elif number_of_down_train_people > total_seats_per_down_train[1]:
                                print("There are not enough seats on this train, please choose a different train.")
                            else:
                                print(f"Please input a number less than or equal to {number_of_up_train_people}")
                        else:
                            print("")
                            print("The selected train is full. Please choose a different train time.")
                            print("")
                    elif chosen_down_train_time == "14:00":
                        # Check that the chosen train has empty seats
                        if available_seats_per_down_train[2] != "Closed":
                            # Check if the number of people is less than the seats available for the chosen train and less than the total going up
                            if number_of_down_train_people <= number_of_up_train_people and number_of_down_train_people <= total_seats_per_down_train[2]:
                                chosen_down_train_time = 2
                                valid_input = True
                            elif number_of_down_train_people > total_seats_per_down_train[2]:
                                print("There are not enough seats on this train, please choose a different train.")
                            else:
                                print(f"Please input a number less than or equal to {number_of_up_train_people}")
                        else:
                            print("")
                            print("The selected train is full. Please choose a different train time.")
                            print("")
                    elif chosen_down_train_time == "16:00":
                        # Check that the chosen train has empty seats
                        if available_seats_per_down_train[3] != "Closed":
                            # Check if the number of people is less than the seats available for the chosen train and less than the total going up
                            if number_of_down_train_people <= number_of_up_train_people and number_of_down_train_people <= total_seats_per_down_train[3]:
                                chosen_down_train_time = 3
                                valid_input = True
                            elif number_of_down_train_people > total_seats_per_down_train[3]:
                                print("There are not enough seats on this train, please choose a different train.")
                            else:
                                print(f"Please input a number less than or equal to {number_of_up_train_people}")
                        else:
                            print("")
                            print("The selected train is full. Please choose a different train time.")
                            print("")
                    else:
                        print("Please input a valid time shown on the screen display.")
                except:
                    print(f"Please input a valid number. eg: {number_of_up_train_people}")

            # Checks if everyone who goes up is buying a return ticket
            if number_of_down_train_people < number_of_up_train_people:
                number_of_up_train_people = number_of_up_train_people - number_of_down_train_people
                valid_input = False
                print("")
                print(f"Please buy extra tickets for {number_of_up_train_people} people.")

            # Saves the total number of tickets for later use
            total_number_of_tickets = number_of_down_train_people + total_number_of_tickets

            # Check if discount is possible
            if number_of_down_train_people >= 10:
                number_of_tickets = number_of_down_train_people - (number_of_down_train_people // 10)
                total_free_tickets = (number_of_down_train_people // 10) + total_free_tickets
                print(f"The number_of_tickets = {number_of_tickets}")
                print(f"The total_free_tickets = {total_free_tickets}")
            else:
                number_of_tickets = number_of_down_train_people
                print(f"The number_of_tickets = {number_of_tickets}")

            # Calculates current total price for going down the mountain
            down_train_price = (ticket_price * number_of_tickets) + down_train_price
            # Adds the current stored value and the inputted value
            total_number_of_people = number_of_down_train_people + passengers_per_down_train[chosen_down_train_time]
            total_money_per_chosen_train = down_train_price + money_per_down_train[chosen_down_train_time]
            # Removes the old up train values
            passengers_per_down_train.pop(chosen_down_train_time)
            available_seats_per_down_train.pop(chosen_down_train_time)
            money_per_down_train.pop(chosen_down_train_time)
            # Adds the new up train values in the same place
            passengers_per_down_train.insert(chosen_down_train_time, total_number_of_people)
            available_seats_per_down_train.insert(chosen_down_train_time, (total_seats_per_down_train[chosen_down_train_time] - passengers_per_down_train[chosen_down_train_time]))
            money_per_down_train.insert(chosen_down_train_time, total_money_per_chosen_train)

        # Calculates and prints the total price
        print(f"The up_train_price = {up_train_price}, down_train_price = {down_train_price}")
        total_price = round((up_train_price + down_train_price), 2)
        print("")
        print(f"------------------Receipt------------------")
        print(f"You've bought {total_number_of_tickets} tickets.")
        print(f"The cost of one ticket is ${ticket_price}0")
        print(f"You get {total_free_tickets} tickets free!")
        print(f"The total price of the tickets is ${total_price}0")
        print("-------------------------------------------")
        print("")
        input("Press 'Enter' to finish booking.")
        print("")

        # Check which trains are full and update the display
        check_fill()

        # Prints the times and seats available per train before the start of a new booking
        screen_display()


# Run this only if the first two inputs are 'Day end'
def end_day():
    # Calculate the total number of people and total money taken
    total_number_of_people_today = passengers_per_up_train[0] + passengers_per_up_train[1] + passengers_per_up_train[2] + passengers_per_up_train[3] + passengers_per_down_train[0] + passengers_per_down_train[1] + passengers_per_down_train[2] + passengers_per_down_train[3]
    total_amount_of_money_taken_today = money_per_up_train[0] + money_per_up_train[1] + money_per_up_train[2] + money_per_up_train[3] + money_per_down_train[0] + money_per_down_train[1] + money_per_down_train[2] + money_per_down_train[3]
    # Find out the train with the most passengers
    most_passengers_per_train_today = max(passengers_per_up_train)
    # If there are more people in a return train, it will do this
    if max(passengers_per_down_train) > most_passengers_per_train_today:
        # Find out the train with the most passengers
        most_passengers_per_train_today = max(passengers_per_down_train)

        # Starts a loop to find out which train time has the most passengers
        position_in_list = 0
        while position_in_list != 4:
            if most_passengers_per_train_today == passengers_per_down_train[position_in_list]:
                # Saves the train time to train_time_with_most_passengers to use later
                train_time_with_most_passengers = train_times_per_down_train[position_in_list]
            position_in_list = position_in_list + 1
    # If there are more people in a departure train, it will do this
    else:
        # Starts a loop to find out which train time has the most passengers
        position_in_list = 0
        while position_in_list != 4:
            if most_passengers_per_train_today == passengers_per_up_train[position_in_list]:
                # Saves the train time to train_time_with_most_passengers to use later
                train_time_with_most_passengers = train_times_per_up_train[position_in_list]
            position_in_list = position_in_list + 1

    print("")
    print("")
    print("TODAY'S TOTAL")
    print("")
    print("---------------------------------------------------------")
    print("Departure times      Passengers booked       Money taken")
    print(f"{train_times_per_up_train[0]}                {passengers_per_up_train[0]}                       {money_per_up_train[0]}")
    print(f"{train_times_per_up_train[1]}                {passengers_per_up_train[1]}                       {money_per_up_train[1]}")
    print(f"{train_times_per_up_train[2]}                {passengers_per_up_train[2]}                       {money_per_up_train[2]}")
    print(f"{train_times_per_up_train[3]}                {passengers_per_up_train[3]}                       {money_per_up_train[3]}")
    print("---------------------------------------------------------")
    print("Return times      Passengers booked       Money taken")
    print(f"{train_times_per_down_train[0]}             {passengers_per_down_train[0]}                       {money_per_down_train[0]}")
    print(f"{train_times_per_down_train[1]}             {passengers_per_down_train[1]}                       {money_per_down_train[1]}")
    print(f"{train_times_per_down_train[2]}             {passengers_per_down_train[2]}                       {money_per_down_train[2]}")
    print(f"{train_times_per_down_train[3]}             {passengers_per_down_train[3]}                       {money_per_down_train[3]}")
    print("---------------------------------------------------------")
    print(f"The total number of pasengers for today is {total_number_of_people_today}.")
    print(f"The total amount of money taken for today is ${total_amount_of_money_taken_today}0")
    print(f"The {train_time_with_most_passengers} train had the most pasengers today.")
    print("---------------------------------------------------------")

end_day()
