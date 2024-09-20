sentence = input("Введіть рядок: ")
words = sentence.split()  
longest_word = ""
max_length = 0

for word in words:
    length = len(word)
    if length > max_length:
        longest_word = word
        max_length = length

print("Слово з найбільшою довжиною:", longest_word)
