students_grades = {
    "Іванов": 5,
    "Петров": 3,
    "Сидоренко": 4,
    "Коваленко": 5,
    "Шевченко": 2,
    "Гнатюк": 4,
    "Остапчук": 5,
    "Бойко": 3
}


top_students = {surname: grade for surname, grade in students_grades.items() if grade in [4, 5]}


print("Учні з оцінками 4 та 5:", top_students)
