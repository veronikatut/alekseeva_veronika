alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input("Введите сообщение: ").lower()
k = int(input("Введите сдвиг: "))

encrypted = ''
for char in message:
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + k) % len(alphabet)
        encrypted += alphabet[new_index]
    else:
        encrypted += char

print(f"Зашифрованное сообщение: {encrypted}")