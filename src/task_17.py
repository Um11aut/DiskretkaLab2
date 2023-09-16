from enum import Enum

class Degree(Enum):
    Bomj = -1
    Bakalavr = 0
    Magistr = 1
    Aspirant = 2

    def __str__(self):
        return self.name.capitalize()

class Student:
    '''Зберігає особисті дані студента, email, name ...'''
    def __init__(self, name="John Doe", courses =[], number = 0, email = "", degree = Degree.Bomj):
        self.name = name
        self.courses = courses
        self.number = number
        self.email = email
        self.degree = degree
        print("Створено об’єкт для "+ name)
    
    def printDetails(self):
        # Виводить атрибути
        print("Ім’я: ", self.name)
        print("Курси: ", self.courses)
        print("Номер: ", self.number)
        print("Пошта: ", self.email)
        print("Сатус: ", self.degree)
    
    def enroll(self, course):
        # Додає навчальні курси

        self.courses.append(course)

def task17():
    student1 = Student("Mary", [], 123, "test@test.com", str(Degree.Bomj))
    newcourse = True
    while newcourse:
        print("Уведіть новий курс для", student1.name)
        c = input()
        student1.enroll(c)
        print("Чи хочите ви додати новий курс? Y - да, N - ні")
        j = input()
        if j == "N":
            newcourse = False
        elif j == "Y":
            newcourse = True

    student1.printDetails()