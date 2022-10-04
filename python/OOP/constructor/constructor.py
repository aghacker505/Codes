class Employee:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def show_details(self):
        print("Name of the employee: " , self.name)
        print("Age of the employee: " , self.age)
        print("Gender of the employee: ", self.gender)
        print("Salary of the employee: ", self.salary)

e1 = Employee('Abhay', 20, "Male", 80000)
e1.show_details()