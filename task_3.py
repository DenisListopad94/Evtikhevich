# 1.	Дана строка состоящая минимум из 6 символов.
some_cartoon = "Trolls Band Together"
# - Сначала выведите третий символ этой строки.
print(some_cartoon[2])
# - Во второй строке выведите предпоследний символ этой строки.
print(some_cartoon[-2])
# - В третьей строке выведите первые пять символов этой строки.
print(some_cartoon[:5])
# - В четвертой строке выведите всю строку, кроме последних двух символов.
print(some_cartoon[:-2])
# - В пятой строке выведите все символы с четными индексами
print(some_cartoon[::2])
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print(some_cartoon[1::2])
# - В седьмой строке выведите все символы в обратном порядке.
print(some_cartoon[::-1])
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print(some_cartoon[::-2])
# - В девятой строке выведите длину данной строки.
print(len(some_cartoon))

# 2.	Дано слово. Верно ли, что оно начинается и оканчивается на одну и ту же букву?
some_word = 'word'
print(some_word[0] == some_word[-1])

# 3.	Дано слово. Получить его часть, образованную второй, третьей и четвертой буквами.
given_word = "element"
print(given_word[1:4])

# 4.	Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.
fruit = 'яблоко'
print(fruit[1:5])
print(fruit[3:])

# 5.	В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
surname_name = "Ivanov Ivan"
name_surname = surname_name.split()
name_surname.reverse()
name_surname = " ".join(name_surname)
print(name_surname)

# 6.	Проверить является ли строка палиндромом.(шалаш).
is_palindrom = "12321"
print("Some string is palindrom:", is_palindrom == is_palindrom[::-1])

# 7.	Создайте список и извлеките из него списка второй элемент.
earth_oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
print("The second element of list is", earth_oceans[1])

# 8.	Вывести входит ли строка1 в строку2 (пример: employ и employment )
some_string = "playground"
substring = "ground"

index = some_string.find(substring)

if index != -1:
    print('"' + substring + '"' + " is a substring of a string " + '"' + some_string + '"')
else:
    print('"' + substring + '"' + " is not part of a string " + '"' + some_string + '"')

# 9.	*Дана строка которая содержит более 2 символов ‘f’. Строка может быть произвольной.
# Найдите индекс второй буквы ‘f’ в данной строке.
line = "My kitten is the fluffiest of all fluffy kittens"
index_1 = line.find("f")
index_2 = line.find("f", index_1 + 1)

if index_2 != -1:
    print("The second 'f' has index", index_2)
else:
    print("There's no second 'f' in this string")

# 10.	*Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {'1a': 20, '2b': 25, '2g': 18, '3a': 27, '3v': 19, '4a': 25, '4g': 30, '5a': 24, '9b': 21, '9a': 33}
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
school['4g'] = 28
print(school)
# б) в школе появился новый класс.
school['5b'] = 23
print(school)
# в) в школе был расформирован (удален) другой класс.
school.pop("3v")
print(school)
del school['2g']
print(school)
# г) Вычислите общее количество учащихся 9 классов в школе.

print("Total number of 9th grade students in the school =", school.get("9a") + school.get("9b"))

print(school["9a"] + school["9b"])
print(school)
print(list(school.values())[6] + list(school.values())[7])
