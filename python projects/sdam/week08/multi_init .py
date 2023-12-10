end_list = []
space = input("Enter your full name: ").split(" ")
time = len(space)
number_2 = 0
for i in space:
    if "-" in i:
        number = 0
        name_item = i.split("-")
        temp_list = []
        while number < len(name_item):
            temp_list.append(name_item[number][0])
            number = number + 1
        item = "-".join(temp_list)
        end_list.append(item)
        number_2 = number_2 + 1
    else:
        end_list.append(space[number_2][0])
        number_2 = number_2 + 1
output = ".".join(end_list)
print("Your shorten name are:", output)

