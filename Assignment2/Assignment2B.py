#Diamond
#Get variables
char1 = str(input("Enter a charater to use: "))
width = int(input("Enter the diamond's width: "))
#Width parameter 1
if width < 3:
    print("please enter a width of at least 3")
    width = int(input("Enter the diamond's width: "))
#width parameter 2
if width % 2 == 0 :
    odd_width = width + 1
    print("To make a diamond, we will use " + str(odd_width) + " as a width instead")
    width = odd_width
#define what space means
space = int((width - 1) / 2)
#define the counter that will create the shape, from 1 -> width
count = 1
#define the loop to make it bigger
while space >= 1 and count <= width:
    print(" " * space, end="")
    print(char1 * count, end="")
    print(" " * space)
    space -= 1
    count += 2
#define the loop to make it smaller
while space <= width and count >= 1:
    print(" " * space, end="")
    print(char1 * count, end="")
    print(" " * space)
    space += 1
    count -= 2