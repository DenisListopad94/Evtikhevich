# 1)	Дано 3 числа. Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно. Если нет вывести False.
a = 15
b = 25
c = 10
if a < 0 or b < 0 or c < 0:
    print(True)
else:
    print(False)
# 2)	Верно ли что, целые n и k имеют одинаковую четность.
# n = 25
# k = 15
# if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
#     print("The numbers n and k have the same parity.")
# else:
#     print("The numbers n and k have different parity")

# 3)	Найти количество четных чисел среди заданных трех целых чисел.
# В ответе вывести количество четных чисел.
# lst = [25, 127, -111]
# even_count = 0
# for ind in range(len(lst)):
#     if lst[ind] % 2 == 0:
#         even_count += 1
# print("Among given", even_count, "even")
# 4)	Дано двузначное число. Определить является ли сумма его цифр двузначным числом. (Ответ: Да/Нет)
# two_digit = 40
# tens_digit = two_digit // 10
# units_digit = two_digit % 10
# digits_sum = tens_digit + units_digit
# if digits_sum // 10:
#     print('yes')
# else:
#     print('No')
# # 5)	Вывести на экран число "10" 20 раз столбиком.
# var = '10'
# times = 20
# print((var + '\n')*times)

# 6)	Дано число N. Составить программу выводящую кубы чисел от 1 до N в одну строку.
# N = 5
# lst = []
# n = 1
# while n <= N:
#     lst.append(str(n ** 3))
#     n += 1
# print(' '.join(lst))

# 7)	Найти произведение всех целых чисел от 5 до 20 включительно.
# first_number = 5
# last_number = 20
# integers_product = 1
# for integer_number in range(first_number, last_number + 1):
#     integers_product *= integer_number
# print("Product of integers from", first_number, "to", last_number, "is", integers_product)

# 8)	Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9
# n = 15
# i = 1
# result = ''
# while i ** 2 < n:
#     result += str(i ** 2) + ' '
#     i += 1
# print(result)
# 9)	Дано натуральное число n. Найти значение минимальной цифры в данном числе.
# n = 273
# lst = []
# while n:
#     lst.append(n % 10)
#     n //= 10
#
# min_elem = lst[0]
# for ind in range(1, len(lst)):
#     if lst[ind] < min_elem:
#         min_elem = lst[ind]
# print(min_elem)

# 10)	Напишите программу, принимающую на вход год и выводящую "Високосный", если в этом году действительно 366 дней, и "Не високосный" иначе. Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на 400.
# year = 2012
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")
# 11)	*С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида "На лугу n коров", склоняя слово "коров" в соответствии с числом n. Проверяем большие числа!!!
# Sample Input:
# 7
# Sample Output:
# На лугу 1 корова
# На лугу 2 коровы
# На лугу 3 коровы
# На лугу 4 коровы
# На лугу 5 коров
# На лугу 6 коров
# На лугу 7 коров

# n = 9
# str_result = ''
# count = 1
# while count <= n:
#     str_result = "На лугу " + str(count) + " коров"
#     if count % 10 == 1 and not str(count).endswith('11'):
#         str_result += 'a'
#     if (count % 10 == 2 and not str(count).endswith('12') or
#         count % 10 == 3 and not str(count).endswith('13') or
#         count % 10 == 4 and not str(count).endswith('14')):
#         str_result += 'ы'
#     count += 1
#     print(str_result)

# 12)	*Числа Фибоначчи – известная числовая последовательность, в которой первые два члена равны единице, а каждый последующий получается сложением двух предыдущих. По введенному числу n выведите n чисел Фибоначчи через пробел.
# Sample Input:
# 8
# Sample Output:
# 1 1 2 3 5 8 13 21
# n = 9
# fib_lst = [0, 1]
#
# count = 1
# while count < n:
#     count += 1
#     fib_lst.append(fib_lst[count-1] + fib_lst[count-2])
# fib_lst.pop(0)
#
# print(*fib_lst)

# 13)	*В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов a человек, а в команде информатиков — b человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа a и b, каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа без остатка.
#
# a = 11
# b = 7
#
# if a > b:
#     max_number = a
#     min_number = b
# else:
#     max_number = b
#     min_number = a
# counter = max_number
# while max_number % min_number != 0:
#     max_number += counter
# print(max_number)
