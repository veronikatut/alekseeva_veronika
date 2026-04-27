guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break

    name = input("Имя гостя: ")

    if action == "пришёл":
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")

    elif action == "ушёл":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Гостя {name} нет на вечеринке")