
students = [
    ["Андрій", "Петров"],
    ["Марія", "Іванова"],
    ["Олександр", "Сидоров"],
    ["Андрій", "Коваль"],
    ["Ірина", "Мельник"],
    ["Андрій", "Лисенко"],
]


andriy_count = sum(1 for student in students if student[0] == "Андрій")

print(f"Кількість студентів з іменем 'Андрій': {andrii_count}")
