sentence = input("Введіть речення (щонайменше 7 слів): ")
words = sentence.split()

while len(words) < 7:
    print("Речення занадто коротке!")
    sentence = input("Введіть речення, яке містить щонайменше 7 слів: ")
    words = sentence.split()

ascii_sentence = ""
for char in sentence:
    ascii_sentence += str(ord(char)) + " "

print("\nРечення у вигляді ASCII-кодів:")
print(ascii_sentence.strip())
