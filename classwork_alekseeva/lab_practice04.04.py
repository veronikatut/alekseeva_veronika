import random

# Список возможных вариантов выбора
CHOICES = ["камень", "ножницы", "бумага"]

# Класс, описывающий одного игрока
class Player:
    def __init__(self, name):
        self.name = name      # Имя игрока
        self.score = 0        # Счёт игрока (начинается с 0)

    # Метод для получения хода игрока с клавиатуры
    def get_choice(self):
        print(f"\nХод игрока {self.name}")
        print("Варианты: 1 - Камень, 2 - Ножницы, 3 - Бумага")

        while True:
            choice = input("Ваш выбор (1/2/3): ").strip()
            if choice in ["1", "2", "3"]:
                return CHOICES[int(choice) - 1]  # Возвращаем строку (камень/ножницы/бумага)
            else:
                print("Неверный ввод. Введите 1, 2 или 3.")

    # Метод для добавления очка игроку
    def add_point(self):
        self.score += 1


# Класс, описывающий саму игру
class Game:
    def __init__(self):
        self.players = []       # Список игроков
        self.rounds = 0         # Количество раундов

    # Метод для настройки игры (ввод игроков и раундов)
    def setup(self):
        print("=== Камень, Ножницы, Бумага ===\n")

        # Вводим количество игроков
        while True:
            try:
                count = int(input("Сколько игроков будет играть? "))
                if count >= 2:
                    break
                else:
                    print("Игроков должно быть не меньше 2.")
            except ValueError:
                print("Введите целое число.")

        # Вводим имена игроков и создаём объекты Player
        for i in range(count):
            name = input(f"Введите имя игрока {i + 1}: ").strip()
            self.players.append(Player(name))

        # Вводим количество раундов
        while True:
            try:
                self.rounds = int(input("Сколько раундов сыграем? "))
                if self.rounds >= 1:
                    break
                else:
                    print("Раундов должно быть не меньше 1.")
            except ValueError:
                print("Введите целое число.")

    # Метод для определения победителя в одном раунде
    # Принимает список пар (игрок, его выбор)
    def get_round_winners(self, player_choices):
        # Правила: кто кого побеждает
        wins_against = {
            "камень": "ножницы",    # камень бьёт ножницы
            "ножницы": "бумага",    # ножницы режут бумагу
            "бумага": "камень"      # бумага накрывает камень
        }

        winners = []

        # Сравниваем каждого игрока с каждым
        for i in range(len(player_choices)):
            is_winner = True
            player_i, choice_i = player_choices[i]

            for j in range(len(player_choices)):
                if i == j:
                    continue  # Не сравниваем игрока с самим собой

                player_j, choice_j = player_choices[j]

                # Если игрок i проигрывает хотя бы одному — он не победитель
                if wins_against[choice_j] == choice_i:
                    is_winner = False
                    break

            if is_winner:
                winners.append(player_i)

        # Если победили все — значит ничья (все выбрали одинаково или все варианты)
        if len(winners) == len(player_choices):
            return []  # Ничья — победителей нет

        return winners

    # Метод для запуска одного раунда
    def play_round(self, round_number):
        print(f"\n{'='*30}")
        print(f"  РАУНД {round_number}")
        print(f"{'='*30}")

        player_choices = []

        # Каждый игрок делает свой выбор
        for player in self.players:
            choice = player.get_choice()
            player_choices.append((player, choice))

        # Показываем выборы всех игроков
        print("\nВыборы игроков:")
        for player, choice in player_choices:
            print(f"  {player.name}: {choice}")

        # Определяем победителей раунда
        winners = self.get_round_winners(player_choices)

        if not winners:
            print("\nРезультат: Ничья!")
        else:
            names = ", ".join(w.name for w in winners)
            print(f"\nПобедитель(и) раунда: {names}!")
            for winner in winners:
                winner.add_point()  # Начисляем очки победителям

    # Метод для отображения итогового счёта
    def show_results(self):
        print(f"\n{'='*30}")
        print("  ИТОГОВЫЙ СЧЁТ")
        print(f"{'='*30}")

        # Сортируем игроков по убыванию счёта
        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)

        for i, player in enumerate(sorted_players):
            print(f"  {i + 1}. {player.name} — {player.score} очков")

        # Определяем финального победителя
        top_score = sorted_players[0].score
        champions = [p for p in sorted_players if p.score == top_score]

        print()
        if len(champions) == 1:
            print(f"🏆 Победитель игры: {champions[0].name}!")
        else:
            names = ", ".join(c.name for c in champions)
            print(f"🏆 Ничья между: {names}!")

    # Главный метод — запускает всю игру
    def run(self):
        self.setup()  # Настройка

        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)  # Играем каждый раунд

        self.show_results()  # Показываем итоги


# Точка входа в программу
if __name__ == "__main__":
    game = Game()
    game.run()