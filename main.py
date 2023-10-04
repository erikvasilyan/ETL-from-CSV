import csv
from collections import defaultdict, Counter


def convertAlumnesDictToCsvAndSave():
    output_file = 'basket_players_CA.csv'

    with open(output_file, 'w', newline='') as outCsvfile:
        fieldnames = ['Nom', 'Equip', 'Posicio', 'Altura', 'Pes', 'Edat']
        writer = csv.DictWriter(outCsvfile, fieldnames=fieldnames, delimiter='^')
        writer.writeheader()
        for alumne in players:
            writer.writerow(alumne)


def calculateMaxWeight():
    maxWeight = max(players, key=lambda x: x['Pes'])
    return maxWeight


def calculateMinHeight():
    minHeight = min(players, key=lambda x: x['Altura'])
    return minHeight


players = []

with open('basket_players.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile, delimiter=';')

    for i, row in enumerate(data):
        name = row['Name']
        team = row['Team']
        position = row['Position']

        match position:
            case 'Point Guard':
                position = 'Base'
            case 'Shooting Guard':
                position = 'Escorta'
            case 'Small Forward':
                position = 'Aler'
            case 'Power Forward':
                position = 'Ala-pivot'
            case 'Center':
                position = 'Pivot'

        height = round(float(row['Heigth']) * 2.54, 2)
        weight = round(float(row['Weigth']) * 0.45, 2)
        age = round(float(row['Age']))

        alumne_dict = {
            'Nom': name,
            'Equip': team,
            'Posicio': position,
            'Altura': height,
            'Pes': weight,
            'Edat': age
        }

        players.append(alumne_dict)

print(f"\nRecompte de files: {i}")

convertAlumnesDictToCsvAndSave()

weightMax = calculateMaxWeight()
print(f"\na) Nom del jugador amb el pes més alt:\n{weightMax['Nom']} amb un pes de {weightMax['Pes']} kg")

heightMin = calculateMinHeight()
print(f"\nb) Nom del jugador amb l’alçada més petita:\n{heightMin['Nom']} amb una alçada de {heightMin['Altura']} cm")

teamPlayers = defaultdict(list)
for player in players:
    team = player['Equip']
    teamPlayers[team].append(player)

print("\nc) Mitjana de pes i alçada de jugador per equip:\n")
for team, jugadors in sorted(teamPlayers.items()):
    teamWeight = sum(jugador['Pes'] for jugador in jugadors) / len(jugadors)
    teamHeight = sum(jugador['Altura'] for jugador in jugadors) / len(jugadors)
    print(f"Equip: {team}, Mitjana de pes: {teamWeight:.2f} kg, Mitjana d'alçada: {teamHeight:.2f} cm")

positions = [alumne['Posicio'] for alumne in players]
positionsCount = Counter(positions)

print("\nd) Recompte de jugadors per posició:\n")
for position, count in positionsCount.items():
    print(f"Posició: {position}, Recompte: {count}")

ages = sorted([player['Edat'] for player in players])
ageCount = Counter(ages)

print("\ne) Distribución de jugadores por edad de menor a mayor:\n")
for age, count in ageCount.items():
    print(f"Edat: {age}, Recompte: {count}")
