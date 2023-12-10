number = []
for i in range(5):
    input_number = int(input("Number: "))
    number.append(input_number)
pos_sum = 0
neg_sum = 0
for i in number:
    if i > 0:
        pos_sum = pos_sum + i
    elif i < 0:
        neg_sum = neg_sum + i
print("Positive sum: " + str(pos_sum))
print("Negative sum: " + str(neg_sum))