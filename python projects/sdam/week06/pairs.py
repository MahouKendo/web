import random
card = [
    ["Jack", "Jack", "King", "King"],
    ["Jack", "Jack", "King", "King"],
    ["Queen", "Queen", "Ace", "Ace"],
    ["Queen", "Queen", "Ace", "Ace"]
]
shuffle = random.shuffle([random.shuffle(i) for i in card])
front = [
    [" ", "0", "1", "2", "3"],
    ["0", "*", "*", "*", "*"],
    ["1", "*", "*", "*", "*"],
    ["2", "*", "*", "*", "*"],
    ["3", "*", "*", "*", "*"]
]
def main(win_point):
    while win_point != 8:
        for i in front:
            for j in i:
                print(j, end=" ")
            print()
        try:
            choice_row = abs(int(input("Row 1: ")))
            choice_column = abs(int(input("Column 1: ")))
            choice_row_2 = abs(int(input("Row 2: ")))
            choice_column_2 = abs(int(input("Column 2: ")))
            card_1 = card[choice_row][choice_column]
            card_2 = card[choice_row_2][choice_column_2]
            if card_1 == card_2:
                if card_1 == card_2 == "0":
                    print("These card had already been picked")
                elif choice_row != choice_row_2 or choice_column != choice_column_2:
                    print("Card matched")
                    print("========================================================")
                    front[choice_row + 1][choice_column + 1] = "X"
                    front[choice_row_2 + 1][choice_column_2 + 1] = "X"
                    card[choice_row][choice_column] = "0"
                    card[choice_row_2][choice_column_2] = "0"
                    win_point = win_point + 1
                    return main(win_point)
                else:
                    print("No pick the same card")
                    print("========================================================")
            else:
                print("Try again")
                print("========================================================")
                return main(win_point)
        except ValueError:
            print("must input number from 0 to 3")
        except IndexError:
            print("must input number from 0 to 3")
    for i in front:
        for j in i:
            print(j, end=" ")
        print()
    print("You win")

main(0)

