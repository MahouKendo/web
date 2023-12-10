adult = int(input("number of Adult: "))
child = int(input("number of child: "))
concessions = int(input("number of concessions(for over the age of 65): "))

if adult > 0:
    free_adult = int(child / 10)
    if free_adult >= 1:
        adult = adult - free_adult
    if adult < 0:
        adult = 0
    total = adult * 10.5 + child * 7.3 + concessions * 8.4
    if total > 100:
        total = total - (total / 100 * 10)
    print("Your total price are:  £", total)
    ship = input("Do you want to ship rhe ticket for  £2.34: ")
    if ship.capitalize() == "Yes":
        total = total + 2.34
        print("You total price with ship are:  £", total)
        print("Thank for you purchase")
    else:
        print("Thank for you purchase")
else:
    print("You need at least one adult to watch the movie")