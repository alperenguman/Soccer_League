import csv
import random

def csv_import():
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        ## Single list that contains all info
        ## Each player is their own dictionary
        rows = list(reader)

    return (rows)

def sort_players_into_teams():

    ## Collections
    sharks = []
    dragons = []
    raptors = []

    experienced = []
    inexperienced = []

    dragons_height_list = []
    sharks_height_list = []
    raptors_height_list = []

    rows = csv_import()

    ## Sort according to experience
    for row in rows:
        if row['Soccer Experience'].upper() == 'YES':
            experienced.append(row)
        else:
            inexperienced.append(row)

    ## Sort according to height & experience

    experienced_player1 = random.choice(experienced)
    dragons.append(experienced_player1)

    ## Remove the random experienced player from pool of experienced players
    experienced.remove(experienced_player1)

    ## Take the height average for dragons
    for player in dragons:
        dragons_height_list.append(int(player['Height (inches)']))
    dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

    while len(experienced) != 0:
        raptors_height_average = None
        ## Append an experienced player to sharks as close as possible to the dragons average
        throwaway_list = []
        throwaway_list2 = []
        for player in experienced:
            throwaway_list.append(abs(dragons_height_average - float(player['Height (inches)'])))
            ## Try block for when raptors height average is null when there are no members of the team yet.
            try:
                throwaway_list2.append(abs(raptors_height_average - float(player['Height (inches)'])))
            except TypeError:
                continue

        if throwaway_list2 != [] and min(throwaway_list2) < min(throwaway_list):
            selected_player = experienced[throwaway_list2.index(min(throwaway_list2))]
            sharks.append(selected_player)
            experienced.remove(selected_player)
        else:
            selected_player = experienced[throwaway_list.index(min(throwaway_list))]
            sharks.append(selected_player)
            experienced.remove(selected_player)

        ## Average height of sharks
        for player in sharks:
            sharks_height_list.append(int(player['Height (inches)']))

        sharks_height_average = sum(sharks_height_list)/len(sharks_height_list)

        ## Same thing for the raptors
        throwaway_list = []
        throwaway_list2 = []
        for player in experienced:
            throwaway_list.append(abs(sharks_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(dragons_height_average - float(player['Height (inches)'])))

        if min(throwaway_list) < min(throwaway_list2):
                selected_player = experienced[throwaway_list.index(min(throwaway_list))]
                raptors.append(selected_player)
                experienced.remove(selected_player)
        else:
            selected_player = experienced[throwaway_list2.index(min(throwaway_list2))]
            raptors.append(selected_player)
            experienced.remove(selected_player)

        ## Average height of raptors
        for player in raptors:
            raptors_height_list.append(int(player['Height (inches)']))

        raptors_height_average = sum(raptors_height_list)/len(raptors_height_list)

        ## Back to first team inside the while loop
        throwaway_list = []
        throwaway_list2 = []
        for player in experienced:
            throwaway_list.append(abs(raptors_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(sharks_height_average -float(player['Height (inches)'])))

            if throwaway_list != [] and throwaway_list2 != [] and min(throwaway_list) < min(throwaway_list2):
                    selected_player = experienced[throwaway_list.index(min(throwaway_list))]
                    dragons.append(selected_player)
                    experienced.remove(selected_player)
            else:
                selected_player = experienced[throwaway_list2.index(min(throwaway_list2))]
                dragons.append(selected_player)
                experienced.remove(selected_player)

        ## Average height of dragons
        for player in dragons:
            dragons_height_list.append(int(player['Height (inches)']))

        dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

    while len(inexperienced) != 0:

        ## Inexperienced - Sharks
        throwaway_list = []
        throwaway_list2 = []
        for player in inexperienced:
            throwaway_list.append(abs(dragons_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(raptors_height_average - float(player['Height (inches)'])))

        if min(throwaway_list) < min(throwaway_list2):
                selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
                sharks.append(selected_player)
                inexperienced.remove(selected_player)
        else:
            selected_player = inexperienced[throwaway_list2.index(min(throwaway_list2))]
            sharks.append(selected_player)
            inexperienced.remove(selected_player)

        for player in sharks:
            sharks_height_list.append(int(player['Height (inches)']))

        sharks_height_average = sum(sharks_height_list)/len(sharks_height_list)

        ## Inexperienced - Raptors
        throwaway_list = []
        throwaway_list2 = []
        for player in inexperienced:
            throwaway_list.append(abs(sharks_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(dragons_height_average - float(player['Height (inches)'])))

        if min(throwaway_list) < min(throwaway_list2):
                selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
                raptors.append(selected_player)
                inexperienced.remove(selected_player)
        else:
            selected_player = inexperienced[throwaway_list2.index(min(throwaway_list2))]
            raptors.append(selected_player)
            inexperienced.remove(selected_player)

        for player in raptors:
            raptors_height_list.append(int(player['Height (inches)']))

        raptors_height_average = sum(raptors_height_list)/len(raptors_height_list)

        ## Inexperienced - Dragons
        throwaway_list = []
        throwaway_list2 = []
        for player in inexperienced:
            throwaway_list.append(abs(raptors_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(sharks_height_average - float(player['Height (inches)'])))

        if min(throwaway_list) < min(throwaway_list2):
                selected_player = inexperienced[throwaway_list.index(min(throwaway_list))]
                dragons.append(selected_player)
                inexperienced.remove(selected_player)
        else:
            selected_player = inexperienced[throwaway_list2.index(min(throwaway_list2))]
            dragons.append(selected_player)
            inexperienced.remove(selected_player)

        for player in dragons:
            dragons_height_list.append(int(player['Height (inches)']))

        dragons_height_average = sum(dragons_height_list)/len(dragons_height_list)

    return(dragons,raptors,sharks, raptors_height_average, dragons_height_average, sharks_height_average)

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
    if raptors_practice == dragons_practice or dragons_practice == sharks_practice or raptors_practice == sharks_practice:
        set_practice()

    return (raptors_practice,dragons_practice,sharks_practice)

def write_letter(player):

    sharks_players = []
    dragons_players = []
    raptors_players = []

    rows = csv_import()

    for players in sharks:
        sharks_players.append(players['Name'])
    for players in dragons:
        dragons_players.append(players['Name'])
    for players in raptors:
        raptors_players.append(players['Name'])

    if player in sharks_players:
        player_team = 'Sharks'
        practice = practice_times[2]
    elif player in dragons_players:
        player_team = 'Dragons'
        practice = practice_times[1]
    elif player in raptors_players:
        player_team = 'Raptors'
        practice = practice_times[0]
    else:
        print("Student not found in database")
        exit()

    for row in rows:
        if row['Name'] == player:
            parents = row['Guardian Name(s)']

    letter = """Dear {},

Your child {} is assigned to the team {}.
First practice is on {} at {}. Hope to see you
and little {} there.

Sincerely,
Coach""".format(parents, player, player_team, practice.split()[0], practice.split()[1] + ' ' + practice.split()[2],
                player.split()[0])

    name_split = player.split()
    name_join = '_'.join(name_split)
    player_file = name_join + '.txt'

    with open(player_file, "w") as file:
        file.write(letter)

    return(sharks_players, dragons_players, raptors_players)

def write_log():
    import time
    time = time.localtime()
    print (time)
    time_list = str(time[3]) + ':' + str(time[4]) + ':' + str(time[5])

    log_file = 'log'

    log_content = """

Generated at {}

Raptors Height Average: {}
Dragons Height Average: {}
Sharks Height Average: {}

Raptors Team: {}
Dragons Team: {}
Sharks Team: {}

Dragons Practice: {}
Raptors Practice: {}
Sharks Practice: {}

############################
""".format(time_list,raptors_height_average,dragons_height_average,sharks_height_average,
           raptors_players, dragons_players, sharks_players, practice_times[1], practice_times[0], practice_times[2])

    with open(log_file, "a") as log:
        log.write(log_content)

if __name__ == "__main__":
    dragons,raptors,sharks, raptors_height_average, dragons_height_average, sharks_height_average = sort_players_into_teams()
    practice_times = set_practice()
    sharks_players, raptors_players, dragons_players = write_letter('Sal Dali')
    write_log()