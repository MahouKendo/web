def program():
    while True:
        reversed_num = 0
        user_choice = int(input("Enter an integer of at least 2 digits or -1 to quit: "))
        if user_choice == -1:
            print("Program end")
            break
        elif user_choice < 10 or user_choice > 10000000000:
            print("Your input is invalid, please try again")
            return program()
        else:
            while user_choice != 0:
                digit = user_choice % 10
                reversed_num = reversed_num * 10 + digit
                user_choice //= 10
            print("Your integer reversed is: ", reversed_num)
            return program()

program()