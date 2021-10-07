word = input()

char_list = list(word)

char_list[0] = char_list[0].lower()

for char in char_list:
    if char.isupper():
        char_list[char_list.index(char)] = "_" + char
    else:
        pass

word = ''.join(char_list)

word = word.lower()

print(word)
