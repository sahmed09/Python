import datetime

clients = {1: "Shihab", 2: "Ahmed", 3: "Apu"}
menu = {1: "Diet", 2: "Exercise"}


def get_date():
    return datetime.datetime.now()


try:
    for key, value in clients.items():
        print("Press", key, "for", value)
    client_choice = int(input("Select Client Name: "))

    print("Selected Client : ", clients[client_choice] + "\n")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    work_choice = int(input("Select What you want to do: "))
    print()

    if work_choice is 1:
        for key, value in menu.items():
            print("Press", key, "for", value)
        log_choice = int(input("Select What you want to log: "))

        f = open(clients[client_choice] + "_" + menu[log_choice] + ".txt", "a")
        print("\nEnter to", menu[log_choice], ": ")
        myText = input()
        f.write("[" + str(get_date()) + "]: " + myText + "\n")
        f.close()
        print("\nSuccessfully logged data")

    elif work_choice is 2:
        for key, value in menu.items():
            print("Press", key, "to retrieve", value)
        retrieve_choice = int(input("Select What you want to retrieve: "))

        print("\n" + clients[client_choice] + "'s", menu[retrieve_choice], "report: ")

        f = open(clients[client_choice] + "_" + menu[retrieve_choice] + ".txt", "rt")
        contents = f.read()
        print(contents)
        f.close()

    else:
        print("\nInvalid Input")

except Exception as e:
    print("\nInvalid Input")
