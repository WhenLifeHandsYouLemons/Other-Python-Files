total_cost_of_coach = 550
entry_cost = 30

valid_input = True

while valid_input:
    try:
        no_of_people = int(input("How many students are going on this trip? "))
        if no_of_people <= 0:
            print("Please input a valid, positive number")
        else:
            valid_input = False
    except ValueError:
        print("Please input a valid number")

total_cost = (no_of_people * entry_cost) + total_cost_of_coach
print(f"The total cost of the trip will be ${total_cost}")