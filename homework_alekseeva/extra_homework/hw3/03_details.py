shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000]]

detail = input("Название детали: ")

count = 0
total_price = 0

for item in shop:
    if item[0] == detail:
        count += 1
        total_price += item[1]

print(f"Кол-во деталей — {count}")
print(f"Общая стоимость — {total_price}")