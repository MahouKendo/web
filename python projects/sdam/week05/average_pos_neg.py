list_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos_total = 0
neg_total = 0
pos_number = 0
neg_number = 0
for i in range(len(list_number)):
    list_number[i]= int(input("enter nums: "))
    if list_number[i] > 0:
        pos_total = pos_total + list_number[i]
        pos_number = pos_number + 1
        pos_average = pos_total / pos_number
    elif list_number[i] < 0:
        neg_total = neg_total + list_number[i]
        neg_number = neg_number + 1
        neg_average = neg_total / neg_number
if pos_total != 0:
    print("Positive total: ",pos_total)
    print("Positive average: ",pos_average)
else:
    print("There no positive number")
if neg_total != 0:
    print("Negative total: ",neg_total)
    print("Negative average: ",neg_average)
else:
    print("There no negative number")