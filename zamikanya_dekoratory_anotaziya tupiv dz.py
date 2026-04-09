from typing import List, Callable, Union, Optional, Dict
import time
from functools import wraps

# 1. Функція з анотаціями типів
def add_numbers(a: int, b: int) -> int:
    return a + b

# 2. Замикання з генератором послідовності
def sequence_generator(start: int, step: int) -> Callable[[], int]:
    current = start
    def next_number() -> int:
        nonlocal current
        result = current
        current += step
        return result
    return next_number

# 3. Декоратор для логування
def log_calls(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with {args}, {kwargs}. Result: {result}")
        return result
    return wrapper

# 4. Замикання для підрахунку викликів
def call_counter(func: Callable) -> Callable:
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper

# 5. Декоратор для вимірювання часу виконання
def measure_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

# 6. Декоратор для перевірки типів
def type_check(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for a, t in zip(args, types):
                if not isinstance(a, t):
                    print(f"Type error: {a} is not {t}")
                    return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 7. Функція, що збільшує числа у списку
def increment_list(nums: List[int]) -> List[int]:
    return [x + 1 for x in nums]

# 8. Функція, що повертає довжину рядка
def string_length(s: str) -> int:
    return len(s)


# Тести
print(add_numbers(3, 4))   #1

gen = sequence_generator(10, 5)  #2
print(gen())  
print(gen())  

@log_calls
def multiply(a: int, b: int) -> int: #3
    return a * b

multiply(2, 3)  

@call_counter   #4
def greet(name: str):
    print(f"Hello, {name}!")

greet("Simon")
greet("Simon")  

print(increment_list([1,2,3]))  
print(string_length("Python"))  


@measure_time  #5
def slow():
    time.sleep(1)

slow()  


@type_check(int, int)  #6
def add(a, b):
    return a + b

add(2, 3)      
add(2, "3")    


print(increment_list([1,2,3])) #7


print(string_length("Python"))  #8