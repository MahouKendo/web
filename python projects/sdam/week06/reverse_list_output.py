number_list = []
for i in range(5):
    number = int(input("Enter your number: "))
    number_list.append(number)
begin_num = -1
end_num = 0
time = int(len(number_list)/2)
for i in range(time):
    begin_num = begin_num + 1
    end_num = end_num - 1
    number_list[begin_num], number_list[end_num] = number_list[end_num], number_list[begin_num]
print("Your reverse list are:", number_list)