n = int(input("Введите длину списка: "))

lst = []
for i in range(1, n + 1):
    if i % 2 == 0:
        lst.append(1)
    else:
        lst.append(i % 5)

print(f"Результат: {lst}")