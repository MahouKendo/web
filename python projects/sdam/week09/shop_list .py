item_list = []
price_list = []

for i in range(5):
    item = input("Item: ")
    item_list.append(item)
    price = int(input("Price: "))
    price_list.append(price)

for i, j in zip(range(len(item_list)), range(len(price_list))):
    for l, k in zip(range(i+1, len(item_list)), range(j+1, len(price_list))):
        if price_list[j] > price_list[k]:
            item_list[i], item_list[l] = item_list[l], item_list[i]
            price_list[j], price_list[k] = price_list[k], price_list[j]

for i, j in zip(item_list, price_list):
    print(i, j)


