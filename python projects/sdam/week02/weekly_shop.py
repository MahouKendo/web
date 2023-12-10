item = ["Peach", "Bean", "Chicken pieces", "Socks", "Bottle of water"]
item_number = []
item_price = []

for i in item:
    print(i)
    number = float(input("How many: "))
    item_number.append(number)
    price = float(input("Price: "))
    item_price.append(price)

total_item = 0
for i in item_number:
    total_item = total_item + i
print("Total number of items purchased:", total_item)

full_cost = 0
for i, j in zip(item_number, item_price):
    full_cost = full_cost + i*j
print("Your weekly shop cost:", full_cost)


