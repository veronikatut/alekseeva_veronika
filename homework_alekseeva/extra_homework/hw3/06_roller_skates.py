n = int(input("Кол-во коньков: "))
skates = []
for i in range(1, n + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)

k = int(input("Кол-во людей: "))
people = []
for i in range(1, k + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    people.append(size)

count = 0
used_skates = []

for person in people:
    if person in skates:
        index = skates.index(person)
        if index not in used_skates:
            used_skates.append(index)
            count += 1

print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}")