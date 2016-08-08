import csv

with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

def sort_players_into_teams():
    ## Collections
    sharks = []
    dragons = []
    raptors = []
    league = []
    experienced = []

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

    


sort_players_into_teams()