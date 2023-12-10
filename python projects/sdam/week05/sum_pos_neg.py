list_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos_total = 0
neg_total = 0
for i in range(len(list_number)):
    list_number[i]= int(input("enter nums: "))
    if list_number[i] > 0:
        pos_total = pos_total + list_number[i]
    elif list_number[i] < 0:
        neg_total = neg_total + list_number[i]
print("Negative total: ",neg_total)
print("Positive total: ",pos_total)
