surname = input("Введіть прізвище студента: ")
points = int(input("Введіть кількість балів: "))

if points > 80:
    print(f"Студент {surname} здав іспит")
else:
    print(f"Іспит не складено")

