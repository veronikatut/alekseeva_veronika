"""
    >>> foo(True, False)
    first_bool
    >>> foo(False, True)
    second_bool
    >>> foo(True, True)
    first_bool
    >>> foo(False, False)
    oops
"""

"""
Условный оператор
if
elif
else 
"""


def foo(f_bool, s_bool):
    if f_bool:
        print('first_bool')
    elif s_bool:
        print('second_bool')
    else:
        print('oops')

