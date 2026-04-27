word = input("Введите слово: ")

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")