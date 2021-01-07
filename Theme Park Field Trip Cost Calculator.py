"""
For IGCSE Computer Science course
Made by: Sooraj Sannabhadti
"""
import time

# Task 1
cost_of_coach = 550
entry_cost = 30
free_tickets = 0

valid_input = True
while valid_input:
    try:
        no_of_students = int(input("How many students are going on this trip? "))

        if no_of_students <= 0:
            print("Please input a valid, positive number between 1 and 45")
            print("")
        elif no_of_students > 45:
            print("The maximum number of students allowed on this trip is 45.")
            print("")
        else:
            valid_input = False
    except ValueError:
        print("Please input a number.")
        print("")

if no_of_students >= 11:
    free_tickets = no_of_students // 11

cost_of_coach_per_student = round((cost_of_coach / no_of_students), 2)
cost_of_entry_per_student = round(((entry_cost * (no_of_students - (free_tickets))) / no_of_students), 2)
cost_per_student = round((cost_of_coach_per_student + cost_of_entry_per_student), 2)

print("")
print("----------------------------------------")
print(f"The estimated cost of coach per student will be ${cost_of_coach_per_student}")
print(f"The estimated cost of entry per student will be ${cost_of_entry_per_student}")
print(f"The estimated cost per student will be ${cost_per_student}")
print("----------------------------------------")
print("")

# Task 3
time.sleep(2.5)
valid_input = True
while valid_input:
    try:
        no_of_students = int(input("How many students are STILL going on this trip? "))

        if no_of_students < 0:
            print("Please input a valid, positive number between 0 and 45")
            print("")
        elif no_of_students > 45:
            print("Sorry, the maximum number of students allowed on this trip is 45.")
            print("")
        else:
            print("")
            valid_input = False
    except ValueError:
        print("Please input a number.")
        print("")


# Task 2
name_list_count = 0
paid_list_count = 0
check_list_count = 0
profit_or_loss_text = ""
paid = 0

names_of_students = []
paid_or_not = []

while no_of_students != 0:
    name_of_person = input(f"What is the first name of the student number {no_of_students}? ")
    print("")

    if name_of_person != "":
        names_of_students.append(name_of_person)
        no_of_students = no_of_students - 1

        valid_input = True

        while valid_input:
            check_to_pay = input(f"Has {name_of_person} paid? (Input paid or not paid) ")

            if check_to_pay == "paid":
                paid_or_not.append(check_to_pay)

                print("")

                valid_input = False
            elif check_to_pay == "not paid":
                paid_or_not.append(check_to_pay)

                print("")

                valid_input = False
            else:
                print("Please input 'paid' or 'not paid'")
                print("")
    else:
        print("Please type the name of a student only.")
        print("")

valid_input = len(names_of_students)

print("----------------------------------------")
print("Receipt")
print("----------------------------------------")

while valid_input != 0:
    print(f"{names_of_students[name_list_count]} has {paid_or_not[paid_list_count]} ${cost_per_student}")
    name_list_count = name_list_count + 1
    paid_list_count = paid_list_count + 1
    valid_input = valid_input - 1

# Task 3
valid_input = len(paid_or_not)

while valid_input != check_list_count:
    if paid_or_not[check_list_count] == "paid":
        paid = paid + 1
        check_list_count = check_list_count + 1
    else:
        check_list_count = check_list_count + 1

if paid >= 11:
    free_tickets = paid // 11
    print(f"The free tickets are {free_tickets}, the paid are {paid}")
# cost_of_coach_per_student = round((cost_of_coach / paid), 2)
# cost_of_entry_per_student = round(((entry_cost * (paid - (free_tickets))) / paid), 2)
cost_charged = round((cost_of_coach + ((paid - free_tickets) * entry_cost)), 2)

money_collected = round((paid * cost_per_student), 2)
profit_or_loss = round((money_collected - cost_charged), 2)

if profit_or_loss > 0:
    profit_or_loss_text = "made a profit"
elif profit_or_loss < 0:
    profit_or_loss_text = "made a loss"
else:
    profit_or_loss_text = "broken even"

print("----------------------------------------")
print(f"The total money charged is ${cost_charged}")
print(f"The total money collected is ${money_collected}.")
print(f"The trip has {profit_or_loss_text} by ${profit_or_loss}.")
print("----------------------------------------")

"""
TEST DATA #1
15
20
a
paid
b
paid
c
paid
d
paid
e
paid
f
paid
f
paid
g
paid
h
paid
i
paid
j
paid
k
paid
l
paid
m
paid
n
paid
o
paid
p
paid
q
paid
r
paid
s
paid


TEST DATA #2
20
15
a
paid
b
paid
c
paid
d
paid
e
paid
f
paid
f
paid
g
paid
h
paid
i
paid
j
paid
k
paid
l
paid
m
paid
n
paid

"""
