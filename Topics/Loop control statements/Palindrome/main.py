
word = input()

word_reverse = ''.join(reversed(word))


if word == word_reverse:
    print("Palindrome")
else:
    print("Not palindrome")
