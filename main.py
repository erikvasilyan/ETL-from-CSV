import csv
from collections import defaultdict, Counter


def translateEnCsvToCaAppendingToPlayersList():
    with open('basket_players.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile, delimiter=';')

        for i, row in enumerate(data):
            playerName = row['Name']
            playerTeam = row['Team']
            playerPosition = row['Position']

            match playerPosition:
                case 'Point Guard':
                    playerPosition = 'Base'
                case 'Shooting Guard':
                    playerPosition = 'Escorta'
                case 'Small Forward':
                    playerPosition = 'Aler'
                case 'Power Forward':
                    playerPosition = 'Ala-pivot'
                case 'Center':
                    playerPosition = 'Pivot'

            playerHeight = round(float(row['Heigth']) * HEIGHT_CM_MODIFIER, 2)
            playerWeight = round(float(row['Weigth']) * WEIGHT_KG_MODIFIER, 2)
            playerAge = round(float(row['Age']))

            student_dict = {
                'Nom': playerName,
                'Equip': playerTeam,
                'Posicio': playerPosition,
                'Altura': playerHeight,
                'Pes': playerWeight,
                'Edat': playerAge
            }

            players.append(student_dict)
    print(f"\nRecompte de files: {i}")


def convertStudentsListToCsvAndSave():
    with open(OUT_FILE, 'w', newline='') as outCsvfile:
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


def appendPlayersToTeams():
    for player in players:
        playerTeam = player['Equip']
        playersByTeam[playerTeam].append(player)


HEIGHT_CM_MODIFIER = 2.54
WEIGHT_KG_MODIFIER = 0.45
OUT_FILE = 'basket_players_CA.csv'
players = []

translateEnCsvToCaAppendingToPlayersList()
convertStudentsListToCsvAndSave()

weightMax = calculateMaxWeight()
print(f"\na) Nom del jugador amb el pes més alt:\n{weightMax['Nom']} amb un pes de {weightMax['Pes']} kg")

heightMin = calculateMinHeight()
print(f"\nb) Nom del jugador amb l’alçada més petita:\n{heightMin['Nom']} amb una alçada de {heightMin['Altura']} cm")

playersByTeam = defaultdict(list)
appendPlayersToTeams()

print("\nc) Mitjana de pes i alçada de jugador per equip:\n")
for team, jugadors in sorted(playersByTeam.items()):
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
