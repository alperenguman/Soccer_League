import csv
import random

## Collections
sharks = []
dragons = []
raptors = []
league = []


def sort_players_into_teams():
    experienced = []
    inexperienced = []
    dragons_height_list = []
    sharks_height_list = []
    raptors_height_list = []

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
        raptors_height_average = None
        ## Append an experienced player as close as possible to the first average
        throwaway_list = []
        throwaway_list2 = []
        for player in experienced:
            throwaway_list.append(dragons_height_average - float(player['Height (inches)']))
            try:
                throwaway_list2.append(raptors_height_average - float(player['Height (inches)']))
            except TypeError:
                continue
        try:
            if min(throwaway_list) < min(throwaway_list2):
                selected_player = experienced[throwaway_list.index(min(throwaway_list))]
                sharks.append(selected_player)
                experienced.remove(selected_player)
            else:
                selected_player = experienced[throwaway_list2.index(min(throwaway_list2))]
                sharks.append(selected_player)
                experienced.remove(selected_player)
        except ValueError:
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
        try:
            selected_player = experienced[throwaway_list.index(min(throwaway_list))]
            dragons.append(selected_player)
            experienced.remove(selected_player)

        except ValueError:
            continue

        ## Average 1st team
        for player in dragons:
            dragons_height_list.append(int(player['Height (inches)']))
            dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

        continue

    while len(inexperienced) != 0:

        ## Append an inexperienced player as close as possible to the first average
        throwaway_list = []
        for player in inexperienced:
            throwaway_list.append(dragons_height_average - float(player['Height (inches)']))

        selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
        sharks.append(selected_player)
        inexperienced.remove(selected_player)

        ## Average 2nd team
        for player in sharks:
            sharks_height_list.append(int(player['Height (inches)']))
            sharks_height_average = sum(sharks_height_list)/len(sharks_height_list)

        ## Append an inexperienced player as close as possible to the second average
        throwaway_list = []
        for player in inexperienced:
            throwaway_list.append(sharks_height_average - float(player['Height (inches)']))

        selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
        raptors.append(selected_player)
        inexperienced.remove(selected_player)

        ## Average 3rd team
        for player in sharks:
            raptors_height_list.append(int(player['Height (inches)']))
            raptors_height_average = sum(raptors_height_list)/len(raptors_height_list)

        ## Append an inexperienced player as close as possible to the first average
        throwaway_list = []
        for player in inexperienced:
            throwaway_list.append(raptors_height_average - float(player['Height (inches)']))

        selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
        dragons.append(selected_player)
        inexperienced.remove(selected_player)

        ## Average 1st team
        for player in dragons:
            dragons_height_list.append(int(player['Height (inches)']))
            dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

    return(dragons,raptors,sharks, raptors_height_average, dragons_height_average, sharks_height_average)

dragons, raptors, sharks, x, y, z = sort_players_into_teams()
print(x)
print('\n')
print(y)
print('\n')
print(z)





def set_practice():

    days = 'Friday', 'Saturday', 'Sunday'
    am_pm = 'AM', 'PM'

    raptors_day = random.choice(days)
    raptors_hour = str(random.randint(1,12)) + ' ' + random.choice (am_pm)
    raptors_practice = raptors_day + ' ' + raptors_hour

    sharks_day = random.choice(days)
    sharks_hour = str(random.randint(1,12)) + ' ' + random.choice (am_pm)
    sharks_practice = sharks_day + ' ' + sharks_hour

    dragons_day = random.choice(days)
    dragons_hour = str(random.randint(1,12)) + ' ' + random.choice (am_pm)
    dragons_practice = dragons_day + ' ' + dragons_hour

    ## MAKE SURE PRACTICE TIMES DON'T COINCIDE
    while raptors_practice == dragons_practice or dragons_practice == sharks_practice or raptors_practice == sharks_practice:
        set_practice()

    return (raptors_practice,dragons_practice,sharks_practice)



practice_times = set_practice()

def write_letter(player):

    if player in sharks:
        player_team = 'Sharks'
        practice = practice_times[2]
    elif player in dragons:
        player_team = 'Dragons'
        practice = practice_times[1]
    elif player in raptors:
        player_team = 'Raptors'
        practice = practice_times[0]
    else:
        print("Student not found in database")
        exit()

    for row in rows:
        if row['Name'] == player:
            parents = row['Guardian Name(s)']

    print("""Dear {},

Your child {} is assigned to the team {}.
First practice is on {} at {}. Hope to see you
and little {} there.

Sincerely,
Coach""".format(parents, player, player_team, practice.split()[0], practice.split()[1] + ' ' + practice.split()[2],
                player.split()[0]))


write_letter('Phillip Helm')