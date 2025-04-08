from Student import Student
from Employee import Employee

student = Student("Alex", 30, "English", 3 ,70)
print("This is from programmer 1")
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









