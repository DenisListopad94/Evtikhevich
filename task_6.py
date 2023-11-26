# 1.	Напишите функцию которая будет генерировать список из 10 чисел степени 2 от 1 до 10.
# def power_two():
#     print([el**2 for el in range(1, 11)])
# power_two()

# 2.	Напишите функцию которая будет генерировать список всех трёхзначных чисел кратных 5 и 3.
# def divisible_5_3():
#     print([el for el in range(100, 1000) if el % 3 == 0 or el % 5 == 0])
# divisible_5_3()
# 3.	Программа получает на вход три числа через пробел — начало и конец диапазона, а также степень,
# в которую нужно возвести каждое число из диапазона. Напишите функцию которая сгенерирует и
# вернёт данный.
# def some_pow():
#     start, end, power = map(int, input("Enter start, end, power: ").split())
#     print(*[el ** power for el in range(start, end+1)])
# some_pow()
# Sample Input:
# 5 12 3
# Sample Output:
# 125 216 343 512 729 1000 1331 1728
#
# 4.	Напишите функцию, на вход которой подаётся список чисел одной строкой. Программа должна
# для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка,
# являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце
# этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список
# "13 6 9 15 7" (без кавычек).Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
# some_lst = list(map(int, input("Enter values: ").split()))
# def neighbour_sum(numbers_list: list)->list:
#     if len(numbers_list) == 1:
#         return(numbers_list)
#     new_lst = []
#     new_lst.append(numbers_list[1] + numbers_list[len(numbers_list) - 1])
#     for ind in range(1, len(numbers_list)-1):
#         new_lst.append(numbers_list[ind-1] + numbers_list[ind+1])
#     new_lst.append(numbers_list[len(numbers_list) - 2] + numbers_list[0])
#
#     return new_lst
# result_lst = neighbour_sum(some_lst)
# print(*result_lst)

# def sum_of_neighbors(numbers):
#     if len(numbers) == 1:
#         return numbers
#
#     result = []
#     for i in range(len(numbers)):
#         left_neighbor = numbers[(i - 1) % len(numbers)]
#         right_neighbor = numbers[(i + 1) % len(numbers)]
#         result.append(left_neighbor + right_neighbor)
#
#     return result

# Get input from the user
# input_list = list(map(int, input().split()))
#
# result_list = sum_of_neighbors(input_list)
# print(result_list)

# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10
#
# 5.	Напишите функцию, для нахождения минимального элемента из 2 чисел.
# С помощью данной функции найдите минимальное четырёх чисел.
# def min_value(val_1: int, val_2: int)->int:
#     if val_1 < val_2:
#         min_val = val_1
#         return val_1
#     else:
#         min_val = val_2
#         return val_2
# print(min_value(min_value(10, 115), min_value(2, -1000)))

# 6.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа и
# выведите результат работы этой функции.
# from math import sqrt
# def distance(x1: float, y1: float, x2: float, y2: float):
#     result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     return result
# x1, x2, y1, y2 = map(float, input("Enter the x and y coordinates of the start and end points: ").split())
# res = distance(x1, y1, x2, y2)
# print(f"{res}")
# 7.	Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число
# Фибоначчи. Ищем число Фиббоначи через цикл! Рекурсию не использовать!
# def fib(n: int):
#     fib_lst =[0, 1, 1]
#     if n <= 2:
#         return n
#     for ind in range(3, n+1):
#         fib_lst.append(fib_lst[ind-1] + fib_lst[ind-2])
#     return fib_lst[n]
# num = int(input("Enter n: "))
# result = fib(num)
# print(f"{result}")
# 8.	Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента
# целое число x и возвращающую самое маленькое целое число y, такое что:
# -y больше или равно x
# -y делится нацело на 5
# 10 - > 10
# 12,14,13 ->15
# Попробуйте решить без цикла!
# def closest_mod_5(x: int):
#     y = x if x % 5 == 0 else x + 5 - x % 5
#     return y
# print(closest_mod_5(1048))
# 9.	Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка.
# def modify_list(l:list):
#     ind = 0
#     while ind < len(l):
#         if l[ind] % 2 == 0:
#             l[ind] //= 2
#             ind += 1
#         else:
#             del l[ind]
#
# lst = [1, 15, 20, 25, 92]
# modify_list(lst)
# print(lst)

# Дополнительные задачи
# 10.	*В языке Python есть некоторые ограничения на имена переменных. Имена переменных
# -могут состоять только из цифр, букв и знаков подчеркивания.
# -не могут начинаться с цифры.
# Программист вводит строки с именами переменных. Для каждой переменной нужно вывести
# "Можно использовать", если ее имя корректно, или "Нельзя использовать", если это не так.
# Определив все нужные переменные, программист заканчивает ввод строкой "Поработали, и хватит".
# Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать,
# что программист использует только латинские буквы. # Не может содержать : ! @ # $ % ^ & * ()
# def check_variable(v:str) -> str:
#     for symb in v:
#         if symb in "!@#$%^&*()" or v[0].isdigit():
#             return f"{v} can not be used"
#         elif not (symb.isalnum() or symb == '_'):
#             return f"{v} can not be used"
#     return f"{v} can be used"
# while True:
#     some_str = input("Enter values names: ")
#     if some_str == "We've worked and that's enough":
#         break
#     else:
#         print(check_variable(some_str))
# 11.	*Сгенерировать список всех простых чисел до  100.
# number = 100
# print([numb for numb in range(2, number + 1) if all(numb % i != 0 for i in range(2, int(numb // 2) + 1))])


