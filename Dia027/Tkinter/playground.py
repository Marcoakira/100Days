''' add '''

# def add (*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(total)
#

# add(1,2,3,4,5, 22, 33, 44, 55, 66, 77, 88, 99, 100)

''' calculate the average of a list of numbers '''
# def calculate(n,**kwargs):
#     print(kwargs)
#     n += kwargs['add']
#     print(n)
#     n *= kwargs['multiply']
#     print(n)
#

# calculate(25, add=5, multiply=2)

''''''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'
#     def __repr__(self):
#         return f'Person({self.name!r}, {self.age!r})'
#
#
# p = Person('John', 25)
# print(p)

''' '''


class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')

my_car = Car(make='Ford', model='Fiesta', colour='red', seats=5)

print(my_car.make)
