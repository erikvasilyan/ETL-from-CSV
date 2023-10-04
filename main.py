import csv


def convertAlumnesDictToCsvAndSave():
    output_file = 'basket_players_CA.csv'

    with open(output_file, 'w', newline='') as outCsvfile:
        fieldnames = ['Nom', 'Equip', 'Posicio', 'Altura', 'Pes', 'Edat']
        writer = csv.DictWriter(outCsvfile, fieldnames=fieldnames)

        writer.writeheader()
        for alumne in alumnes:
            writer.writerow(alumne)


alumnes = []

with open('basket_players.csv', 'r') as csvfile:
    dades = csv.DictReader(csvfile, delimiter=';')

    for i, row in enumerate(dades):
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

        height = float(row['Heigth']) * 2.54
        weight = float(row['Weigth']) * 0.45
        age = round(float(row['Age']))

        alumne_dict = {
            'Nom': name,
            'Equip': team,
            'Posicio': position,
            'Altura': height,
            'Pes': weight,
            'Edat': age
        }

        alumnes.append(alumne_dict)

convertAlumnesDictToCsvAndSave()
