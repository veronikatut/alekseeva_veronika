s = input("Введите строку: ")

first_h = s.index('h')
last_h = s.rindex('h')

between = s[first_h + 1:last_h]
reversed_between = between[::-1]

print(f"Развёрнутая последовательность между первым и последним h: {reversed_between}")