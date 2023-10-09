import csv
from collections import defaultdict, Counter
import json


def translate_en_csv_to_ca_appending_to_players_list():
    with open('basket_players.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile, delimiter=';')

        for i, row in enumerate(data, start=2):
            player_name = row['Name']
            player_team = row['Team']
            player_position = row['Position']

            player_position = translate_en_position_to_ca(player_position)

            player_height = round(float(row['Heigth']) * height_cm_modifier, 2)
            player_weight = round(float(row['Weigth']) * weight_kg_modifier, 2)
            player_age = round(float(row['Age']))

            student_dict = {
                'Nom': player_name,
                'Equip': player_team,
                'Posicio': player_position,
                'Altura': player_height,
                'Pes': player_weight,
                'Edat': player_age
            }

            players.append(student_dict)
    print(f"\nRecompte de files: {i}")


def translate_en_position_to_ca(player_position):
    match player_position:
        case 'Point Guard':
            player_position = 'Base'
        case 'Shooting Guard':
            player_position = 'Escorta'
        case 'Small Forward':
            player_position = 'Aler'
        case 'Power Forward':
            player_position = 'Ala-pivot'
        case 'Center':
            player_position = 'Pivot'
    return player_position


def convert_students_list_to_csv():
    with open(out_csvfile, 'w', newline='') as open_csvfile:
        fieldnames = ['Nom', 'Equip', 'Posicio', 'Altura', 'Pes', 'Edat']
        writer = csv.DictWriter(open_csvfile, fieldnames=fieldnames, delimiter='^')
        writer.writeheader()
        for alumne in players:
            writer.writerow(alumne)


def get_max_weight():
    max_weight = max(players, key=lambda x: x['Pes'])
    return max_weight


def get_min_height():
    min_height = min(players, key=lambda x: x['Altura'])
    return min_height


def append_players_to_teams():
    for player in players:
        player_team = player['Equip']
        players_by_team[player_team].append(player)
        

def convert_to_json():
    data = []
    with open(out_csvfile, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter='^')
        for row in csv_reader:
            data.append(row)

    with open(out_jsonfile, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def print_average_player_weight_height_per_team():
    print("\nc) Mitjana de pes i alçada de jugador per equip:\n")
    for team, team_players in sorted(players_by_team.items()):
        team_weight = sum(team_player['Pes'] for team_player in team_players) / len(team_players)
        team_height = sum(jugador['Altura'] for jugador in team_players) / len(team_players)
        print(f"Equip: {team}, Mitjana de pes: {team_weight:.2f} kg, Mitjana d'alçada: {team_height:.2f} cm")


def print_player_count_by_position():
    print("\nd) Recompte de jugadors per posició:\n")
    for position, count in positions_count.items():
        print(f"Posició: {position}, Recompte: {count}")


def print_distribution_of_players_by_age_from_youngest_to_oldest():
    print("\ne) Distribución de jugadores por edad de menor a mayor:\n")
    for age, count in age_count.items():
        print(f"Edat: {age}, Recompte: {count}")


def print_player_with_max_weight():
    weight_max = get_max_weight()
    print(f"\na) Nom del jugador amb el pes més alt:\n{weight_max['Nom']} amb un pes de {weight_max['Pes']} kg")


def print_player_with_max_height():
    height_min = get_min_height()
    print(
        f"\nb) Nom del jugador amb l’alçada més petita:\n{height_min['Nom']} amb una alçada de {height_min['Altura']} cm")


height_cm_modifier = 2.54
weight_kg_modifier = 0.45
out_csvfile = 'jugadors_basket.csv'
out_jsonfile = 'jugadors_basket.json'
players = []

translate_en_csv_to_ca_appending_to_players_list()
convert_students_list_to_csv()

print_player_with_max_weight()

print_player_with_max_height()

players_by_team = defaultdict(list)
append_players_to_teams()

print_average_player_weight_height_per_team()

positions = [alumne['Posicio'] for alumne in players]
positions_count = Counter(positions)

print_player_count_by_position()

ages = sorted([player['Edat'] for player in players])
age_count = Counter(ages)

print_distribution_of_players_by_age_from_youngest_to_oldest()

convert_to_json()
