import random

team1 = [round(random.uniform(5, 10), 2) for i in range(20)]
team2 = [round(random.uniform(5, 10), 2) for i in range(20)]

winners = []
for i in range(20):
    if team1[i] >= team2[i]:
        winners.append(team1[i])
    else:
        winners.append(team2[i])

print(f"Первая команда: {team1}")
print(f"Вторая команда: {team2}")
print(f"Победители тура: {winners}")