# Base class
class Person:
    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height=height

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("height",self.height)

# Derived class
class Teacher(Person):
    def __init__(self, name, age,height, subject):
        # Calling the parent constructor (Person)
        super().__init__(name, age,height)
        self.subject = subject

    def display(self):
        # Calling the parent display method
        super().display()
        print(f"Subject: {self.subject}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Creating objects of the classes
person1 = Person("John", 30,183)
teacher1 = Teacher("Alice", 35, 179,"Mathematics")

# Displaying information about the person and the teacher
print("Person Information:")
person1.display()

print("\nTeacher Information:")
teacher1.display()
teacher1.teach()
