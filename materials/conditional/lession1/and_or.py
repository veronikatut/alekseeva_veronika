"""
    >>> foo_or(True, False)
    True
    >>> foo_or(False, True)
    True
    >>> foo_or(True, True)
    True
    >>> foo_or(False, False)
    False
    >>> foo_or(1, 2)
    1
    >>> foo_or(2, 1)
    2
    >>> foo_or('', ['second'])
    ['second']
    >>> foo_or(['second'], True)
    ['second']
    >>> foo_or(False, '')
    ''

    >>> foo_and(True, False)
    False
    >>> foo_and(False, True)
    False
    >>> foo_and(False, False)
    False
    >>> foo_and(True, True)
    True
    >>> foo_and(1, 2)
    2
    >>> foo_and(2, 1)
    1
    >>> foo_and('', True)
    ''
    >>> foo_and(True, [])
    []

"""


"""
Логические операции с типами отличными от bool

Логические операции можно также применять с типами отличными от bool, как мы это делали в конструкции
if elif else и в тернарном операторе.

Результатом при использовании операторов or и and будет последний проверенный операнд.

При этом стоит заметить, что результатом выполнения в общем случае будет значение одного из операндов операторов,
а не значение типа bool (оператор not исключение).

"""

from typing import TypeVar, Any

FirstVariableType = TypeVar('FirstVariableType', bound=Any)
SecondVariableType = TypeVar('SecondVariableType', bound=Any)

def foo_or(variable1: FirstVariableType, variable2: SecondVariableType) -> FirstVariableType | SecondVariableType:
    return variable1 or variable2

def foo_and(variable1: FirstVariableType, variable2: SecondVariableType) -> FirstVariableType | SecondVariableType:
    return variable1 and variable2
