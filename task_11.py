# # Задачи на генераторы
# #
# # 1.	Напишите функцию fib, которая будет выводить последовательно каждое число Фиббоначи.
# # def fibonacci():
# #     f1 = 0
# #     f2 = 1
# #     while True:
# #         yield f1
# #         f1, f2 = f2, f1 + f2
# #
# # def print_fibonacci_number(numb):
# #     fib_generator = fibonacci()
# #     for _ in range(numb):
# #        print(next(fib_generator))
# #
# # print_fibonacci_number(8)
#
# # 2.	Напишите функцию simple, которая будет выводить поочерёдно простые числа от 2 до
# # введённого числа n до вызова исключения.
#
# # def simple(number: int) -> None:
# #     num = 2
# #     while num <= number:
# #         is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
# #
# #         if is_prime:
# #             yield num
# #         num += 1
# #
# # prime_generator = simple(20)
# #
# # try:
# #     while True:
# #         next_prime = prime_generator
# #         print(next(next_prime))
# # except StopIteration:
# #     print("Stop Iteration")
#
# # 3.	Напишите генератор для вывода всех совершенных чисел до 1000000000.
# # def perfect_numbers(limit):
# #     for num in range(2, limit + 1):
# #         sum_divisors = sum(i for i in range(1, num) if num % i == 0)
# #         if sum_divisors == num:
# #             yield num
# #
# #
# # perfect_numbers_generator = perfect_numbers(10000)
# #
# # for number in perfect_numbers_generator:
# #     print(number)
#
# # Задачи на повторение
# #
# # 4.	Исключить из строки группы символов, расположенные между первыми символами '{' и '}' вместе
# # со скобками. Если нет символа '}', то исключить все символы до конца строки после '{'.
# # Вывести символ, наиболее часто встречающийся в строке.
some_string = "Some text with {text which we have to delete} and we get clear text"
if '{' in some_string:
    start = some_string.find('{')
    result = some_string[:start] if '}' not in some_string else (
            some_string[:start] + some_string[some_string.find('}') + 1:])
    print(result)
else:
    print(f"There is no '{{' in the string: '{some_string}'")
letters = {}

for letter in some_string:
    if letter != ' ':
        letters[letter] = letters.get(letter, 0) + 1

max_key = max(letters, key=letters.get)
print("Letter Counts:", letters)
print("Character with Maximum Count:", max_key)
#
# # 5.	Ваш отдел работает над приложением, обращающимся к некоторому серверу. Вам поручили реализовать
# # некоторые запросы: GET, POST и DELETE. В контексте вашего приложения
# # POST-запрос добавляет строку на сервер, GET-запрос возвращает последнюю добавленную строку,
# # а DELETE-запрос удаляет последнюю добавленную строку. Дан список команд с запросами
# # (GET и DELETE не принимают параметров, а POST принимает строку или число),
# # список команд прерывается точкой. Выведите, что возвращает сервер, а также строки,
# # которые остались в списке, разделяя их через пробел.
# # Sample Input:
# # POST 12
# # POST 15
# # POST 81
# # GET
# # DELETE
# # DELETE
# # POST Stack Overflow
# # POST Recursion
# # DELETE
# # GET
# # .
# # Sample Output:
# # 81
# # Stack Overflow
#
# # class Server:
# #     def __init__(self):
# #         self.data = []
# #
# #     def post(self, value):
# #         self.data.append(value)
# #
# #     def get(self):
# #         if self.data:
# #             return self.data[-1]
# #         else:
# #             return None
# #
# #     def delete(self):
# #         if self.data:
# #             self.data.pop()
# #
# # def request_processing(requests):
# #     server = Server()
# #     output = []
# #
# #     for request in requests:
# #         if request.startswith("POST"):
# #             _, value = request.split(maxsplit=1)
# #             server.post(value)
# #         elif request == "GET":
# #             result = server.get()
# #             if result is not None:
# #                 output.append(result)
# #         elif request == "DELETE":
# #             server.delete()
# #
# #     return output
# #
# # requests = []
# # while True:
# #     request = input().strip()
# #     if request == '.':
# #         break
# #
# #     requests.append(request)
# #
# # output = request_processing(requests)
# # print('\n'.join(output))
#
# # 6.	Используя list comprehension. Сгенерируйте список как показано ниже:
# #
# # 1    1    1    1     1    1
# # 1    2    3    4     5    6
# # 1    3    6   10  15    21
# # 1   4   10   20  35    56
# # 1   6   21   56  126  252
#
# # rows = 5
# # cols = 6
# #
# # pascal_matrix = [[1 if i == 0 or j == 0 else 0 for j in range(cols)] for i in range(rows)]
# #
# # # Денис, пожалуйста, перепиши этот цикл for в виде list comprehension. У меня не получилось (((
# #
# # for i in range(1, rows):
# #     for j in range(1, cols):
# #         pascal_matrix[i][j] = pascal_matrix[i - 1][j] + pascal_matrix[i][j - 1]
# #
# # for row in pascal_matrix:
# #     print(' '.join(map(str, row)))
#
# # 7.	Коля понял, что у многих из его знакомых есть несколько телефонных номеров и нельзя хранить
# # только один из них. Он попросил доработать Вашу программу так, чтобы можно было добавлять к
# # существующему контакту новый номер или даже несколько номеров, которые передаются через запятую.
# #
# #  По запросу телефонного номера должен выводиться весь список номеров в порядке добавления,
# # номера должны разделяться запятой. Если у контакта нет телефонных номеров, должна выводиться строка
# # "Не найдено".
#
# # Sample Input:
# # Ben 89001234050, +70504321009
# # Alice 210-220
# # Alice
# # Alice 404-502, 894-005, 439-095
# # Nick +16507811251
# # Ben
# # Alex +4(908)273-22-42
# # Alice
# # Nick
# # Robert 51234047129, 92174043215
# # Alex
# # Robert
# # Sample Output:
# # 210-220
# # 89001234050, +70504321009
# # 210-220, 404-502, 894-005, 439-095
# # +16507811251
# # +4(908)273-22-42
# # 51234047129, 92174043215
# # phones = {}
# #
# # while True:
# #
# #     phone = input()
# #     name_phone = phone.split()
# #
# #     if phone == ".":
# #         break
# #
# #     if len(name_phone) >= 2:
# #         name = name_phone[0]
# #         if name in phones:
# #             existing_contacts = phones[name]
# #             existing_contacts += ', ' + ' '.join(name_phone[1:])
# #             phones[name] = existing_contacts
# #         else:
# #             phones[name] = ' '.join(name_phone[1:])
# #     else:
# #         if name_phone[0] in phones:
# #             print(phones[name_phone[0]])
# #         else:
# #             print(f"{name_phone[0]} not found")
# # 8.	Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
# # Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
# # Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов
# # — число выборщиков от этого штата. На практике, все выборщики от штата голосуют в соответствии
# # с результатами голосования внутри штата, то есть на заключительной стадии выборов в голосовании
# # участвуют штаты, имеющие различное число голосов. В первой строке дано количество записей.
# # Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов.
# # Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов.
# # Участников нужно выводить в алфавитном порядке.
# # Biden 10
# # Bush 20
# # Obama 30
# # Biden 5
# # Bush 3
# # Obama 40
# # Biden 18
# # Bush 13
# # Obama 15
#
#
# def voting_results(records):
#     candidate_votes = {}
#     print("Enter a list of candidates and votes for them from each state: ")
#     for i in range(records):
#         candidate, votes = input().split()
#         votes = int(votes)
#
#         if candidate not in candidate_votes:
#             candidate_votes[candidate] = 0
#
#         candidate_votes[candidate] += votes
#
#     sorted_candidates = sorted(candidate_votes.keys())
#     for candidate in sorted_candidates:
#         print(candidate, candidate_votes[candidate])
#
# records_number = int(input("Enter the number of entries with votes for candidates: "))
#
# voting_results(records_number)
#
# Дополнительные задачи из таска 9

# 1.	Задача на взаимодействие между классами.
# Разработать систему «Интернет-магазин».
# Товаровед добавляет информацию о Товаре.
# Клиент делает заявку на товар, если товар есть в наличие в магазине то покупатель оплачивает товар
# иначе товаровед делает запрос на склад о наличии товара.

# 2.	Задача на взаимодействие между классами. Разработать систему «Вступительные экзамены».
# Абитуриент регистрируется на Факультет, сдает Экзамены. Преподаватель выставляет Оценку.
# Система подсчитывает средний бал и определяет Абитуриента, зачисленного в учебное заведение.
# class Applicant:
#     def __init__(self, name):
#         self.name = name
#         self.exam_scores = []
#
#     def take_exam(self, scores):
#         self.exam_scores.extend(scores)
#
#     def define_average_score(self):
#         return sum(self.exam_scores) / len(self.exam_scores) if self.exam_scores else 0
#
#
# class Faculty:
#     def __init__(self, faculty_name, passing_grade):
#         self.faculty_name = faculty_name
#         self.passing_grade = passing_grade
#         self.applicants = []
#
#     def register_applicant(self, applicant):
#         self.applicants.append(applicant)
#
#     def assign_scores(self, applicant, scores):
#         applicant.take_exam(scores)
#         print(f"Scores assigned to {applicant.name}: {', '.join(map(str, applicant.exam_scores))}")
#
# class EntranceExam:
#     @staticmethod
#     def determine_enrollment(applicant, faculty):
#         average_score = applicant.define_average_score()
#         if average_score >= faculty.passing_grade:
#             print(f"Applicant {applicant.name} is enrolled in the {faculty.faculty_name} faculty")
#         else:
#             print(f"Applicant {applicant.name} was not enrolled in the {faculty.faculty_name} faculty")
#
# applicant1 = Applicant("Artem")
# applicant2 = Applicant("Ivan")
#
# faculty_it = Faculty("Information Technologies", 85)
# faculty_csn = Faculty("Computer Systems and Networks", 75)
#
# faculty_it.register_applicant(applicant1)
# faculty_csn.register_applicant(applicant2)
#
# faculty_it.assign_scores(applicant1, [79, 88, 90])
# faculty_csn.assign_scores(applicant2, [65, 75, 68])
#
# EntranceExam.determine_enrollment(applicant1, faculty_it)
# EntranceExam.determine_enrollment(applicant2, faculty_csn)

