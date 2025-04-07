class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age
    
    def getPersonString(self):
        return "The person " + self.getName() + " is " + str(self.getAge()) + " years old"
    
    def printMyself(self):
        print(self.getPersonString())

if __name__ == "__main__":
    test_name = "test_name"
    test_age = 80
    person = Person(test_name, test_age)
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + person.getName())