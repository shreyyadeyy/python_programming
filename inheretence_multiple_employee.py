#Parent class 1 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def display_Person(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

#Parent class 2
class Employee:
    def __init__(self,salary,employee_id):
        self.salary = salary
        self.employee_id = employee_id 

    def display_Employee(self):
        print(f"Salary:{self.salary}")
        print(f"Employee_id:{self.employee_id}")

#Child class inheriting from Person and Employee 
class Manager(Person, Employee):
    def __init__(self,name,age,salary,employee_id,department):
        #Initialize parent classes
        Person.__init__(self,name,age)
        Employee.__init__(self,employee_id,salary)

        #Manager-specific attribute
        self.department = department 

    #Manager-specific method 
    def display_Manager(self):
        print("\n---Manager Details---")
        self.display_Person()
        self.display_Employee()
        print(f"Department: {self.department}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting for the {self.department}")

    #Creating object of Manager class
manager1 = Manager("ABC", 35, 95000, "1000", "IT")

    #Calling methods 
manager1.display_Manager()
manager1.conduct_meeting()







    