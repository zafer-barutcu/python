from typing import final

PI = 3.14

@final
class Animal:
    pass

class Dog(Animal): # gives error due to final
    pass

