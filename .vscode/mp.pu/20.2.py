import json

def save_healed_animals(healed_animals, filename='healed_animals.json'):
    with open(filename, 'w') as file:
        json.dump(healed_animals, file)

def load_healed_animals(filename='healed_animals.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_healed_animal(healed_animals, animal):
    healed_animals.append(animal)
    save_healed_animals(healed_animals)



