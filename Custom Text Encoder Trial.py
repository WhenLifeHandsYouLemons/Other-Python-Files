import shutil

tries = 5

password = input("What is the password? ")
while tries != 0:
    if password == "password":
        print("Yay!")
    else:
        print("Wrong password!")
        tries = tries - 1


print("You have run out of tries! Please wait for __ minutes before continuing.")
