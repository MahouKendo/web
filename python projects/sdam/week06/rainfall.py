month_rain = [
    []
         ]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
number = []

for j in month:
    rain = int(input("Enter rainfall for " + j + ": "))
    number.append(rain)

arr_number = 0
for i in range(max(number)):
    month_rain.append([])
    arr_number = arr_number + 1
    for J in range(12):
        month_rain[arr_number].append(" ")

for J in range(12):
    month_rain[0].append("  ")

while number[0] > 0:
    number[0] = number[0] - 1
    month_rain[number[0]][0] = "x"
while number[1] > 0:
    number[1] = number[1] - 1
    month_rain[number[1]][1] = "x"
while number[2] > 0:
    number[2] = number[2] - 1
    month_rain[number[2]][2] = "x"
while number[3] > 0:
    number[3] = number[3] - 1
    month_rain[number[3]][3] = "x"
while number[4] > 0:
    number[4] = number[4] - 1
    month_rain[number[4]][4] = "x"
while number[5] > 0:
    number[5] = number[5] - 1
    month_rain[number[5]][5] = "x"
while number[6] > 0:
    number[6] = number[6] - 1
    month_rain[number[6]][6] = "x"
while number[7] > 0:
    number[7] = number[7] - 1
    month_rain[number[7]][7] = "x"
while number[8] > 0:
    number[8] = number[8] - 1
    month_rain[number[8]][8] = "x"
while number[9] > 0:
    number[9] = number[9] - 1
    month_rain[number[9]][9] = "x"
while number[10] > 0:
    number[10] = number[10] - 1
    month_rain[number[10]][10] = "x"
while number[11] > 0:
    number[11] = number[11] - 1
    month_rain[number[11]][11] = "x"

print("==================================================================")
for l in month:
    print(l, end="  ")
print()
for j in month_rain:
    for lst in j:
        print("", lst, end="   ")
    print()

