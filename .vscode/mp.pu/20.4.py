from animals import load_animals, add_animal
from healed_animals import load_healed_animals, add_healed_animal
from feedback import load_feedback, add_feedback

def main():
    # Завантаження списків
    animals = load_animals()
    healed_animals = load_healed_animals()
    feedbacks = load_feedback()

    # Додавання нових тварин
    add_animal(animals, {"name": "Dog", "status": "Sick"})
    add_healed_animal(healed_animals, {"name": "Cat", "status": "Healed"})
    add_feedback(feedbacks, {"author": "John Doe", "text": "Great service!"})

    # Показ списків
    print("Animals:", animals)
    print("Healed Animals:", healed_animals)
    print("Feedbacks:", feedbacks)

if __name__ == "__main__":
    main()




