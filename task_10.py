# 1.	Создайте систему управления задачами с использованием классов. Реализуйте классы
# "Task", "Project" и "ProjectManager". Каждая задача должна содержать описание, статус
# (выполнена или нет) и срок выполнения. Проект должен включать в себя список задач и методы
# для добавления новой задачи, отметки задачи как выполненной и вывода списка всех задач.


# class Task:
#     def __init__(self, description, due_date):
#         self.description = description
#         self._status = "Not Completed"
#         self.due_date = due_date
#
#     @property
#     def status(self):
#         return self._status
#
#     def is_completed(self):
#         self._status = "Completed"
#
#     def __str__(self):
#         return f"Description: {self.description}, Status: {self.status}, Due Date: {self.due_date}"
#
#
# class Project:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def task_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index].is_completed()
#             print(f"Task at index {index} is completed")
#         else:
#             print("Invalid task index")
#
#     def list_tasks(self):
#         print("Tasks in the project:")
#         for index, task in enumerate(self.tasks):
#             print(f"Task {index}: {task}")
#
# class ProjectManager:
#     def __init__(self):
#         self.projects = []
#
#     def create_project(self):
#         project = Project()
#         self.projects.append(project)
#         return project
#
#     def list_projects(self):
#         print("Projects in the manager:")
#         for index, project in enumerate(self.projects):
#             print(f"Project {index}")
#
# manager = ProjectManager()
#
# project1 = manager.create_project()
#
# task1 = Task("Prepare for the interview", "2023-12-11")
# task2 = Task("Complete task 10", "2023-12-11")
#
# project1.add_task(task1)
# project1.add_task(task2)
#
# project1.list_tasks()
#
# project1.task_completed(0)
#
# project1.list_tasks()
# 2.	Создайте систему для управления бронированием билетов в авиакомпании. Реализуйте классы
# "Passenger", "Ticket", "Flight" и "Airline ". Каждый пассажир должен иметь атрибуты, такие как
# имя и фамилия. Билет должен содержать информацию о пассажире и маршруте полета.
# Рейс должен включать в себя список зарезервированных билетов. Авиакомпания должна иметь методы
# для бронирования билета, отмены брони и отображения списка зарезервированных билетов.
# class Passenger:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
# class Ticket:
#     def __init__(self, passenger, flight):
#         self.passenger = passenger
#         self.flight = flight
#
# class Flight:
#     def __init__(self, route):
#         self.route = route
#         self.reserved_tickets = []
#
# class Airline:
#     def __init__(self):
#         self.flights = []
#
#     def book_ticket(self, passenger, flight):
#         ticket = Ticket(passenger, flight)
#         flight.reserved_tickets.append(ticket)
#         print(f"Tickets booked for {flight.route}: {passenger.first_name} {passenger.last_name}")
#
#     def cancel_reservation(self, ticket):
#         if ticket in ticket.flight.reserved_tickets:
#             ticket.flight.reserved_tickets.remove(ticket)
#             print(f"Reservation cancelled")
#         else:
#             print("There's no ticket in reservation")
#
#     def display_reserved_tickets(self):
#         for flight in self.flights:
#             for ticket in flight.reserved_tickets:
#                 print(f"{flight.route}: {ticket.passenger.first_name} {ticket.passenger.last_name}")
#
#
# passenger_1 = Passenger("Ivan", "Klepov")
# passenger_2 = Passenger("Artem", "Yan")
# passenger_3 = Passenger("Kate", "Y")
# passenger_4 = Passenger("Victor", "Yan")
# passenger_5 = Passenger("Yulia", "Klepova")
# passenger_6 = Passenger("Anton", "Klepov")
#
# airline = Airline()
# flight_1 = Flight("Krakow - Chicago")
# flight_2 = Flight("Warsaw - Rome")
#
# airline.flights.extend([flight_1, flight_2])
#
# airline.book_ticket(passenger_1, flight_1)
# airline.book_ticket(passenger_2, flight_1)
# airline.book_ticket(passenger_5, flight_1)
# airline.book_ticket(passenger_6, flight_1)
# airline.book_ticket(passenger_3, flight_2)
# airline.book_ticket(passenger_4, flight_2)
#
# airline.display_reserved_tickets()
#
# airline.cancel_reservation(flight_1.reserved_tickets[3])
#
# airline.display_reserved_tickets()
# 3.	Создать абстрактный класс «Alive». Определить наследуемые классы – «Fox», «Rabbit» и «Plant».
# Лисы едят кроликов. Кролики едят растения. Растение поглощают солнечный свет. Представители каждого
# класса могут умереть, если достигнут определенного возраста или для них не будет еды.
# Напишите виртуальные методы поедания и определения состояния живых существа
# (живые или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
# не больше 100 кроликов, 1000 растений
import time
from abc import ABC, abstractmethod

class Alive(ABC):
    @abstractmethod
    def count_alive_instance(self):
        pass

class Plants(Alive):
    def __init__(self, count_plants: int, koef_grown: int = 30, rabbit_food_koef: int = 10):
        self.count_plants = count_plants
        self.koef_grown = koef_grown
        self.rabbit_food_koef = rabbit_food_koef

    @property
    def count_alive_instance(self) -> int:
        return self.count_plants

    def year_grown(self):
        self.count_plants *= self.koef_grown

    def rabbits_food(self, count_rabbits):
        self.count_plants -= count_rabbits * self.rabbit_food_koef

class Rabbits(Alive):
    def __init__(self, count_rabbits: int, koef_reproduction: int = 15, rabbit_food_koef: int = 10,
                 fox_food_koef: int = 150):
        self.count_rabbits = count_rabbits
        self.koef_reproduction = koef_reproduction
        self.rabbit_food_koef = rabbit_food_koef
        self.fox_food_koef = fox_food_koef
    @property
    def count_alive_instance(self) -> int:
        return self.count_rabbits

    def year_reproduction(self):
        self.count_rabbits *= self.koef_reproduction

    def is_enough_food(self, count_plants):
        if self.count_rabbits * self.rabbit_food_koef > count_plants:
            rabbits_out = self.count_rabbits - count_plants // self.rabbit_food_koef
            print(f"warning!!! we need get out {rabbits_out} rabbits")
            time.sleep(5)
            self.count_rabbits -= int(rabbits_out * 1.5)

    def foxes_food(self, count_foxes):
        self.count_rabbits -= count_foxes * self.fox_food_koef

class Foxes(Alive):
    def __init__(self, count_foxes: int, koef_fox_reproduction: int = 3, fox_food_koef: int = 150):
        self.count_foxes = count_foxes
        self.koef_fox_reproduction = koef_fox_reproduction
        self.fox_food_koef = fox_food_koef

    @property
    def count_alive_instance(self) -> int:
        return self.count_foxes

    def year_fox_repr(self):
        self.count_foxes *= self.koef_fox_reproduction

    def is_enough_food(self, count_rabbits):
        if self.count_foxes * self.fox_food_koef > count_rabbits:
            foxes_out = self.count_foxes - count_rabbits // self.fox_food_koef
            print(f"warning!!! we need get out {foxes_out} foxes")
            time.sleep(5)
            self.count_foxes -= int(foxes_out * 1.5)

plants = Plants(450)
rabbits = Rabbits(80)
foxes = Foxes(2)

year = 1

while year <= 20:
    print(f"year {year}")
    print(f"count plants: {plants.count_alive_instance}")
    print(f"count rabbits: {rabbits.count_alive_instance}")
    print(f"count foxes: {foxes.count_alive_instance}")
    plants.year_grown()
    rabbits.year_reproduction()
    foxes.year_fox_repr()

    foxes.is_enough_food(rabbits.count_alive_instance)
    rabbits.is_enough_food(plants.count_alive_instance)

    rabbits.foxes_food(foxes.count_alive_instance)
    plants.rabbits_food(rabbits.count_alive_instance)

    year += 1

# Дополнительные задачи
#
# 4.	Разработайте программу, имитирующую работу транспортного агентства. Транспортное агентство имеет сеть филиалов в нескольких городах. Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и воздушным. Любой вид транспортировки имеет стоимость единицы веса на единицу пути и скорость доставки. Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.  Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый. Автомобильный транспорт можно использовать между любыми городами. Заказчики через случайные промежутки времени обращаются в один из филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки. Транспортное агентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
#
# -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
# -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
# -Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.

