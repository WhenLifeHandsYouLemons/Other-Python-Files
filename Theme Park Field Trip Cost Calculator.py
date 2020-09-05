cost_of_coach = 550
entry_cost = 30
free_tickets = 0
name_list_count = 0
paid_list_count = 0
check_list_count = 0
profit_or_loss_text = ""
paid = 0

names_of_students = []
paid_or_not = []

valid_input = True

while valid_input:
    try:
        no_of_people = int(input("How many students are going on this trip? "))

        if no_of_people <= 0:
            print("Please input a valid, positive number")
            print("")
        else:
            valid_input = False
    except ValueError:
        print("Please input a number")
        print("")

if no_of_people >= 10:
    free_tickets = no_of_people // 10

cost_per_student = round(((cost_of_coach / (no_of_people - free_tickets)) + entry_cost), 2)
print("----------------------------------------")
print(f"The estimated cost per student will be ${cost_per_student}")
print("----------------------------------------")

while no_of_people != 0:
    name_of_person = input("What is the first name of the student? ")
    print("")

    if name_of_person.isalpha():
        names_of_students.append(name_of_person)
        no_of_people = no_of_people - 1

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
        print("Please type the first name of a student")
        print("")

valid_input = len(names_of_students)

print("----------------------------------------")

while valid_input != 0:
    print(f"{names_of_students[name_list_count]} has {paid_or_not[paid_list_count]} ${cost_per_student}")
    name_list_count = name_list_count + 1
    paid_list_count = paid_list_count + 1
    valid_input = valid_input - 1

cost_charged = cost_of_coach + (len(names_of_students) * entry_cost)

valid_input = len(paid_or_not)

while valid_input != check_list_count:
    if paid_or_not[check_list_count] == "paid":
        paid = paid + 1
        check_list_count = check_list_count + 1
    else:
        check_list_count = check_list_count + 1

money_collected = paid * cost_per_student
profit_or_loss = round(money_collected - cost_charged, 2)

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
