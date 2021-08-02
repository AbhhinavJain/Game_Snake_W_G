import random
def Game():
    user = 0
    com = 0
    for i in range(8):
        var = ["Snake", "Water", "Gun"]
        computer = random.choice(var)
        x = input("your turn:")
        if (x == "snake" or x == "Snake") and computer == "Water":
            user += 1
        elif (x == "snake" or x == "Snake") and computer == "Gun":
            com += 1
        if (x == "Water" or x == "water") and computer == "Gun":
            user += 1
        elif(x == "Water" or x == "water") and computer == "Snake":
            com += 1
        if (x == "Gun" or x == "gun") and computer == "Snake":
            user += 1
        elif (x == "Gun" or x == "gun") and computer == "Water":
            com += 1
        print("I choose :" ,computer)
    print("Game Over :")
    print("Your Score is :", user)
    if user > com:
        print("Congratulations :")
        print("You are WINNER")
    elif user == com:
        print("Match Draw")
        print("if you want to play again , then press 1 otherwise 0")
        again = int(input())
        while(again == 1):
            print("Give your inputs as Snake or snake and so on  as you wish and play .")
            Game()
            print("if you want to play again , then press 1 otherwise 0")
            again = int(input())
    else:
        print("You are Lose")


print("GAME : Snake Water Gun")
print()
print()
print("Now Game Start:")
print("Give your inputs as Snake or snake and so on  as you wish and play .")
Game()
print("if you want to play again , then press 1 otherwise 0")
again = int(input())
while(again == 1):
    Game()
    print("if you want to play again , then press 1 otherwise 0")
    again = int(input())

