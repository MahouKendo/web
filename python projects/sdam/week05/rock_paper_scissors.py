import random
def game(player_total_point, computer_total_point):
    while True:
        computer_pick = random.randint(1, 3)
        if computer_pick == 1:
            computer_pick = "Rock"
        elif computer_pick == 2:
            computer_pick = "Scissors"
        else:
            computer_pick = "Paper"
        print("computer point: ", computer_total_point)
        print("Player point: ", player_total_point)
        player_choice = input("Rock, paper or scissors: ")
        print("Computer choice: ", computer_pick)
        if player_choice.capitalize() == "Rock" and computer_pick == "Rock":
            print("Draw")
            print("=======================================")
        if player_choice.capitalize() == "Paper" and computer_pick == "Paper":
            print("Draw")
            print("=======================================")
        if player_choice.capitalize() == "Scissors" and computer_pick == "Scissors":
            print("Draw")
            print("=======================================")
        if player_choice.capitalize() == "Rock" and computer_pick == "Paper":
            print("You lose")
            print("=======================================")
            computer_total_point = computer_total_point + 1
        if player_choice.capitalize() == "Scissors" and computer_pick == "Rock":
            print("You lose")
            print("=======================================")
            computer_total_point = computer_total_point + 1
        if player_choice.capitalize() == "Scissors" and computer_pick == "Paper":
            print("You win")
            print("=======================================")
            player_total_point = player_total_point + 1
        if player_choice.capitalize() == "Paper" and computer_pick == "Scissors":
            print("You lose")
            print("=======================================")
            computer_total_point = computer_total_point + 1
        if player_choice.capitalize() == "Rock" and computer_pick == "Scissors":
            print("You win")
            print("=======================================")
            player_total_point = player_total_point + 1
        if player_choice.capitalize() == "Paper" and computer_pick == "Rock":
            print("You win")
            print("=======================================")
            player_total_point = player_total_point + 1
        if computer_total_point == 0:
            print("computer need 3 more point to win")
        elif computer_total_point == 1:
            print("computer need 2 more point to win")
        elif computer_total_point == 2:
            print("computer need 1 more point to win")
        elif computer_total_point == 3:
            print("You lose the game")
            break
        if player_total_point == 0:
            print("You need 3 more point to win")
            print("=======================================")
        elif player_total_point == 1:
            print("You need 2 more point to win")
            print("=======================================")
        elif player_total_point == 2:
            print("You need 1 more point to win")
            print("=======================================")
        elif player_total_point == 3:
            print("You win the game")
            break
        return game(player_total_point, computer_total_point)
game(0, 0)
