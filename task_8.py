# Задачи на файлы

# 1.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла
# добавлен восклицательный знак.
# file = open(file="test.txt", mode="w")
# for i in range(1, 11):
#     file.write(str(i)+" string of text\n")
# file.close()
#
# file = open("test.txt", encoding="utf-8")
# for line in file:
#     print(line.rstrip() + "!")
# file.close()
# 2.	Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа.
# Затем записать их произведение в файл output.txt.
# file = open(file="input.txt", mode="w")
# for i in range(1, 11):
#     file.write(str(i)+' ')
# file.close()
# file = open(file="input.txt")
# data = file.read().split()
# data = list(map(int, data))
# prod = 1
# for el in data:
#     prod *= el
# file.close()
# file = open(file="output.txt", mode="w")
# file.write(str(prod))
# file.close()
# 3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
# цену единицы и дату поступления товара на склад. Вывести список товаров, хранящихся больше месяца
# и стоимость которых превышает 1 000 000 р.


# 4.	Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений
# кортеж состоящий из 2-ух элементов – имя(str) и возраста(int). Сделать 5-6 элементов словаря и
# записать данный словарь на диск в файл json формата
import json

ages_info = {
    10000: ("Anna", 30),
    20000: ("Alex", 25),
    30000: ("Peter", 15),
    40000: ("Susan", 14),
    50000: ("Eddie", 10),
    60000: ("Lucy", 8)
}
with open("ages.json", "w") as file:
    json.dump(ages_info, file)
# 5.	Прочитать сохранённый json – файл и записать данные на диск в csv файл. Первое значение
# каждой строки должно начинаться со слова person, значения разделить ;
import csv
with open("ages.json") as file:
    data = json.load(file)
with open("ages.csv", "w") as csv_file:
    for key, value in data.items():
        csv.writer(csv_file).writerow(['person', *value])

# Задачи на исключения
#
# 6.	Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
# x = (1, 2, 5, 7)
# x = x  / 2
# print(x)
# x = (1, 2, 5, 7)
#
# try:
#     print(x = x / 2)
# except Exception as e:
#     print("Some Exception: ", e)

# 7.	Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента,
# которого нет в списке.
# some_lst = [1, 2, 3, 4, 5]
# try:
#     print(some_lst[3])
# except IndexError:
#     print("IndexError!!!")

# 8.	Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку
# и число.
# def func_concat(str1: str, str2: str) -> str:
#     return str1 + str2
# try:
#     print(func_concat("grey ", 1))
# except TypeError:
#     print("TypeError is not allowed")

# 9.	Напишите программу которые будет ловить FileNotFoundError, когда вы пытаетесь открыть файл
# для чтения, которого не существует.
# try:
#     with open("test.txt", "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found")

# 10.	Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
# когда пользователь пытается удалить элемент которого нет в списке.
# def delete_elem(lst: list, elem) -> list:
#     if elem not in lst:
#         raise TypeError(f"There's no element: {elem} in the list")
#
#     lst.remove(elem)
#     return lst
#
#
# some_lst = ["Reepicheep", "Caspian", "Trumpkin", "Pattertwig", "Peepicheek", "Trufflehunter"]
# try:
#     new_list = delete_elem(some_lst,"aspian")
#     print(new_list)
#
# except TypeError as e:
#     print("TypeError")
#     print(e)

# Дополнительные задачи *
#
# 11.	Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое. Для решение вам необходимо открыть файл
# для чтения 7.txt .
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3
#
# 12.	Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает
# из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит
# обратную операцию, получая исходный текст. Для решение вам необходимо открыть файл для чтения 8.txt .
#
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# Aaabbbbcceeeeeeeeeeb
#
#
#
