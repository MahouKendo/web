import json

account_list = []


def new_account():
    username_position = -2
    repeated_time = len(account_list) / 2
    username_input = input("Enter your username: ")
    conform = input("Conform username(y,n): ")
    if conform.capitalize() == "Y":
        for i in range(int(repeated_time)):
            username_position = username_position + 2
            if username_input == account_list[username_position]:
                print("This account already exit")
                return new_account()
        print("--------------------------------------------")
        print("Password must be at least 8 character long")
        print("Password must not start or end with space")
        print("Password must not begin with a number")
    elif conform.capitalize() == "N":
        print("Returning................")
        return new_account()
    else:
        print("Please conform it right")
        return new_account()

    def password_checking():
        password_input = input("Enter your password: ")
        password_check = list(password_input)
        if len(password_check) < 8:
            print("Password must be at least 8 character long")
            return password_checking()
        elif password_check[0] == " " or password_check[-1] == " ":
            print("Password must not start or end with space")
            return password_checking()
        try:
            int(password_check[0])
            print("Password must not begin with a number")
            return password_checking()
        except ValueError:
            conform_pass = input("Please conform your password: ")
            if conform_pass == password_input:
                print("----------------------------------------")
                print("New account creating...................")
                print("Account created")
                return password_input
            else:
                print("Password not match")
                return password_checking()

    password = password_checking()
    account_list.append(username_input)
    account_list.append(password)
    with open("Account Management.json", "w") as file:
        json.dump(account_list, file)


def exiting_account(chance):
    print("You only got 3 chance of password log in with all user, on failing the 3rd attempt will lock you out")
    print("--------------------------------------------")
    while chance > 0 or chance != 4:
        username_position = -2
        repeated_time = len(account_list) / 2
        username_input = input("Enter your username(Quit to quit): ")
        if username_input.capitalize() == "Quit":
            chance = 5
            print("Returning.............")
            return chance
        conform = input("Conform username(y,n): ")
        if conform.capitalize() == "Y":
            for i in range(int(repeated_time)):
                username_position = username_position + 2
                if username_input == account_list[username_position]:
                    password_input = input("Enter your password: ")
                    if password_input == account_list[username_position + 1]:
                        print("Correct password")
                        chance = 4
                        return chance
                    else:
                        print("Wrong password")
                        print("------------------------------------")
                        chance = chance - 1
                        print("You have", chance, "chance left")
                        print("-------------------------------------")
                        return exiting_account(chance)
            print("User do not exit")
            return exiting_account(chance)
        elif conform.capitalize() == "N":
            print("Retuning.............")
            return exiting_account(chance)
        else:
            print("Please conform it right")
            print("----------------------------------")
            return exiting_account(chance)
    if chance == 0:
        print("Out of chance")
        print("-------------------------------------")
        return chance


def main():
    while True:

        with open("Account Management.json", "r") as file:
            account_list.clear()
            data = json.load(file)
            for i in data:
                account_list.append(i)
        user_choice = input("Chose 1 for new account, 2 for exiting account and 3 to quit: ")
        if user_choice == "1":
            new_account()
            return main()
        elif user_choice == "2":
            chance = exiting_account(3)
            if chance == 0:
                print("Lock out")
                break
            elif chance == 5:
                return main()
            else:
                print("Entering.............................")
                print("Welcome my boy")
                break
        elif user_choice == "3":
            print("Quiting.............................")
            break
        else:
            print("Pick either 1, 2 or 3 please")
            return main()


main()
