"""
For IGCSE Computer Science course
"""

import random

menu = ["French fries", "1/4 pound burger", "1/4 pound cheeseburger", "1/2 pound burger", "1/2 pound cheeseburger", "Medium pizza", "Medium pizza with extra toppings", "Large pizza", "Large pizza with extra toppings", "Garlic bread"]
prices = [2.00, 5.00, 5.55, 7.00, 7.50, 9.00, 11.00, 12.00, 14.50, 4.50]
item_codes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
current_order_codes = []
current_quantities = []
current_items = []
current_total_price_of_items = []
order_no_today = []
order_totals_today = []
current_price_of_items = []
finder = 0

def printing_menu():
    print("")
    print("------------------------------------------------------------")
    print(f"ITEM CODE         MENU                           PRICE")
    print("")
    print(f"    {item_codes[0]}        {menu[0]}                        ${prices[0]}")
    print(f"    {item_codes[1]}        {menu[1]}                    ${prices[1]}")
    print(f"    {item_codes[2]}        {menu[2]}              ${prices[2]}")
    print(f"    {item_codes[3]}        {menu[3]}                    ${prices[3]}")
    print(f"    {item_codes[4]}        {menu[4]}              ${prices[4]}")
    print(f"    {item_codes[5]}        {menu[5]}                        ${prices[5]}")
    print(f"    {item_codes[6]}        {menu[6]}    ${prices[6]}")
    print(f"    {item_codes[7]}        {menu[7]}                         ${prices[7]}")
    print(f"    {item_codes[8]}        {menu[8]}     ${prices[8]}")
    print(f"    {item_codes[9]}        {menu[9]}                        ${prices[9]}")
    print("------------------------------------------------------------")

def find_pos():
    if order_code == "A":
        finder = 0
    elif order_code == "B":
        finder = 1
    elif order_code == "C":
        finder = 2
    elif order_code == "D":
        finder = 3
    elif order_code == "E":
        finder = 4
    elif order_code == "F":
        finder = 5
    elif order_code == "G":
        finder = 6
    elif order_code == "H":
        finder = 7
    elif order_code == "I":
        finder = 8
    elif order_code == "J":
        finder = 9
    current_items.append(menu[finder])
    current_price_of_items.append(prices[finder])

def printing_receipt():
    list_no = 0
    order_total = sum(current_total_price_of_items)
    print("")
    print("------------------------------------------------------------")
    print(f"Your order number is: #{order_no}")
    print("")
    print("QUANTITY      PRICE        ITEMS")
    while list_no < len(current_order_codes):
        print(f"   {current_quantities[list_no]}          ${current_price_of_items[list_no]}         {current_items[list_no]}")
        list_no = list_no + 1
    print("              -------")
    print(f"Order total:  ${order_total}")

def total_calculation():
    i = 0
    while i < len(current_price_of_items):
        T = current_price_of_items[i] * current_quantities[i]
        current_total_price_of_items.append(T)
        i = i + 1

def quantity_input():
    type_no_order = True
    while type_no_order == True:
        print("")
        quantity = input(f"How many '{current_items[-1]}' would you like? Please type a number: ")
        if quantity.isnumeric():
            current_quantities.append(int(quantity))
            type_no_order = False

ordering = True
while ordering == True:
    printing_menu()

    type_order = True

    while type_order == True:
        print("")
        order_code = input("What do you want to buy? Type nothing to finish. Please type the item code in capitals: ")
        if order_code == "":
            total_calculation()
            type_order = False
        elif len(order_code) == 1 and order_code.isupper() and order_code <= "J":
            current_order_codes.append(order_code)
            find_pos()
            quantity_input()

    order_no = random.randint(100, 999)
    order_no_today.append(order_no)

    printing_receipt()

    ordering = False
