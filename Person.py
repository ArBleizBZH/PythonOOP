
from employee import Employee
from datetime import datetime

class Person:

    species = "Homo Sapiens"
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age 
        Person.count += 1

    def display(self):
        print(f"{self.name} is a {self.age} years old {Person.species} ")

    @classmethod
    def show_count(cls):
        print(f"There are {cls.count} {cls.species}" )

    #python doesn't allow method overloading, so to instantiate the class from a dictionary 
    # or string etc,  we can use a class method instead
    @classmethod
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name, int(age)) #cls stands for class in method initializer so we can use it for instantiation instead of class name
    
    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], int(d['age'])) #cls stands for class in method initializer so we can use it for instantiation instead of class name

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name + ' ' + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name, age)

def callPerson():

    #Class variables and class methods can be called outside and prior to any class instances existing
    #class variable
    print(Person.species)
    #class methods
    Person.show_count()

    p1 = Person("John", 20)
    p2 = Person("Tim", 45)

    p1.display()
    p2.display()

    #class method makes less sense called from class instance, but it's still possible
    p1.show_count()

    #python doesn't allow method overloading, so to instantiate the class from a dictionary 
    # or string etc,  we can use a class method instead
    s = 'Jim, 23'
    p33 = Person.from_str(s)
    p33.display()

    d = {"name": "Jane", "age": 22}
    p44 = Person.from_dict(d)
    p44.display()
#callPerson()

def new_callPerson():
    emp1 = Employee('James', 'Smith', 1990, 6000)
    p5 = Person.from_employee(emp1)
    p5.display()
new_callPerson()