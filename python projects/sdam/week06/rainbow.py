number = [1, 2, 3, 4, 5, 6, 7]
colour = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
def main():
    while True:
        choice = int(input("Enter a number from 1 to 7 to display rainbow colour or -1 to quit: "))
        for i, j in zip(number, colour):
            if choice == i:
                print(j)
                return main()
        if choice == -1:
            print("Quitting program")
            break
        elif choice != all(i for i in number):
            print("Error")
            return main()

main()