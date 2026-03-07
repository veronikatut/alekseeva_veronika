# Задание № 1

def bread(func):
    def wrapper(*args, **kwargs):
        print("Bread")
        func(*args, **kwargs)
    return wrapper

def salat(func):
    def wrapper(*args, **kwargs):
        print("Salat")
        func(*args, **kwargs)
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        print("Tomato")
        func(*args, **kwargs)
    return wrapper

@bread
@salat
@tomato
def make_sandwich():
    print("Meat")

make_sandwich()

# Задание № 2

def bread(func):
    def wrapper(*args, **kwargs):
        return "Bread\n" + func(*args, **kwargs) + "\nBread"
    return wrapper

def salat(func):
    def wrapper(*args, **kwargs):
        return "Salat\n" + func(*args, **kwargs)
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        return "Tomato\n" + func(*args, **kwargs)
    return wrapper

@bread
@salat
@tomato
def make_sandwich():
    return "Meat"

print(make_sandwich())

# Задание № 3

def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    wrapper.cache = cache_dict  # Доступ к кэшу

    return wrapper


@cache
def heavy_function(n):
    print(f"Вычисляем для {n}...")
    return n * n


print(heavy_function(5))
print(heavy_function(5))
print(heavy_function(10))
print(heavy_function(10))

print("Кэш:", heavy_function.cache)