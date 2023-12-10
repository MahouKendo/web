player_1_board = [
    ["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "],
    [" 1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["Player 1 gameboard"]
]

player_2_board = [
    ["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "],
    [" 1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["Player 2 gameboard"]
]

player_1_battle_board = [
    ["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "],
    [" 1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["Player 1 gameboard"]
]

player_2_battle_board = [
    ["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "],
    [" 1 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 2 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 3 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 4 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    [" 5 ", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["Player 2 gameboard"]
]

def battle_board():
    for i, j in zip(player_1_battle_board, player_2_battle_board):
        for l in i:
            print(l, end="")
        print(end="                      ")
        for k in j:
            print(k, end="")
        print()


def semi_battle_board():
    for i, j in zip(player_1_battle_board, player_2_board):
        for l in i:
            print(l, end="")
        print(end="                      ")
        for k in j:
            print(k, end="")
        print()

def board():
    for i, j in zip(player_1_board, player_2_board):
        for l in i:
            print(l, end="")
        print(end="                      ")
        for k in j:
            print(k, end="")
        print()

def pl1_placing(ship):
    ship = ship + 3
    while True:
        while ship > 0:
            board()
            print("===================================================================================================")
            print("Player 1 turn")
            print("You have", ship, "ship left")
            try:
                pl1_row = int(input("player1 Row: "))
                pl1_column = int(input("player1 Column: "))
                direction = input("Direction(left, right, up or down): ")
                direction_check_column = pl1_column - 1
                direction_check_row = pl1_row - 1
                if 0 < pl1_row and 0 < pl1_column:
                    if player_1_board[pl1_row][pl1_column] != "[D]":
                        if direction == "left":
                            if direction_check_column > 0:
                                player_1_board[pl1_row][pl1_column] = "[D]"
                                player_1_board[pl1_row][direction_check_column] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        if direction == "right":
                            if direction_check_column != 4:
                                player_1_board[pl1_row][pl1_column] = "[D]"
                                player_1_board[pl1_row][pl1_column + 1] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        if direction == "down":
                            if direction_check_row != 4:
                                player_1_board[pl1_row][pl1_column] = "[D]"
                                player_1_board[pl1_row + 1][pl1_column] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        if direction == "up":
                            if direction_check_row > 0:
                                player_1_board[pl1_row][pl1_column] = "[D]"
                                player_1_board[direction_check_row][pl1_column] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        else:
                            print("Enter it right")
                    else:
                        print("You already pick this spot")
                else:
                    print("Out of range")
            except ValueError:
                print("Input number pl")
            except IndexError:
                print("Out of range")
        board()
        print("====================================================================")
        conform = input("Conform(y/n): ")
        if conform == "y":
            break
        elif conform == "n":
            for i in player_1_board:
                for j in range(len(i)):
                    if i[j] == "[D]":
                        i[j] = "[ ]"
            return pl1_placing(0)
        else:
            print("please conform it right")
            print("====================================================================")
            return pl1_placing(-3)

def pl2_placing(ship):
    ship = ship + 3
    while True:
        while ship > 0:
            semi_battle_board()
            print("===================================================================================================")
            print("Player 2 turn")
            print("You have", ship, "ship left")
            try:
                pl2_row = int(input("player2 Row: "))
                pl2_column = int(input("player2 Column: "))
                direction = input("Direction(left, right, up or down): ")
                direction_check_column = pl2_column - 1
                direction_check_row = pl2_row - 1
                if 0 < pl2_row and 0 < pl2_column:
                    if player_2_board[pl2_row][pl2_column] != "[D]":
                        if direction == "left":
                            if direction_check_column > 0:
                                player_2_board[pl2_row][pl2_column] = "[D]"
                                player_2_board[pl2_row][direction_check_column] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        if direction == "right":
                            player_2_board[pl2_row][pl2_column] = "[D]"
                            player_2_board[pl2_row][pl2_column + 1] = "[D]"
                            ship = ship - 1
                        if direction == "down":
                            player_2_board[pl2_row][pl2_column] = "[D]"
                            player_2_board[pl2_row + 1][pl2_column] = "[D]"
                            ship = ship - 1
                        if direction == "up":
                            if direction_check_row > 0:
                                player_2_board[pl2_row][pl2_column] = "[D]"
                                player_2_board[direction_check_row][pl2_column] = "[D]"
                                ship = ship - 1
                            else:
                                print("Out of range")
                        else:
                            print("Enter it right")
                    else:
                        print("You already pick this spot")
                else:
                    print("Out of range")
            except ValueError:
                print("Input number pl")
            except IndexError:
                print("Out of range")
        semi_battle_board()
        print("====================================================================")
        conform = input("Conform(y/n): ")
        if conform == "y":
            break
        elif conform == "n":
            for i in player_2_board:
                for j in range(len(i)):
                    if i[j] == "[D]":
                        i[j] = "[ ]"
            return pl2_placing(0)
        else:
            print("please conform it right")
            print("====================================================================")
            return pl2_placing(-3)

pl1_ship = 3
pl2_ship = 3
def battle_phase():
    global pl1_ship
    global pl2_ship
    def player1_turn():
        global pl2_ship
        while pl2_ship > 0:
            battle_board()
            print("====================================Player 1 turn============================")
            print("player2 have", pl2_ship, "ship left")
            try:
                pl1_row = abs(int(input("Player1 row: ")))
                pl1_column = abs(int(input("Player1 column: ")))
                if 0 < pl1_row and 0 < pl1_column:
                    pl1_guess = player_2_board[pl1_row][pl1_column]
                    if pl1_guess == "[D]":
                        player_2_battle_board[pl1_row][pl1_column] = "[H]"
                        player_2_board[pl1_row][pl1_column] = "0"
                        pl2_ship = pl2_ship - 0.5
                        print("Destroyer hit")
                        print("====================================================================")
                        return player1_turn()
                    elif pl1_guess == "0":
                        print("You already pick this spot")
                    else:
                        player_2_battle_board[pl1_row][pl1_column] = "[M]"
                        player_2_board[pl1_row][pl1_column] = "0"
                        print("You miss the target")
                        print("====================================================================")
                        break
            except ValueError:
                print("Input number pl")
            except IndexError:
                print("Out of range")

    def player2_turn():
        global pl1_ship
        while pl1_ship > 0:
            battle_board()
            print("====================================Player 2 turn============================")
            print("player1 have", pl1_ship, "ship left")
            try:
                pl2_row = abs(int(input("Player2 row: ")))
                pl2_column = abs(int(input("Player2 column: ")))
                pl2_guess = player_1_board[pl2_row][pl2_column]
                if 0 < pl2_row and 0 < pl2_column:
                    if pl2_guess == "[D]":
                        player_1_battle_board[pl2_row][pl2_column] = "[H]"
                        player_1_board[pl2_row][pl2_column] = "0"
                        pl1_ship = pl1_ship - 0.5
                        print("Destroyer hit")
                        print("====================================================================")
                        return player2_turn()
                    elif pl2_guess == "0":
                        print("You already pick this spot")
                    else:
                        player_1_battle_board[pl2_row][pl2_column] = "[M]"
                        player_1_board[pl2_row][pl2_column] = "0"
                        print("You miss the target")
                        print("====================================================================")
                        return battle_phase()
            except ValueError:
                print("Input number pl")
            except IndexError:
                print("Out of range")


    player1_turn()
    if pl2_ship > 0:
        player2_turn()
    if pl1_ship == 0:
        battle_board()
        print("\n")
        print("=====================================Player 2 win===============================")
    elif pl2_ship == 0:
        battle_board()
        print("\n")
        print("=====================================Player 1 win===============================")

def main():
    print("=====================Placing destroyer phase==============")
    pl1_placing(0)
    print("\n")
    pl2_placing(0)
    board()
    print("========================Placing phase end==================")
    print("\n")
    print("========================Battle phase ======================")
    battle_phase()
    print("\n")
    print("======================================GAME OVER=====================================")

main()