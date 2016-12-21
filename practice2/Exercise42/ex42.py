## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

pass
class Dog(Animal):

    def __init__(self, name):
        pass
        self.name = name

pass
class Cat(Animal):

    def __init__(self, name):
        pass
        self.name = name

pass
class Person(object):

    def __init__(self, name):
        pass
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

pass
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        pass
        self.salary = salary

pass
class Fish(object):
    pass

pass
class Salmon(Fish):
    pass

pass
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

pass
satan = Cat("Satan")

pass
mary = Person("Mary")

pass
mary.pet = satan

pass
frank = Employee("Frank", 120000)

pass
frank.pet = rover

pass
flipper = Fish()

pass
crouse = Salmon()

pass
harry = Halibut()