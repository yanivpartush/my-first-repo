from Person import Person

class Employee(Person):
    def __init__(self, name, age, field_of_work, salary):
        super().__init__(name, age)
        self.salary = salary
        self.field_of_work = field_of_work

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary
    
    def printEmployee(self):
        print(self.getPersonString() + ", The field is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))

    def printMyself(self):
        self.printEmployee()
    