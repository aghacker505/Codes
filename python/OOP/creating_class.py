#instance variable and instance method
class Student:
    def __init__(self):
        self.name = 'Abhay'
        self.age = 19
        self.marks = 900

    #this is an instance method
    def talk(self):
        print("Hi, my name is", self.name)
        print("My age is", self.age)
        print("My marks are", self.marks)

# create an instance to Student class.
s1 = Student()

# call the method using instance.
s1.talk()