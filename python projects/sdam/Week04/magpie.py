number = [1, 2, 3, 4, 5, 6, 7]
word = ["One for sorrow", "Two for joy", "Three for a girl", "Four for a boy", "Five for silver", "Six for gold", "Seven for secret never to be told"]

input_number = int(input("Number: "))
for i, j in zip(number, word):
    if i == input_number:
        print(j)
else:
    print("Not a permitted number")