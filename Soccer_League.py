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

    if len(experienced) %3 != 0:
        print("Cannot evenly distribute Experienced players among the 3 teams")
        exit()
    else:
        pass
    First_Round = True
    raptors_height_average = 0
    dragons_height_average = 0
    while len(experienced) != 0:
        ## Append an experienced player to sharks as close as possible to the dragons average
        throwaway_list = []
        throwaway_list2 = []
        for player in experienced:
            throwaway_list.append(abs(dragons_height_average - float(player['Height (inches)'])))
            throwaway_list2.append(abs(raptors_height_average - float(player['Height (inches)'])))

        if First_Round == True:
            random_player = random.choice(experienced)
            sharks.append(random_player)
            experienced.remove(random_player)
            First_Round == False
        elif throwaway_list2 != [] and min(throwaway_list2) < min(throwaway_list):
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


        if min(throwaway_list) < min(throwaway_list2):
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

    difference = []
    difference.append(dragons_height_average)
    difference.append(sharks_height_average)
    difference.append(raptors_height_average)
    diff = max(difference) - min(difference)

    sharks_players = []
    dragons_players = []
    raptors_players = []

    for players in sharks:
        sharks_players.append(players['Name'])
    for players in dragons:
        dragons_players.append(players['Name'])
    for players in raptors:
        raptors_players.append(players['Name'])

    if diff >= 1:
        return sort_players_into_teams()

    else:
        return(dragons,raptors,sharks, raptors_height_average, dragons_height_average,
               sharks_height_average, raptors_players, dragons_players, sharks_players)


def write_letter(player):

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
Coach""".format(parents, player, player_team, practice.split()[0] + ' ' + practice.split()[1],practice.split()[2],
                player.split()[0])

    name_split = player.split()
    name_join = '_'.join(name_split)
    player_file = name_join.lower() + '.txt'

    with open(player_file, "w") as file:
        file.write(letter)

def write_log():
    import time
    time = time.localtime()
    time_list = str(time[3]) + ':' + str(time[4]) + ':' + str(time[5])
    a = 0
    for players in raptors:
        if players['Soccer Experience'].upper() == 'YES':
            a = a + 1
        else:
            continue
    b = 0
    for players in dragons:
        if players['Soccer Experience'].upper() == 'YES':
            b = b + 1
        else:
            continue
    c = 0
    for players in sharks:
        if players['Soccer Experience'].upper() == 'YES':
            c = c + 1
        else:
            continue

    difference = []
    difference.append(dragons_height_average)
    difference.append(sharks_height_average)
    difference.append(raptors_height_average)
    diff = max(difference) - min(difference)

    log_file = 'log'

    log_content = """
Generated at {}

Raptors - Experienced Players: {}
Dragons - Experienced Players: {}
Sharks - Experienced Players: {}

Raptors Height Average: {}
Dragons Height Average: {}
Sharks Height Average: {}
Tallest/Shortest Difference: {}

Raptors Team: {}
Dragons Team: {}
Sharks Team: {}

Dragons Practice: {}
Raptors Practice: {}
Sharks Practice: {}

############################
""".format(time_list, a, b, c, raptors_height_average,dragons_height_average,sharks_height_average, diff,
           ", ".join(raptors_players), ", ".join(dragons_players), ", ".join(sharks_players), practice_times[1], practice_times[0], practice_times[2])

    with open(log_file, "a") as log:
        log.write(log_content)

    return (log_content)

if __name__ == "__main__":
    rows = csv_import()
    dragons,raptors,sharks, raptors_height_average, dragons_height_average, sharks_height_average, raptors_players, dragons_players, sharks_players= sort_players_into_teams()
    practice_times = ["March 18, 1pm", "March 17, 1pm", "March 17, 3pm"]
    league = dragons_players + raptors_players + sharks_players
    for player in league:
        write_letter(player)
    log = write_log()
    print("\n" + "Success!" + "\n" + log)