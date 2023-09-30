class Person:

    def __init__(self, name: str = 'Jimmy', age: int = 2):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age

    @property
    def person_name(self):  # person_name is also a variable outside the method
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    @person_name.setter  # calling variable instead of method is easier
    def person_name(self, name):

        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name must be string')
        self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age):
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'


person1 = Person()

person1.person_name = 'Daniel'

print(person1.person_name)
print(person1.person_age)

print(person1)
