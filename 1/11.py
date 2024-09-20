import random
import string
import getpass
import re

# Функція для генерації випадкового пароля
def generate_random_password(length=8, use_upper=True, use_special=True, allow_repeats=True):
    characters = string.ascii_lowercase + string.digits
    if use_upper:
        characters += string.ascii_uppercase
    if use_special:
        characters += string.punctuation
    
    if allow_repeats:
        password = ''.join(random.choice(characters) for i in range(length))
    else:
        password = ''.join(random.sample(characters, length))
    
    return password

# Функція для створення пароля
def create_password():
    while True:
        password = getpass.getpass("Введіть ваш пароль: ")
        if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            print("Пароль успішно створено!")
            return password
        else:
            print("Пароль має бути довжиною 8 або більше символів та містити хоча б одну букву і одну цифру.")

# Функція для перевірки, чи є ім'я тварини паліндромом
def is_palindrome(name):
    return name == name[::-1]

# Функція для перевірки груп символів, що повторюються
def find_repeating_groups(text):
    repeating_groups = re.findall(r'(\w+).*\1', text)
    return repeating_groups

# Основна функція для входу в систему
def main():
    print("Ласкаво просимо до інформаційної системи ветеринарної клініки!")
    
    # Вибір створення пароля
    print("1. Створити свій пароль")
    print("2. Згенерувати випадковий пароль")
    choice = input("Виберіть опцію (1 або 2): ")

    if choice == '1':
        password = create_password()
    elif choice == '2':
        length = int(input("Введіть довжину пароля: "))
        use_upper = input("Використовувати великі літери? (так/ні): ").lower() == 'так'
        use_special = input("Використовувати спецсимволи? (так/ні): ").lower() == 'так'
        allow_repeats = input("Чи можуть символи повторюватись? (так/ні): ").lower() == 'так'
        password = generate_random_password(length, use_upper, use_special, allow_repeats)
        print(f"Ваш згенерований пароль: {password}")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        return main()

    # Перевірка імен тварин на паліндроми
    animal_names = input("Введіть імена тварин через кому: ").split(',')
    for name in animal_names:
        name = name.strip()
        if is_palindrome(name):
            print(f"Ім'я {name} є паліндромом.")
        else:
            print(f"Ім'я {name} не є паліндромом.")

    # Створення списку відгуків
    reviews = []
    print("Введіть відгуки. Для завершення введіть 'stop'.")
    while True:
        review = input("Введіть відгук: ")
        if review.lower() == 'stop':
            break
        reviews.append(review)

    # Створення тексту з відгуків
    review_text = ' '.join(reviews)
    print(f"\nТекст з відгуків: {review_text}")

    # Пошук груп символів, що повторюються
    repeating_groups = find_repeating_groups(review_text)
    if repeating_groups:
        print("\nЗнайдено групи символів, що повторюються:")
        for group in repeating_groups:
            print(group)
    else:
        print("\nГрупи символів, що повторюються, не знайдено.")

main()
