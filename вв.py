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
    "1. Показати список тварин на лікуванні",
    "2. Додати нову тварину до списку на лікування",
    "3. Тварину вилікувано",
    "4. Показати список вилікуваних тварин",
    "5. Вийти з програми",
    "6. Видалити помилково додану тварину за ім'ям",
    "7. Видалити помилково додану тварину за номером",
    "8. Відсортувати список тварин за ім'ям",
    "9. Змінити ім'я тварини",
    "10. Знайти номер тварини за ім'ям"
]

while True:
    print("Оберіть команду:")
    for i, command in enumerate(commands, start=1):
        print(f"{i}. {command}")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print("Список тварин на лікуванні:", animals)
    elif choice == "2":
        animal = input("Введіть ім'я нової тварини: ")
        animals.append(animal)
        print(f"Тварину '{animal}' додано до списку на лікування.")
    # Додайте решту обробників команд тут
    # ...
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

