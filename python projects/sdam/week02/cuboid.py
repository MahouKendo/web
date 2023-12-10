width = int(input("Width: "))
height = int(input("Height: "))
length = int(input("Length: "))
volume = width * height * length
area = 2 * height * length + 2 * height * width + 2 * length * width
print("Surface area: " + str(area))
print("Volume:" + str(volume))