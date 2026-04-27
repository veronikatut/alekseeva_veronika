n = int(input("Кол-во чисел: "))
lst = []
for i in range(n):
    lst.append(int(input("Число: ")))

print(f"Последовательность: {lst}")

# Ищем минимальный суффикс lst, который является началом палиндрома
to_add = []

for start in range(len(lst)):
    temp = lst[start:]
    # проверяем является ли lst палиндромом если приписать temp[::-1] в конец
    candidate = lst + temp[::-1]
    # проверяем палиндром ли candidate
    if candidate == candidate[::-1]:
        to_add = temp[::-1]
        break

# если не нашли — просто разворачиваем весь список
if not to_add and lst != lst[::-1]:
    to_add = lst[::-1]

print(f"Нужно приписать чисел: {len(to_add)}")
print(f"Сами числа: {to_add}")