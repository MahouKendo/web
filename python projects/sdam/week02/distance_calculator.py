u = float(input("initial velocity metres per second: "))
t = float(input("time taken in second: "))
a = float(input("acceleration metres per second: "))

s = (u * t) + (a * t**2)/2

print("distance",s)