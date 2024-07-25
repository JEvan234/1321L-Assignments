#Square size assignment
size = int(input("Enter the size of the square: "))
#check for positive integer
while size <= 0:
    print("Invalid input!")
    size = int(input("Enter the size of the square: "))

border = int(input("Enter the size of the border: "))
while border < 0:
    print("invalid input!")
    border = int(input("Enter the size of the border: "))

total_size = size + (border * 2)

square_color = int(input("Enter the color of the square: "))
while square_color < 0 or square_color > 1:
    print("Invalid input!")
    square_color = int(input("Enter the color of the square: "))

border_color = int(input("Enter the color of the border: "))
while (border_color < 0 or border_color > 1):
    print("Invalid input!")
    square_color = int(input("Enter the color of the border: "))

print("PBM File Contents:")
print("P1")
print(str(total_size) + " " + str(total_size))

for i in range(0, border):
    print((str(border_color) + " ") * (total_size))

for i in range(0, size):
    print((str(border_color) + " ") * border, end="")
    print((str(square_color) + " ") * size, end="")
    print((str(border_color) + " ") * border)

for i in range(0, border):
    print((str(border_color) + " ") * (total_size))