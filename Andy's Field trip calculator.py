import time

#Task 1
Coach_cost = 550
Ticket_cost = 30
Names = []
Paid = 0
Not_paid = 0
Paid_or_not = []
Name_list_count = 0
Counter = 0
Total_students = 0
Valid_input = True

while Valid_input:
    try:
        Est_students = int(input("How many students are estimated to go on the field trip:     "))
        if Est_students > 45:
            print("45 is the maximum amount of students that can go on this trip")
        elif Est_students <= 0:
            print("Please enter a positive integer between 1 and 45")
        else:
            print("")
            Valid_input = False
    except ValueError:
        print("Please enter a positive, valid integer between 1 and 45.")

Est_discount = ((Est_students//11)*30)
Est_total_cost = Coach_cost + (Ticket_cost * Est_students) - Est_discount
Est_cost_per = Est_total_cost/Est_students
Est_students_2 = Est_students
Valid_input = True

print(f"{Est_total_cost}$ is the estimated total cost of the trip.")
print(f"{Est_cost_per}$ is the estimated cost per student.")
print("")
time.sleep(2)

#Task 2
while Valid_input == True:
    try:
        Addtional_students = int(input("How many additional students want to go?: "))
        if Addtional_students >= 0:
            print("")
            Valid_input = False
        else:
            print("please enter a positive integer")
    except ValueError:
        print("")

Est_students = Est_students + Addtional_students
Valid_input = True

while Est_students != 0:
    while Valid_input:
        Name = input(f"What is the name of student number {Est_students}:    ")
        try:
            if Name != "":
                Names.append(Name)
                Est_students = Est_students - 1
                Valid_input = False
            else:
                print("Please enter something")
                print("")
        except ValueError:
            print("Please input something.")
            print("")
    while Valid_input == False:
        try:
            Payment = input(f"Has {Name} paid? (answer 'paid' or 'not paid'):     ")
            if Payment == "paid":
                Paid_or_not.append(Payment)
                Paid = Paid + 1
                Total_students = Total_students + 1
                print("Thank you")
                print("")
                Valid_input = True
                time.sleep(1)
            elif Payment == "not paid":
                Paid_or_not.append(Payment)
                Not_paid = Not_paid + 1
                print("Thank you")
                print("")
                Valid_input = True
                time.sleep(1)
            else:
                print("Please answer with a 'paid' or 'not paid' ")
                print("")
        except ValueError:
            print("")


Counter = Total_students


try:
    Print_or_not = input("Would you like a printout to show the students who have paid and those who have not (answer Yes/No):  ")
    if Print_or_not == "Yes":
        while  Counter != 0:
            if Paid_or_not[Name_list_count] == "paid":
                print(f"{Names[Name_list_count]} has paid ${Est_cost_per}")
                Name_list_count = Name_list_count + 1
                Counter = Counter - 1
                time.sleep(1)
            else:
                print(f"{Names[Name_list_count]} has not paid")
                Name_list_count = Name_list_count + 1
                Counter = Counter - 1
                time.sleep(1)
    elif Print_or_not == "No":
        print("Okay then")
        print("")
        Counter = 0
        time.sleep(1)
    else:
        print("Please answer 'Yes' or 'No'")
except ValueError:
    print("")

print("")
time.sleep(0.5)
print("")
time.sleep(0.5)
print("")
time.sleep(2)

#Task 3
Valid_input = True

print(f"The total number of students going on this trip is: {Total_students}")

Discount = (Total_students//11)
Actual_costs = Coach_cost + ((Total_students - Discount)* 30)
Total_paid = Total_students * Est_cost_per
Current_account_balance = Total_paid - Actual_costs

print(f"The total cost charged was: {Actual_costs}.")
print(f"The total amount of money collected was: {Total_paid}")

if Actual_costs == Total_paid:
    print("You have broken even! Congradulations, You must have very good organization skills.")
elif Actual_costs <= Total_paid:
    print(f"You have made a profit.")
else: 
    print("You have made a loss.")
    print("")
time.sleep(0.5)
print("")
time.sleep(0.5)
print("")
time.sleep(2)
print(f"Your current account balance is: ${Current_account_balance}")