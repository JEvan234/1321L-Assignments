#build a website
#print begionning
print("[Let's make a website (URL)!]")
print()
#get user inputs
scheme = input("Scheme: ")
subdomain = input("Subdomain: ")
secondleveldomain = input("Second-level domain: ")
topleveldomain = input("Top-level domain: ")
subdirectory = input("Subdirectory: ")
#print the resulting URL
print()
print("Your URL is:")
print(scheme + "://" + subdomain + "." + secondleveldomain + "." + topleveldomain + "/" + subdirectory)