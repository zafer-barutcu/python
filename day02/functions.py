# if you create a function inside a class, it becomes method. But if you created in a module, it is function
# methods must be created in a class
import numbers


# functions and methods are slightly different.
# before functions, there is no indentation, but for methods
def display_message():  # generic function
    print("Hello World")
    print("Hi Human Being")


def value():
    return 10


display_message()
number = value()
print(number)


def return_int() -> int:
    return int('34')


print(return_int())


def divide(num1: int, num2: int):  # restrict the data type of parameter, you got warning not error
    return num1 + num2


print(divide('Java', 'Java'))


def add(num1: numbers, num2: numbers) -> numbers:  # abstract class for numbers
    return num1 + num2


print(add(10, 20))
print(add(10.5, 11.4))

print("*--------------------------")


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid Operator')
        return 0


print(calculate(10, 20, '+'))

print(calculate(100.5, 67, '/'))

print("*------------# no method overloading in Python #--------------")


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(1, 2, 3, 4))

print("----------------------------")


def concat(a: str, b, c='', d=3, e=""):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat("Zafer", "Barut")
concat("asa", 2, 3, 4, True)  # it works on this way

# in Python, there are myriad of methods vis a vis Java

"""
1.declaring
2.parameters
3.restricting parameter datat type
4.setting default value to parameter
5.restricting return type

Should digest Dynamic Typing
"""
