"""
    >>> is_truthy("Hello, World!")
    True
    >>> is_truthy("")
    False
    >>> is_falsy("Hello, World!")
    False
    >>> is_falsy("")
    True
"""

"""
Любые условные конструкции изначально ожидают в качестве своих операндов
значения типа bool. Но Python позволяет нам передавать в качестве операндов для проверки
условия любые значения, которые могут интерпритироваться как булевы.

Например, в конструкцию if {variable} можно передавать следующие значение (по правде и многие другие):

   0 -> False
   1 -> True
   322 -> True

   "" -> False
   "text" -> True

   [] -> False
   [""] -> True
   ["qwerty"] -> True

   etc.

Часто типы "контейнеры" при использовании в конструкции if elif else
рассматриваются как bool объекты по их длине:
   len(...) == 0 -> False
   len(...) > 0 -> True
"""

from typing import Any

def is_truthy(variable: Any) -> bool:
    if variable:
        return True
    return False

def is_falsy(variable: Any) -> bool:
    if not variable:
        return True
    return False
