#Food bank
#start script
print("[How far your donation goes]")
print()
#get user inputs
cansofsoup = int(input("How many cans of soup? "))
bagsofrice = int(input("How many bags of rice? "))
cansofveggies = int(input("How many cans of vegetables? "))
cansofpbutter = int(input("How many cans of peanut butter? "))
print()
#Perform calculations with operators
fedbysoup = cansofsoup * 2
fedbyrice = bagsofrice * 4
fedbyveggies = cansofveggies * 3.5
fedbypbutter = cansofpbutter * 7
#print final output
totalfed = float(fedbysoup + fedbyrice + fedbyveggies + fedbypbutter)
print("Your donation will help feed " + str(totalfed) + " people!")
print(str(fedbysoup) + " people with the " + str(cansofsoup) + " can(s) of soup")
print(str(fedbyrice) + " people with the " + str(bagsofrice) + " bag(s) of rice")
print(str(fedbyveggies) + " people with the " + str(cansofveggies) + " can(s) of vegetables")
print(str(fedbypbutter) + " people with the " + str(cansofpbutter) + " can(s) of peanut butter")