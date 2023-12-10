cost = float(input("Cost to produce each item: "))
sale = float(input("Sale price for each item: "))
fixed_cost = float(input("Fixed cost: "))

breakeven = fixed_cost / (sale - cost)
profit = sale - cost

print("Profit per item: ", float(profit))
print("Breakeven", float(breakeven),"items")