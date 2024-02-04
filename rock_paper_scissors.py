import random

poison = ("boulder", "parchment", "shears")
playing = True

while playing:

    player = None
    computer = random.choice(poison)

    while player not in poison:
        player = input("Pick your poison (boulder, parchment, shears): ").lower()

    print(f"Player: {player}")
    print(f"Opponent: {computer}")

    if player == computer:
        print("It's a DRAW!")
    elif player == "boulder" and computer == "shears":
        print("You WIN!")
    elif player == "parchment" and computer == "boulder":
        print("You WIN!")
    elif player == "shears" and computer == "parchment":
        print("You WIN!")
    else:
        print("You LOSE!")

    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again == "I quit":
        playing = False

    elif play_again == "no":
        playing = False
    
    
print("Thank you for playing. :)")






# class Play:

#     def __init__(self, player, poison, opponent):
#         self.player = player
#         self.poison = poison
#         self.opponent = opponent

#         self.player = None
#         self.opponent = random.choice(poison)
#         self.poison = ("boulder", "parchment", "shears")

#     def Draw(self):
#         self.player == self.opponent
#         print("It's a DRAW!")

#     def Boulder(self):
#         self.player == "boulder" and self.opponent == "shears"
#         print("You WIN!")

#     def Parchment(self):
#         self.player == "parchment" and self.opponent == "boulder"
#         print("You WIN!")

#     def Shears(self):
#         self.player == "shears" and self.opponent == "parchment"
#         print("You WIN!")
        
#     def quit(self):
#         print("Thank you for playing. :))
    


