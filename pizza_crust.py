from math import pi

radius, crust = list(map(int, input().rstrip().split()))

cheese_area = pi*(radius-crust)**2
pizza_area = pi*radius**2

print((cheese_area/pizza_area)*100)