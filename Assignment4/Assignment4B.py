#Start the script and define the methods



def valid_check(written):
    check = 10
    for c in str(written):
        c = c.capitalize()
        c = ord(c)
        if 65 <= c <= 90 or c == 32:
            pass
        else:
            check -= 1
    if check < 10:
        return False
    else:
        return True

def encryption(written):
    for c in str(written):
        c = c.upper()
        c = ord(c)
        if c == 32:
            pass
        else:
            c += offset
            if c > 90:
                c -= 26
        c = chr(c)
        print(c, end="")
    return ""

running = True

while running:
    print("Enter your message:")
    message = input()
    offset = int(input("Enter the offset value: "))
    if 0 <= offset <= 26:
        pass
    else:
        print()
        print("sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
        again = input("Do you want to encrypt another message?: ")
        if again.upper() == "N":
            break
    
    if valid_check(message) == True:
        print()
        print("Your secret message is...")
        print(encryption(message))
        again = input("Do you want to encrypt another message?: ")
        if again.upper() == "N":
            break
        elif again.upper() == "Y":
            pass
    else:
        print()
        print("sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
        print()
        again = input("Do you want to encrypt another message?: ")
        if again.upper() == "N":
            break
        elif again.upper() == "Y":
            pass

print()
print("Closing out...")