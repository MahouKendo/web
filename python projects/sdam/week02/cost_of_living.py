item = ["Rent", "Gas", "Electricity", "Water", "Council tax"]
item_price = []

for i in item:
    price = abs(float(input(i + " payment per month: ")))
    item_price.append(price)

if all(i < 9999.99 for i in item_price):
    for i, j in zip(item_price, item):
        print(j + ":" + "£", i)
    full_cost = 0
    for i in item_price:
        full_cost = full_cost + i
    print("===============================")
    print("Total:" + "£", full_cost)
else:
    print("Error")