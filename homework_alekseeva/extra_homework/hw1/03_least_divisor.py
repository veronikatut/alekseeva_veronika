def min_divisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1

n = int(input("Введите число: "))
print(f"Наименьший делитель, отличный от единицы: {min_divisor(n)}")