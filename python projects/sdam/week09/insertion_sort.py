number_list = [1, 5, 3, 8, 0]
def sorting(number_list):
    for i in range(1, len(number_list)):
        key = number_list[i]
        j = i - 1
        while j >= 0 and key > number_list[j]:
            number_list[j+1] = number_list[j]
            j -= 1
        number_list[j+1] = key
sorting(number_list)
print(number_list)