# Словарь рецептов
recipes = {
    tuple(sorted(("вода", "огонь"))): "пар",
    tuple(sorted(("вода", "земля"))): "грязь",
    tuple(sorted(("огонь", "земля"))): "лава",
    tuple(sorted(("воздух", "огонь"))): "энергия",
    tuple(sorted(("вода", "воздух"))): "дождь",
    tuple(sorted(("земля", "воздух"))): "пыль",
    tuple(sorted(("пар", "воздух"))): "облако",
    tuple(sorted(("облако", "воздух"))): "ветер",
    tuple(sorted(("облако", "вода"))): "дождь",
    tuple(sorted(("дождь", "земля"))): "растение",
    tuple(sorted(("лава", "вода"))): "камень",
    tuple(sorted(("камень", "огонь"))): "металл",
    tuple(sorted(("металл", "огонь"))): "инструмент",
    tuple(sorted(("растение", "огонь"))): "уголь",
    tuple(sorted(("грязь", "огонь"))): "кирпич",
    tuple(sorted(("камень", "воздух"))): "песок",
    tuple(sorted(("песок", "огонь"))): "стекло",
    tuple(sorted(("металл", "камень"))): "нож",
    tuple(sorted(("энергия", "камень"))): "молния",
    tuple(sorted(("вода", "энергия"))): "жизнь",
    tuple(sorted(("жизнь", "земля"))): "человек",
    tuple(sorted(("человек", "инструмент"))): "ремесленник",
    tuple(sorted(("человек", "человек"))): "деревня",
}

my_elements = ["вода", "огонь", "земля", "воздух"]


class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):

        pair1 = tuple(sorted([self.name, other.name]))

        if pair1 in recipes:
            return recipes[pair1]

        return None

    def __str__(self):
        return self.name



def show_elements():
    print("\n=== Твои элементы ===")
    for i, elem in enumerate(my_elements):
        print(f"  {i + 1}. {elem}")
    print("====================")



def play():
    print("=" * 40)
    print("      Добро пожаловать в АЛХИМИЮ!")
    print("=" * 40)
    print("Соединяй элементы и открывай новые!")
    print("Введи 'стоп' чтобы выйти из игры")
    print("Введи 'список' чтобы увидеть элементы")

    while True:
        show_elements()

        first = input("\nВведи первый элемент: ").strip().lower()

        if first == "стоп":
            print("Выходим из игры. Пока!")
            break

        if first == "список":
            continue

        if first not in my_elements:
            print(f"Элемент '{first}' у тебя нет!")
            continue

        second = input("\nВведи второй элемент: ").strip().lower()

        if second == "стоп":
            print("Выходим из игры. Пока!")
            break

        if second not in my_elements:
            print(f"Элемент '{second}' у тебя нет!")
            continue


        elem1 = Element(first)
        elem2 = Element(second)
        result = elem1 + elem2

        if result is not None:
            print(f"\n{first} + {second} = {result}!")
            if result not in my_elements:
                my_elements.append(result)
                print(f"Новый элемент '{result}' добавлен в твою коллекцию!")
            else:
                print(f"Элемент '{result}' у тебя уже есть")
        else:
            print(f"\n{first} + {second} = ничего... Попробуй другое сочетание!")

        print(f"\nВсего открыто элементов: {len(my_elements)}")


play()