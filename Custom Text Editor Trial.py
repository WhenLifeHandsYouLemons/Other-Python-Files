import shutil

filez = []

password = input("What is the password? ")
if password == "password":
    loop = True

while loop == True:
    task = input("What would like to do?    New    View    Write/Edit    Exit    : ")
    if task == "New":
        open("C:/Users/2005s/Documents/Notes/Note.sooraj", "w+")
        print("Created new note.")
    if task == "View":
        with open("C:/Users/2005s/Documents/Notes/Note.sooraj", "r") as f:
            content = f.read()
            lines = content.split(" /n ")
            showing = "\n".join(lines)
        print("\nViewing 'C:/Users/2005s/Documents/Notes/Note.sooraj'.")
        print("--------------------------------------------------")
        print(showing)
        print("--------------------------------------------------\n")
    if task == "Write" or task == "Edit":
        written = input("Write what you want to save\n\n")
        print("/n")
        with open("C:/Users/2005s/Documents/Notes/Note.sooraj", "w") as f:
            f.write(written)

        # filezfull = written.split()
        # print(filezfull)
        # for text in filezfull:
        #     word = text.split()
        #     print(word)
        #     for letter in word:
        #         filez.append(letter)
        # print(filez)
    if task == "Exit":
        loop = False
