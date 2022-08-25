import pandas as pd
import numpy as np

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
        self.qb = 0
        self.wr = 0
        self.rb = 0
        self.te = 0
        self.dst = 0
        self.k = 0

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

myTeam.draftPlayer(p1)
myTeam.printTeam()

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

reverse = False
count = 0






