"""

    >>> names = ["Max"]
    >>> foo(names)
    Oops!
    >>> names.append("Stepan")
    >>> names.append("Sasha")
    >>> names.append("Rostics")
    >>> foo(names)
    Max Stepan
    >>> second_names = ["Oleg"]
    >>> foo(second_names)
    Oops!
    >>> foo("Sasha")
    Sasha
"""

"""
Конструкция match-case предназначена для операции сопоставления, но в отличие от других языков
программирования, данная конструкция имеет большую функциональность:

    1. Сопоставление с литеральными значениями строк / чисел
    2. Сопоставление списков
    3. Сопоставление по длине списка
    4. Сопоставление отдельных значений списков
    etc.
"""



def foo(data):
    match data:
        case [max, second_name, *_]:
            print(max, second_name)
        case "Stepan":
            print("Stepan")
        case "Sasha":
            print("Sasha")
        case _:
            print("Oops!")
