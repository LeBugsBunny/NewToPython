import math

height = input("Enter the cone height: ")
radius = input("Enter the cone radius: ")

height = int(height)
radius = int(radius)

def vol_cone():
    area_base = math.pi * (radius * radius)
    third_area_base = area_base / 3
    volume = third_area_base * height
    print(round(volume, 2))

vol_cone()