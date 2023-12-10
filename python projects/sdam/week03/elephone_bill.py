number_of_minutes = int(input("Enter number of minutes: "))
call_charge = number_of_minutes * 15 / 100
VAT = call_charge / 100 * 20
total = call_charge + VAT
print("Number of minutes used:",number_of_minutes)
print("Basic call charge:", "£",call_charge)
print("VAT due:", "£", VAT)
print("Total bill:", "£", total)