import math
wall_cover = 5.1
paint_diameter = 15
paint_height = 30
l_box = 60
w_box = 30
h_box = 35
dia_can = 15
h_can = 30

wall_1 = 40 * 3.4
wall_2 = 30 * 3.4
all_wall = (wall_1 * 2) + (wall_2 * 2)
paint_need = all_wall / wall_cover
result_1 = math.ceil(paint_need)

print("Number of cans need to paint wall:",result_1)

box = l_box * w_box * h_box
can = dia_can * h_can * 3.14
number_can = box / can
number_box = result_1 / number_can
result_2 = math.ceil(number_box)

print("NUmber of boxes need to pack the cans:",result_2)

spare_can = result_1 % number_can
result_3 = math.ceil(spare_can)

print("The spare cans that can't be boxed:",result_3)



