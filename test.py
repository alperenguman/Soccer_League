import csv
import random


experienced = []
inexperienced = []
dragons_height_list = []
sharks_height_list = []
raptors_height_list = []
dragons = []
sharks = []
raptors = []

with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ## Single list that contains all info
    ## Each player is their own dictionary
    rows = list(reader)

## Sort according to experience
for row in rows:
    if row['Soccer Experience'].upper() == 'YES':
        experienced.append(row)
    else:
        inexperienced.append(row)

## Sort according to height

## Append one random experienced player to the first team

experienced_player1 = random.choice(experienced)
dragons.append(experienced_player1)

## Remove the random experienced player from pool of experienced players
experienced.remove(experienced_player1)

## Take the height average for the first team
for player in dragons:
    dragons_height_list.append(int(player['Height (inches)']))
dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

while len(experienced) != 0:

    ## Append an experienced player as close as possible to the first average
    throwaway_list = []
    for player in experienced:
        throwaway_list.append(dragons_height_average - float(player['Height (inches)']))

    selected_player = experienced[throwaway_list.index(min(throwaway_list))]
    sharks.append(selected_player)
    experienced.remove(selected_player)

    ## Average 2nd team
    for player in sharks:
        sharks_height_list.append(int(player['Height (inches)']))
        sharks_height_average = sum(sharks_height_list)/len(sharks_height_list)

    ## Same thing for the 3rd team
    throwaway_list = []
    for player in experienced:
        throwaway_list.append(sharks_height_average - float(player['Height (inches)']))

    selected_player = experienced[throwaway_list.index(min(throwaway_list))]
    raptors.append(selected_player)
    experienced.remove(selected_player)

    ## Average 3rd team
    for player in raptors:
        raptors_height_list.append(int(player['Height (inches)']))
        raptors_height_average = sum(raptors_height_list)/len(raptors_height_list)

    ## Back to first team inside the while loop
    throwaway_list = []
    for player in experienced:
        throwaway_list.append(raptors_height_average - float(player['Height (inches)']))

    selected_player = experienced[throwaway_list.index(min(throwaway_list))]
    dragons.append(selected_player)
    experienced.remove(selected_player)

    ## Average 1st team
    for player in dragons:
        dragons_height_list.append(int(player['Height (inches)']))
        dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

    continue

