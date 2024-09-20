import json

def save_animals(animals, filename='animals.json'):
    with open(filename, 'w') as file:
        json.dump(animals, file)

def load_animals(filename='animals.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_animal(animals, animal):
    animals.append(animal)
    save_animals(animals)


