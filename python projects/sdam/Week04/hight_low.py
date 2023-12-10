import random
number = [1, 11, 12, 13]
word = ["Ace", "Jack", "Queen", "King"]

number_random = random.randint(1, 13)
for i, j in zip(number, word):
    if number_random == i:
        print(j)
else:
    print(number_random)

number_random_2 = random.randint(1, 13)
choice = input("Higher or Lower: ")
if choice.capitalize() == "Higher" or choice.capitalize() == "Lower":
    print("Deals")
    print(number_random_2)
    if choice.capitalize() == "Higher":
        if number_random_2 > number_random:
            print("You win")
        else:
            print("You lose")
    if choice.capitalize() == "Lower":
        if number_random_2 < number_random:
            print("You win")
        else:
            print("You lose")
else:
    print("Incorrect")
