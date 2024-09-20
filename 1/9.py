text = input("Введіть текст: ")
letter_count = {}
for letter in text:
    if letter.isalpha():
    letter_count[letter] = letter_count.get(letter, 0) + 1

most_common_letter = max(letter_count, key=letter_count.get)
print(f"Літера, яка найчастіше зустрічається: {most_common_letter}")
