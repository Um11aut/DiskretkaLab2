class Employee:
    def __init__(self, name="Test", age=18, position="Паразит", pay=10_000):
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay
    
    def getFields(self):
        print(self.name, self.age, self.position, self.pay)

def task18():
    emp = Employee("asd", 20, "Хз хто", 30_000)
    emp.getFields()