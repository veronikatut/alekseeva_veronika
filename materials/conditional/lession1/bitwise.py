"""
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    >>> bitwise_or(3, 4)
    7
    >>> bitwise_xor(5, 2)
    7
    >>> bitwise_shift_left(1, 5)
    32
    >>> bitwise_shift_right(64, 5)
    2
"""

"""
Побитовые операции

    & -> побитовое "и"
    | -> побитовое "или"
    ^ -> побитовое "xor"
    << -> побитовый сдвиг влево ( 1 << 10 == 1024 ~ 0b10000000000 )
    >> -> побитовый сдвиг вправо ( 1024 >> 5 == 16 ~ 0b10000 )

Операции производяться с целыми числами. Числа необходимо представлять в двоичном формате, то есть
операция 4 | 2 производится так, как будто бы вы попытались применить логическое сложение к 100 и 010,
результатом которого будет 110, и в результате операции вы получите число 6
"""

def print_binary_pretty_bitwise(number1: int, number2: int, action: str) -> int:
    number1, number2 = sorted((number1, number2), reverse=True)
    bnumber1 = bin(number1)[2:]
    bnumber2 = bin(number2)[2:]
    print(f"{action} {bnumber1}\n"
          f"  {bnumber2: >{len(bnumber1)}}")

def is_even(number: int) -> bool:
    # print_binary_pretty_bitwise(number, 2, "&")
    return not bool(number & 1)

def bitwise_or(number1: int, number2: int) -> int:
    # print_binary_pretty_bitwise(number1, number2, "|")
    return number1 | number2

def bitwise_xor(number1: int, number2: int) -> int:
    # print_binary_pretty_bitwise(number1, number2, "|")
    return number1 ^ number2

def bitwise_shift_left(number1: int, number2: int) -> int:
    # print_binary_pretty_bitwise(number1, number2, "|")
    return number1 << number2

def bitwise_shift_right(number1: int, number2: int) -> int:
    # print_binary_pretty_bitwise(number1, number2, "|")
    return number1 >> number2
