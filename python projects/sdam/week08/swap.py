number_List = []
number = input("Enter two integers: ").split(" ")
print("Your two integers are", number[0], number [1])
temp = number[0]
number[0] = number[1]
number[1] = temp
number_List.append(number[0])
number_List.append(number[1])
print("Your enteries swapped:")
for i in number_List:
    print(i,  end=" ")

