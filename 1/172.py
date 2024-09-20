import random
import string

def is_valid_password(password):
    if len(password) < 8:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_letter and has_digit


def generate_password(length=8):
    all_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


name = input("Введіть своє ім'я: ")
position = input("Введіть свою посаду: ")
salary = input("Введіть свою зарплату: ")

confirm_name = input(f"Підтвердіть своє ім'я, введіть його ще раз: ")
if confirm_name != name:
    print("Ім'я не співпадає! Завершення програми.")
    exit()

print("Введіть 1 - для введення свого паролю.")
print("Введіть 2 - для автоматичної генерації паролю.")
choice = input("Ваш вибір: ")

if choice == '1':
    password = input("Введіть свій пароль (мінімум 8 символів, одна буква та одна цифра): ")
    if not is_valid_password(password):
        print("Пароль не відповідає вимогам! Завершення програми.")
        exit()
elif choice == '2':
    password = generate_password()
    print(f"Ваш згенерований пароль: {password}")
else:
    print("Невірний вибір! Завершення програми.")
    exit()

print("Вітаємо! Ви успішно увійшли в систему.")
