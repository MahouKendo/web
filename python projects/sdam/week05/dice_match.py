import random

def dice():
    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("First dice:", dice_1)
        print("Second dice:", dice_2)
        if dice_1 == dice_2:
            print("Nice")
            break
        elif dice_1 != dice_2:
            print("Too bad")
            return dice()
        
dice()