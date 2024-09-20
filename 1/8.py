text = input("Введіть рядок: ")
result = ''.join([char for char in text if not char.isdigit()])
print(f"Результат: {result}")
