most_powerful_word = ""
max_power = 0

while True:
    word = input()

    if word == "End of words":
        break

    power = sum(ord(letter) for letter in word)

    if word[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        power *= len(word)
    else:
        power = power // len(word)

    if power > max_power:
        most_powerful_word = word
        max_power = power

print(f"The most powerful word is {most_powerful_word} - {max_power}")
