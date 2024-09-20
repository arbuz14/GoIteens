animals = [
    "Кілер",
    "Катран",
    "Крістіан",
    "Кербер",
    "Дарлінг",
    "Рефлект",
    "Фарадей",
    "Діксон",
    "Арнольд",
    "Парнас"
]

animals_cured = []

commands = [
    "Показати список тварин на лікуванні",
    "Додати нову тварину до списку на лікування",
    "Тварину вилікувано",
    "Показати список вилікуваних тварин",
    "Вийти з програми",
    "Видалити помилково додану тварину за ім'ям",
    "Видалити помилково додану тварину за номером",
    "Відсортувати список тварин за ім'ям",
    "Змінити ім'я тварини",
    "Знайти номер тварини за ім'ям"
]

def show_animals(animals):
    print("Список тварин на лікуванні:", animals)

def add_animal(animals):
    animal = input("Введіть ім'я нової тварини: ")
    animals.append(animal)
    print(f"Тварину '{animal}' додано до списку на лікування.")

def cure_animal(animals, animals_cured):
    animal = input("Введіть ім'я вилікованої тварини: ")
    if animal in animals:
        animals.remove(animal)
        animals_cured.append(animal)
        print(f"Тварину '{animal}' вилікувано.")
    else:
        print(f"Тварини '{animal}' не знайдено у списку на лікування.")

def show_cured_animals(animals_cured):
    print("Список вилікованих тварин:", animals_cured)

def remove_animal_by_name(animals):
    animal = input("Введіть ім'я тварини для видалення: ")
    if animal in animals:
        animals.remove(animal)
        print(f"Тварину '{animal}' видалено зі списку на лікування.")
    else:
        print(f"Тварини '{animal}' не знайдено у списку на лікування.")

def remove_animal_by_number(animals):
    try:
        index = int(input("Введіть номер тварини для видалення: ")) - 1
        if 0 <= index < len(animals):
            removed_animal = animals.pop(index)
            print(f"Тварину '{removed_animal}' видалено зі списку на лікування.")
        else:
            print("Невірний номер тварини.")
    except ValueError:
        print("Будь ласка, введіть коректний номер.")

def sort_animals(animals):
    animals.sort()
    print("Список тварин відсортовано за ім'ям:", animals)

def change_animal_name(animals):
    old_animal = input("Введіть ім'я тварини, яку потрібно змінити: ")
    if old_animal in animals:
        new_animal = input("Введіть нове ім'я для тварини: ")
        index = animals.index(old_animal)
        animals[index] = new_animal
        print(f"Ім'я тварини '{old_animal}' змінено на '{new_animal}'.")
    else:
        print(f"Тварини '{old_animal}' не знайдено у списку на лікування.")

def find_animal_number(animals):
    animal = input("Введіть ім'я тварини для пошуку її номера: ")
    if animal in animals:
        index = animals.index(animal) + 1
        print(f"Номер тварини '{animal}' у списку: {index}.")
    else:
        print(f"Тварини '{animal}' не знайдено у списку на лікуванні.")

while True:
    print("Оберіть команду:")
    for i, command in enumerate(commands, start=1):
        print(f"{i}. {command}")

    choice = input("Ваш вибір: ")

    if choice == "1":
        show_animals(animals)
    elif choice == "2":
        add_animal(animals)
    elif choice == "3":
        cure_animal(animals, animals_cured)
    elif choice == "4":
        show_cured_animals(animals_cured)
    elif choice == "5":
        print("До побачення!")
        break
    elif choice == "6":
        remove_animal_by_name(animals)
    elif choice == "7":
        remove_animal_by_number(animals)
    elif choice == "8":
        sort_animals(animals)
    elif choice == "9":
        change_animal_name(animals)
    elif choice == "10":
        find_animal_number(animals)
    else:
        print("Невірний вибір. Спробуйте ще раз.")


