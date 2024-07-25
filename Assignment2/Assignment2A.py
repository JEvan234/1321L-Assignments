#Bits per channel
import math
print("[Image Encoding Checker]")
width = int(input("What is the image width? "))
height = int(input("What is the image height? "))
filesize = int(input("What is the file size (in bytes)? "))
print()
canvas_size = width * height
if (filesize / math.pow(2, 2)) == canvas_size:
    print("The RGBA image is encoded with 8 bits per channel.")
elif (filesize / math.pow(2, 3)) == canvas_size:
    print("The RGBA image is encoded with 16 bits per channel.")
elif (filesize / math.pow(2, 4)) == canvas_size:
    print("The RGBA image is encoded with 32 bits per channel.")
else:
    print("The information is invalid- please re-enter it.")