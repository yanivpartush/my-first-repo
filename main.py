from Student import Student
from Employee import Employee

student = Student("Yaniv", 59, "Math", 3 ,90)
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









