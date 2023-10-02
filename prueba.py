import csv


with open('basket_players.csv', 'r') as csvfile:
    dades = csv.reader(csvfile)

    for row in dades:
        print(row)

    print("Nom;Equip;Posicio;Altura;Pes;Edat")


# print(f'\nNumber of lines: {i}')


