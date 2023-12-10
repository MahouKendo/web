words_list = []
for i in range(5):
    words = input("Enter your words: ")
    words_list.append(words)
for i in range(len(words_list)):
    for j in range(i + 1, len(words_list)):
        if words_list[i] > words_list[j]:
            words_list[i], words_list[j] = words_list[j], words_list[i]
print(words_list)