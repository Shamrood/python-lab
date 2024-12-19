class Dog:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method to display information about the dog
    def bark(self):
        print(f"{self.name} says woof!")

    # Method to get the dog's age in human years
    def human_years(self):
        return self.age * 7

# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 4)

# Accessing attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 4

# Calling methods
my_dog.bark()  # Output: Buddy says woof!
print(my_dog.human_years())  # Output: 28
