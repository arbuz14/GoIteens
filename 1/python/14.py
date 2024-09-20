from collections import Counter

def top_three_characters(s):
    s = s.replace(" ", "")
    counter = Counter(s)
    most_common = counter.most_common(3)
    for char, count in most_common:
        print(f"Символ: '{char}', Кількість: {count}")

input_string = "Це речення потрібно для коду"
top_three_characters(input_string)
