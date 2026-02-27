# import functools
#
# def hleb(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Булка")
#         func(*args, **kwargs)
#         print("Булка")
#     return wrapper
#
# def sous(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Соус")
#         func(*args, **kwargs)
#         print("Соус")
#     return wrapper
#
# def salat(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Салат")
#         func(*args, **kwargs)
#     return wrapper
#
# @hleb
# @sous
# @salat
# def make_buten():
#     print("Колбаса")
#
# make_buten()

# c return
# import functools
#
# def hleb(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return "Булка\n" + func(*args, **kwargs) + "\nБулка"
#     return wrapper
#
# def sous(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return "Соус\n" + func(*args, **kwargs) + "\nСоус"
#     return wrapper
#
# def salat(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return "Салат\n" + func(*args, **kwargs)
#     return wrapper
#
# @hleb
# @sous
# @salat
# def make_buten():
#     return "Колбаса"
#
# print(make_buten())

# реализация кеша
# def my_cache(func):
#     cache_dict = {}
#
#     def wrapper(*args):
#         if args not in cache_dict:
#             cache_dict[args] = func(*args)
#         return cache_dict[args]
#
#     return wrapper
#
#
# @my_cache
# def heavy_function(n):
#     print(f"Вычисляем для {n}...")
#     return n * n
#
# @my_cache
# def heavy_function1(n):
#     print(f"Вычисляем для {n}...")
#     return n + n
#
#
# print(heavy_function(5))
# print(heavy_function(5))
# print(heavy_function1(10))
# print(heavy_function1(10))

# доступ к кешу

# def my_cache(func):
#    cache_dict = {}

#    def wrapper(*args):
#        if args not in cache_dict:
#            cache_dict[args] = func(*args)
#        return cache_dict[args]

#    wrapper.cache = cache_dict

#    return wrapper


#@my_cache
#def heavy_function(n):
#    print(f"Вычисляем для {n}...")
#    return n * n


#heavy_function(5)
#heavy_function(5)
#heavy_function(10)


#print(heavy_function.cache)