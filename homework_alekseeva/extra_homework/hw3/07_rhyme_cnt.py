n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))

print(f"Значит, выбывает каждый {k}-й человек")

circle = list(range(1, n + 1))
index = 0

while len(circle) > 1:
    print(f"\nТекущий круг людей: {circle}")
    print(f"Начало счёта с номера {circle[index]}")

    index = (index + k - 1) % len(circle)
    print(f"Выбывает человек под номером {circle[index]}")
    circle.pop(index)

    if index == len(circle):
        index = 0

print(f"\nОстался человек под номером {circle[0]}")