n = int(input("Количество видеокарт: "))

gpus = []
for i in range(1, n + 1):
    gpu = int(input(f"{i} Видеокарта: "))
    gpus.append(gpu)

print(f"Старый список видеокарт: {gpus}")

max_gpu = max(gpus)
while max_gpu in gpus:
    gpus.remove(max_gpu)

print(f"Новый список видеокарт: {gpus}")