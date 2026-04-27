k = int(input("Сдвиг: "))
lst = [1, 2, 3, 4, 5]

print(f"Изначальный список: {lst}")

k = k % len(lst)
lst[:] = lst[-k:] + lst[:-k]

print(f"Сдвинутый список: {lst}")