width_input = int(input("Enter your width: "))
if 2 <= width_input <= 40:
    for i in range(1, width_input+1):
        print(" "*(width_input - i), "* "*i)
    for i in range(width_input - 1, 0, -1):
        print(" "*(width_input - i), "* "*i)
else:
    print("Out of range")