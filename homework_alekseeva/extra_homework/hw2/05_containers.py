n = int(input("Количество контейнеров: "))

containers = []
for i in range(n):
    weight = int(input("Введите вес контейнера: "))
    while weight > 200:
        print("Ошибка! Вес не должен превышать 200")
        weight = int(input("Введите вес контейнера: "))
    containers.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))
while new_weight > 200:
    print("Ошибка! Вес не должен превышать 200")
    new_weight = int(input("Введите вес нового контейнера: "))

position = 1
for i in range(n):
    if containers[i] >= new_weight:
        position = i + 2

print(f"Номер, который получит новый контейнер: {position}")