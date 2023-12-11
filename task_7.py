# 1.	Создайте lambda-функцию для нахождения подстроки в введённой строке.
# f = lambda any_str: "question" in any_str
# some_str = input("Enter some string: ")
# print(f(some_str))

# 2.	Проверьте число на чётность с помощью анонимной функции.
# f = lambda number: not number % 2
# print(f(101))
# 3.	Напишите lambda-функцию, которая будет приветствовать пользователя имя которого введено корректно,
# с большой буква. Иначе будет выводить сообщение о неверно введённом имени
# user_name = input("Enter user name: ")
# f = lambda user_name: user_name if user_name.istitle() else "Name is entered incorrectly"
# print(f(user_name))

# 4.	Напишите рекурсивную функцию digits(n), которая принимает натуральное число и возвращает строку
# с цифрами этого числа справа налево, разделяя их пробелами.
# Sample Input:
# 14623
# Sample Output:
# 3 2 6 4 1
# def digits(n: int):
#     n = str(n)
#     if n:
#         print(n[-1], end=" ")
#         digits(n[:-1])
#
# digits(12345)

# def digits(n: int):
#     n = str(n)
#     if not n:
#         return 0
#     else:
#         print(n[-1],end= " ")
#         digits(n[:-1])
#
# digits(13579)

# 5.	Напишите рекурсивную функцию is_power(n), которая возвращает True,
# если переданное натуральное число является степенью двойки, и False иначе.
# Sample Input:
# 1048576
# Sample Output:
# True
# def is_power(n:int)->bool:
#     if n == 1:
#         return True
#     elif not n % 2:
#         return is_power(n / 2)
#     else:
#         return False
#
# print(is_power(256))

# 6.	Дано натуральное число N. Вычислите сумму его цифр
# Sample Input:
# 14623
# Sample Output:
# 16
# def digits_sum(n: int)->int:
#     if n < 10:
#         return n
#     else:
#         return n % 10 + digits_sum(n // 10)
#
# print(digits_sum(14623))
# 7.	Дана функция, которая выводит все простые числа в промежутке от 1 до 100.
# Написать декоратор который будет проверять время работы этой функции. Задекорировать функцию.
# Вывести вpемя работы этой функции, а так же сами простые числа.
# number = int(input("введите число:"))
#
# for numb in range(2, number // 2 + 1):
#     if not number % numb:
#         print("составное")
#         break
# else:
#     print("простое")

# print([numb for numb in range(2, number + 1) if all(numb % i != 0 for i in range(2, int(numb // 2) + 1))])

# from datetime import datetime
# import time

#
# def elapsed(fun: callable) -> callable:
#     def inner(number: int):
#         start = datetime.now()
#         result = fun(number)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds() * 1000
#         print(f"elapsed: {elapsed}")
#         return result
#
#     return inner
#
#
# @elapsed
# def prime_numbers(number: int) -> list:
#     prime_lst = []
#     for numb in range(2, number + 1):
#         is_prime = True
#         for i in range(2, int(numb // 2) + 1):
#             if numb % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_lst.append(numb)
#     return prime_lst
#
#
# result = prime_numbers(100)
# print(result)

# 8.	Дана функция, которая проверяет введённый пользователем пароль. Задекорировать её так,
# чтобы при правильно введённом пароле она приветствовала пользователя.
def check_password(fun):
    def inner():
        user_password = "MyPass123"

        entered_password = input("Enter your password: ")
        if entered_password == user_password:
            return fun()
        else:
            print("Password is incorrect")
            return False
    return inner

@check_password
def greetings():
    print("Hello, User")

greetings()
# Дополнительные задачи:
#
# 9.	*Дано натуральное число n>1. Выведите все простые делители этого числа в порядке не убывания с учетом кратности. Используйте рекурсию!
# 18
# Sample Output:
# 2 3 3
# 10.	*Для переданного числа n выведите все перестановки чисел от 1 до n. Перестановками в математике называют все последовательности, полученные путем переупорядочивания элементов изначального набора. Например, для набора чисел 10, 11, 12 можно получить следующие перестановки:
# 10, 11, 12;    10, 12, 11;    11, 10, 12;    11, 12, 10;    12, 10, 11;    12, 11,10.
# Sample Input:
# 3
# Sample Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
#   3 2 1
# 11.	*Сочетанием из n элементов по k называется подмножество этих n элементов размера k. Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое. Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k). Пример: Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2. Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).Различных сочетаний три, поэтому C(3, 2) = 3. Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать. Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять. Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула: C(n, k) = C(n - 1, k) + C(n - 1, k - 1).                             Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
# Sample Input 1:
# 3 2
# Sample Output 1:
# 3
# Sample Input 2:
# 10 5
# Sample Output 2:
# 252
