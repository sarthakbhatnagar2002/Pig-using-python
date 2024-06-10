import random

def roll():
    mini=1
    maxi=6
    roll= random.randint(mini,maxi)
    return roll

while True:
    players=input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players<=4:
            break

target=int(input("What is the target "))

player_scores=[0 for _ in range(players)]
print(player_scores)

while max(player_scores) < target:
    for playeridx in range(players):
        print("\nPlayer",playeridx+1,"'s turn has just begun\n")
        currentscore=0

        while True:
            turn = input("\nDo you want to continue? (y/n): \n")
            if turn.lower() != "y":
                break

            value=roll()
            if value==1:
                print("\nYou got a 1! Its over for you\n")
                currentscore=0
                break
            else:
                print("\nYou got a ",value)
                currentscore+=value
                
            print("Your score is ", currentscore)
        player_scores[playeridx]+=currentscore
        print("\nYour total score is \n", player_scores[playeridx])

target=max(player_scores)
win=player_scores.index(target)
print("Player",win+1,"is the winner with the score :",target)
