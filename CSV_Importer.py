import csv
import random

## Collections
sharks = []
dragons = []
raptors = []
league = []
experienced = []

with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ## Single list that contains all info
    ## Each player is their own dictionary
    rows = list(reader)

def sort_players_into_teams():

    ## Sort according to experience
    for row in rows:
        if row['Soccer Experience'].upper() == 'YES':
            experienced.append(row)

    ## Distribute among teams
    if len(experienced)%3==0:
        equal_number = int(len(experienced)/3)
        sharks.append(experienced[:equal_number])
        dragons.append(experienced[equal_number:equal_number*2])
        raptors.append(experienced[equal_number*2:])
    else:
        print("Cannot evenly distribute experienced players among the 3 teams.")

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
    else:
        player_team = 'Raptors'
        practice = practice_times[0]

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


sort_players_into_teams()
write_letter('Diego Soto')