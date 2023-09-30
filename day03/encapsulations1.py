class Person:

    def __init__(self, name: str = "StringNone", age: int = 13):  # self is similar to this keyword but this can not declare a variable but self and accessing
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    def set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name must be string')

        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age {age}')
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'


# right now we are outside the class
person0 = Person()
print(person0.get_name())
print(person0.get_age())
print("------------------------")

person1 = Person('James0', 12)
print(person1.get_name())
print(person1.get_age())
print("------------------------")

person2 = Person('Hazel')
print(person2.get_name())
print(person2.get_age())

print(person0)
print(person1)
print(person2)
