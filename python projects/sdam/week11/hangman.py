world_list = []
guess = input("Enter your word: ")
guess_list = list(guess)
guess_time = 0
for i in guess_list:
    if i == " ":
        world_list.append(" ")
    else:
        world_list.append("*")
while any(i == "*" for i in world_list):
    guess_time = guess_time + 1
    number = -1
    for i in world_list:
        print(i, end="")
    print()
    print("==============================")
    guess_word = input("Enter a word: ")
    for i, j in zip(world_list, guess_list):
        number = number + 1
        if j == guess_word:
            world_list[number] = guess_list[number]

print("===============================")
for i in world_list:
    print(i, end="")
print()
print("===============================")
print("The number of guess took you to win:", guess_time)
print("YOU WIN")


