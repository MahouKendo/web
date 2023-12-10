total_second = abs(int(input("The number of second: ")))
hours = int(total_second / 3600)
minutes = int((total_second - hours*3600) / 60)
second = total_second - hours*3600 - minutes*60
print("Hour:", hours)
print("Minutes:", minutes)
print("Seconds:", second)