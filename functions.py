from operator import itemgetter


# Объявляем функцию

def my_simple_func():
    """Эта функция ничего не делает"""


my_simple_func()


# Функция с позиционными аргументами

def print_upper_case(input_string: str):
    print(input_string.upper())


print_upper_case("hello, world!")


# Функция с именованными аргументами

def print_lines(line1, line2, line3):
    print(line1, line2, line3)


print_upper_case(input_string="строка, которую мы передали в именованный аргумент")

print_lines("first", "second", "third")
print_lines(line3="first", line2="second", line1="third")


# Функция с аргументами по умолчанию

def my_func(arg1, arg2, arg3=None):
    pass


print("какая-то строка", end="!\n")


# Возвращаем значение


def sum_numbers(a, b):
    return a + b


assert sum_numbers(5, 10) == 15

s = sum_numbers(5, 10)

print(s)

# Возвращаем несколько значений

import random


def return_numbers():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 10)

    return num1, num2, num3


nums = return_numbers()

print(nums)

num1, *other_nums = return_numbers()

print(num1, other_nums)

# Переменное количество аргументов на примере print


def custom_print(i):
    # print(args, sep=" | ")
    # print(*args, sep=" | ")
    print(i)
    i += 1
    # custom_print(i)


custom_print(0)
# custom_print(1, 2, 3, 4, 5)


def sum_numbers(**kwargs):
    print(kwargs)
    sum = 0
    for v in kwargs.values():
        sum += v
    print(sum)


sum_numbers(num1=10, num2=15, num3=25)


# Функция - тоже объект

p = print

p("hello, world!")


def get_age(user: dict):
    print("берем возраст", user["name"])
    return user["age"]


users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

print(get_age(users[0]))


users.sort(key=get_age, reverse=True)
import pprint

pprint.pprint(users)

users.sort(key=itemgetter("age"))

users.sort(key=lambda user: user["age"])
pprint.pprint(users)

# Сортируем по возрасту