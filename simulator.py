import pandas as pd

class Player:
    def __init__(self, name, position, bye, value):
        self.name = name
        self.position = position
        self.bye = bye
        self.value = value

class Team:
    def __init__(self, name, draftPos):
        self.name = name
        self.draftPos = draftPos
        self.team = []

    def draftPlayer(self, player):
        self.team.append(player)

    def printTeam(self):
        for player in self.team:
            print("Name: " + player.name, player.position, player.bye)

rankings = pd.read_csv("Data/TOP300RANKINGS.csv")

print("Enter Team Name: ")
teamName = input()

print("Enter draft pick (1-10): ")
draftPick = int(input())

while(draftPick > 10 or draftPick < 1):
    print("Invalid draft pick! Please choose a different number")
    print("Enter draft pick: ")
    draftPick = int(input())

p1 = Player(rankings.iloc[1][1], rankings.iloc[1][2], rankings.iloc[1][3], rankings.iloc[1][4])
myTeam = Team(teamName, draftPick)


print(rankings)

picks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for pick in picks:
    if draftPick==pick:
        picks.remove(pick)
        break

bot1 = Team("bot1", picks[0])
bot2 = Team("bot2", picks[1])
bot3 = Team("bot3", picks[2])
bot4 = Team("bot4", picks[3])
bot5 = Team("bot5", picks[4])
bot6 = Team("bot6", picks[5])
bot7 = Team("bot7", picks[6])
bot8 = Team("bot8", picks[7])
bot9 = Team("bot9", picks[8])

draftOrder = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9]
draftOrder.insert(draftPick - 1, myTeam)

reverse = False
pickNum = 0

selected = []
for val in range(0, 300):
    selected.append(val)
while(len(rankings) > 0):
    team = draftOrder[pickNum]
    
    if reverse:
        pickNum -= 1
    else :
        pickNum += 1
    
    if pickNum == 10:
        reverse = True
        pickNum -= 1
    elif pickNum == -1:
        reverse = False
        pickNum += 1

    if team.draftPos == myTeam.draftPos:
        print("It's your time to draft! Select a player!")
        print(rankings.head(10))
        print("Enter index number: ")
        num = int(input()) - (int(rankings.iloc[0][0]) - 1)
        p = Player(rankings.iloc[num][1], rankings.iloc[num][2], rankings.iloc[num][3], rankings.iloc[num][4])
        print(rankings.iloc[num][1])
        print(num + rankings.iloc[0][0] - 1)
        selected.remove(num + int(rankings.iloc[0][0]) - 1)
        rankings = rankings.drop(num + int(rankings.iloc[0][0]) - 1)
        print(selected)
        myTeam.draftPlayer(p)
        print("See your team (yes or no)?")
        response = input().lower()
        if(response == "yes"):
            myTeam.printTeam()
    else:
        first = selected.pop(0)
        p = Player(rankings.iloc[0][1], rankings.iloc[0][2], rankings.iloc[0][3], rankings.iloc[0][4])
        rankings = rankings.drop(first)
        team.draftPlayer(p)




