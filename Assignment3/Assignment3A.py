#Mathletes game
#Add the random funtion
import random
print("[Mathletes Game]")
#define the gamemodes
def easymode():
    print("Playing on easy mode, huh? Okay!")
    strikes = 0
    for Q in range(1, 4):
        v1 = random.randint(-255, 255)
        v2 = random.randint(-255, 255)
        print(f'Q{Q}. {v1} * {v2} = ?')
        answer = int(input())
        while answer != v1 * v2:
            strikes += 1
            if strikes == 3:
                print("Game over...")
                exit()
            print("Incorrect! Try again.")
            answer = int(input())
        print("Correct!")
    print("You Win!")
    exit()

def hardmodemode():
    print("So, you want a challenge? Okay!")
    strikes = 0
    for Q in range(1, 7):
        v1 = random.randint(-255, 255)
        v2 = random.randint(-255, 255)
        print(f'Q{Q}. {v1} * {v2} = ?')
        answer = int(input())
        while answer != v1 * v2:
            strikes += 1
            if strikes == 1:
                print("Incorrect!")
                print("Game over...")
                exit()
            print("Incorrect! Try again.")
            answer = int(input())
        print("Correct!")
    print("You Win!")
    exit()

#game loop
game_mode = int(input("Choose a game mode (0 = Easy, 1 = Hard): "))
while True:
    match game_mode:
        case 0:
            easymode()
            break

        case 1:
            hardmodemode()
            break
    
        case _:
            print("Not an option")
            game_mode = int(input("Choose a game mode (0 = Easy, 1 = Hard): "))