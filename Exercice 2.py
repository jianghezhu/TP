import csv

with open('pokemon.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Pikachu', 35, 55, 30, 50, 40, 90])
  writer.writerow(['Charizard', 78, 84, 78, 109, 85, 100])
  writer.writerow(['Magikarp', 20, 10, 55, 15, 20, 80])

def charger_pokemons_csv(pokemon_csv):

  pokemons = {}
  with open(pokemon_csv, 'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
      pokemon_name = row[0]
      stats = [int(stat) for stat in row[1:]]
      pokemons[pokemon_name] = stats

  return pokemons