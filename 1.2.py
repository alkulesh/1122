str = input("Введите строку: ")
unicode_str = [ord(char) for char in str]
for code in unicode_str:
    print(code)
words = str.split()
long_word = max(words, key=len)
print("Самое длинное слово:", long_word)
