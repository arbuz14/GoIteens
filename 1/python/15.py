import random
import string
import getpass

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def create_account():
    name = input("Введіть ваше ім'я: ")
    profession = input("Введіть вашу професію: ")
    salary = input("Введіть вашу зарплату: ")

    print("1. Створити свій пароль")
    print("2. Згенерувати випадковий пароль")
    choice = input("Виберіть опцію (1 або 2): ")

    if choice == '1':
        while True:
            password = getpass.getpass("Введіть ваш пароль: ")
            confirm_password = getpass.getpass("Підтвердіть ваш пароль: ")
            if password == confirm_password:
                print("Пароль успішно створено!")
                break
            else:
                print("Паролі не співпадають. Спробуйте ще раз.")
    elif choice == '2':
        password = generate_random_password()
        print(f"Ваш згенерований пароль: {password}")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        return create_account()

    
    print("\nОбліковий запис створено:")
    print(f"Ім'я: {name}")
    print(f"Професія: {profession}")
    print(f"Зарплата: {salary}")
    print(f"Пароль: {password}")

create_account()
