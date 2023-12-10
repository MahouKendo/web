feet = float(input("Feet: "))
inches = float(input("Inches: "))
inches_to_feet = inches / 12
cm = (feet + inches_to_feet) * 30.48
mm = cm * 10
m = cm / 100
km = m / 1000
print("Height in kilometres:", round(km, 6))
print("Height in metres:", round(m, 3))
print("Height in centimetres:", round(cm, 1))
print("Height in millimetres:", round(mm, 1))

