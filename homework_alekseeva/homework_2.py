# Задание №1

import json
import functools


def cache(filename, use_kwargs=False):
    def decorator(func):
        # Загружаем кэш из файла если он существует
        try:
            with open(filename, "r") as f:
                file_cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            file_cache = {}

        cache_dict = file_cache  # Объединяем текущий кэш с файловым

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Определяем ключ — позиционные или именованные аргументы
            if use_kwargs:
                key = str(sorted(kwargs.items()))
            else:
                key = str(args)

            if key not in cache_dict:
                cache_dict[key] = func(*args, **kwargs)
                # Сохраняем обновлённый кэш в файл
                with open(filename, "w") as f:
                    json.dump(cache_dict, f, indent=4)
                print(f"Вычисляем и сохраняем в кэш: {key}")
            else:
                print(f"Берём из кэша: {key}")

            return cache_dict[key]

        wrapper.cache = cache_dict
        return wrapper

    return decorator


# Позиционные аргументы
@cache(filename="cache_pos.json", use_kwargs=False)
def multiply(a, b):
    return a * b


# Именованные аргументы
@cache(filename="cache_kw.json", use_kwargs=True)
def power(base, exp):
    return base ** exp


multiply(3, 4)
multiply(3, 4)   # Из кэша
multiply(5, 6)

power(base=2, exp=10)
power(base=2, exp=10)  # Из кэша
power(base=3, exp=3)

print("Позиционный кэш:", multiply.cache)
print("Именованный кэш:", power.cache)


# Задание №2

import functools


def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    continue
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    continue
            # Если все попытки исчерпаны — последняя попытка тоже с обработкой
            try:
                return func(*args, **kwargs)
            except ValueError:
                pass
            except OSError:
                print(f"{func.__name__} raise OsError exception.")
        return wrapper
    return decorator