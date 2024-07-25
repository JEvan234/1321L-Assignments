#color distance; get imports
import math

print()
#get first color
print("First color")
firstcolor_R = int(input("R: "))
firstcolor_G = int(input("G: "))
firstcolor_B = int(input("B: "))
print()
#Get second color
print("Second color")
secondcolor_R = int(input("R: "))
secondcolor_G = int(input("G: "))
secondcolor_B = int(input("B: "))
print()
#Do calculations
red = float((secondcolor_R - firstcolor_R) * (secondcolor_R - firstcolor_R))
blue = float((secondcolor_B - firstcolor_B) * (secondcolor_B - firstcolor_B))
green = float((secondcolor_G - firstcolor_G) * (secondcolor_G - firstcolor_G))\
#squareroot
distance = math.sqrt(red + blue + green)
print("Color Distance: " + str(distance))