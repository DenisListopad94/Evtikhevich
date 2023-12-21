# 1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию
# изменения этих переменных. Добавить функцию, которая находит сумму значений этих переменных,
# и функцию которая находит наибольшее значение из этих двух переменных.
# class TwoVars:
#     def __init__(self, var_1, var_2):
#         self.var_1 = var_1
#         self.var_2 = var_2
#
#     def display(self):
#         print(f"var_1: {self.var_1}")
#         print(f"var_2: {self.var_2}")
#
#     def change_var(self, new_var_1, new_var_2):
#         self.var_1 = new_var_1
#         self.var_2 = new_var_2
#
#     def sum_var(self):
#         return self.var_1 + self.var_2
#
#     def max_var(self):
#         return max(self.var_1, self.var_2)
#
#
# obj = TwoVars(7, 88)
# obj.display()
# obj.change_var(33, 777)
# print(obj.var_1, obj.var_2)
#
# print(obj.sum_var())
# print(obj.max_var())

# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение
# на единицу в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и
# произвольными значениями. Счетчик имеет два метода: увеличения и уменьшения, — и свойство,
# позволяющее получить его текущее состояние. Написать программу, демонстрирующую все возможности класса.
# class DecimalCounter:
#     def __init__(self, min_val=0, max_val=10, arbitrary_val=0):
#         self.min_val = min_val
#         self.max_val = max_val
#         self.arbitrary_val = arbitrary_val
#
#     def display_val(self):
#         print(self.arbitrary_val)
#
#     def increment(self):
#         self.arbitrary_val = min(self.arbitrary_val+1, self.max_val)
#
#     def decrement(self):
#         self.arbitrary_val = max(self.arbitrary_val-1, self.min_val)
#
#
# counter = DecimalCounter()
# counter.display_val()
#
# counter.increment()
# counter.increment()
# counter.increment()
# counter.display_val()
#
# counter.decrement()
# counter.display_val()
#
# counter_2 = DecimalCounter(50, 60, 55)
# counter_2.display_val()
# counter_2.decrement()
# counter_2.decrement()
# counter_2.decrement()
# counter_2.decrement()
# counter_2.decrement()
# counter_2.decrement()
# counter_2.display_val()
#
# counter_2.increment()
# counter_2.increment()
# counter_2.display_val()


# 3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
# поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
# class Shop:
#     def __init__(self):
#         self.products = []
#     def add_product(self, name, price, quantity):
#         new_product = Product(name, price, quantity)
#         self.products.append(new_product)
#         print(f"{name} added to the shop")
#     def remove_product(self, name):
#         for product in self.products:
#             if product.name.lower() == name.lower():
#                 self.products.remove(product)
#                 print(f"{name} removed from the shop")
#     def search_product(self, name):
#         for product in self.products:
#             if product.name.lower() == name.lower():
#                 print(f"{name} found, price: {product.price}, quantity: {product.quantity}")
#                 break
#         else:
#             print(f"{name} not found")
#
#
# shop = Shop()
#
# shop.add_product("Bread", 2.5, 100)
# shop.add_product("Milk", 1.95, 150)
# shop.add_product("Butter", 3.5, 200)
#
#
# shop.search_product("bread")
#
# shop.remove_product("bread")
#
# print("\nProducts available in the store:")
# for product in shop.products:
#     print(f"name: {product.name}, price: {product.price}, quantity: {product.quantity}")

# 4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную
# вместимость, которая выражается целым числом – количеством монет(capacity -вместимость),
# которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё
# какое-то количество монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид:
#
# class MoneyBox:
#     def__init__(self, capacity) :
#     #конструктор с аргументом- вместимость копилки
#     def can_add(self,v)
#     #True, если можно добавить v монет, False иначе
#     def add(self,v)
#     #положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            print(f"{v} coins added to the piggy bank")
        else:
            print("Can’t add coins, the piggy bank’s capacity is exceeded")

piggy_bank = MoneyBox(50)

while True:
    coins_to_add = int(input("Enter the number of coins to add (0 to exit): "))
    if coins_to_add == 0:
        break
    piggy_bank.add(coins_to_add)
    print(f"There are {piggy_bank.coins} coins in the piggy bank\n")

print(f"\nTotal in the piggy bank is: {piggy_bank.coins}")


# Дополнительные задачи
#
# 1.	Задача на взаимодействие между классами. Разработать систему «Интернет-магазин».
# Товаровед добавляет информацию о Товаре. Клиент делает заявку на товар, если товар есть в наличие
# в магазине то покупатель оплачивает товар иначе товаровед делает запрос на склад о наличии товара.
# 2.	Задача на взаимодействие между классами. Разработать систему «Вступительные экзамены».
# Абитуриент регистрируется на Факультет, сдает Экзамены. Преподаватель выставляет Оценку.
# Система подсчитывает средний бал и определяет Абитуриента, зачисленного в учебное заведение.
# 3.	Определить класс «Шахматная фигура» с ее координатами на шахматной доске, ее цветом
# (черный или белый), виртуальным методом «битья» другой фигуры, и унаследовать от него классы,
# соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь». Написать виртуальные методы «битья»
# другой фигуры, которые принимают координаты другой фигуры и определяют, может ли данная  фигура
# «бить» фигуру с теми (принятыми) координатами.
#
