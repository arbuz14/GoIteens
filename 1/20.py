import json

class AnimalRegistry:
    def __init__(self, filename='animals.json'):
        self.filename = filename
        self.animals = self.load_animals()

    def load_animals(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_animals(self):
        with open(self.filename, 'w') as file:
            json.dump(self.animals, file, ensure_ascii=False, indent=4)

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            self.save_animals()

    def list_animals(self):
        return self.animals


class TreatedAnimalsRegistry:
    def __init__(self, filename='treated_animals.json'):
        self.filename = filename
        self.treated_animals = self.load_treated_animals()

    def load_treated_animals(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_treated_animals(self):
        with open(self.filename, 'w') as file:
            json.dump(self.treated_animals, file, ensure_ascii=False, indent=4)

    def add_treated_animal(self, animal):
        if animal not in self.treated_animals:
            self.treated_animals.append(animal)
            self.save_treated_animals()

    def list_treated_animals(self):
        return self.treated_animals

class ReviewsRegistry:
    def __init__(self, filename='reviews.json'):
        self.filename = filename
        self.reviews = self.load_reviews()
    def load_reviews(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    def save_reviews(self):
        with open(self.filename, 'w') as file:
            json.dump(self.reviews, file, ensure_ascii=False, indent=4)
    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
            self.save_reviews()
    def list_reviews(self):
        return self.reviews


def main():
    animal_registry = AnimalRegistry()
    animal_registry.add_animal({"name": "Барсик", "species": "Кіт"})
    print("Список тварин:", animal_registry.list_animals())

    treated_animals_registry = TreatedAnimalsRegistry()
    treated_animals_registry.add_treated_animal({"name": "Барсик", "species": "Кіт"})
    print("Список вилікуваних тварин:", treated_animals_registry.list_treated_animals())

    
    reviews_registry = ReviewsRegistry()
    reviews_registry.add_review({"author": "Олена", "text": "Дуже хороший ветеринар!"})
    print("Відгуки:", reviews_registry.list_reviews())

if __name__ == "__main__":
    main()

