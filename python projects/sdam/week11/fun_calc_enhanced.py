def add(number1, number2):
    total = number1 + number2
    return total

def subtract(number1, number2):
    subtraction = number1 - number2
    return subtraction

def multiply(number1, number2):
    multiply = number1 * number2
    return multiply

def divide(number1, number2):
    divide = number1 / number2
    return divide

def remainder(number1, number2):
    remainder = number1 % number2
    return remainder

def main():
    try:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        choice = input("What you want to do: ")
        if choice == "add":
            print("Your result are:", add(number1, number2))
        elif choice == "subtract":
            print("Your result are:", subtract(number1, number2))
        elif choice == "multiply":
            print("Your result are:", multiply(number1, number2))
        elif choice == "divide":
            print("Your result are:", divide(number1, number2))
        elif choice == "remainder":
            print("Your result are:", remainder(number1, number2))
        else:
            print("Error")
    except ValueError:
        print("Put number pls")
main()