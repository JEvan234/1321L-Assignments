#Decision trees
print("Hello stranger! Do you have time to hear my tale?")
print("1) Yes")
print("2) No")
answer = int(input())
if answer == 1:
    print("Thank you! I come from the land of Pax Bisonica. Our country has been taken over by a cruel tyrant!")
    print("1) What can I do?")
    print("2) That's aweful!")
    answer = int(input())
    if answer == 1:
        pass
    elif answer == 2:
        print("Alas, it is truly terrible...")
    print("Please, you must travel to Pax Bisonica and free our country!")
    print("1) Okay")
    print("2) No")
    answer = int(input())
    if answer == 1:
        print("Horray!")
    elif answer == 2:
        print("Then all is lost...")
elif answer == 2:
    print("Ah, then goodbye...")