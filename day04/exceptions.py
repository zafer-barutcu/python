try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test Finished')
print("----------------------------")

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2])
except:
    print('index number is too large')
else:
    print('index number is valid')

try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print("It is a stntax error")
except OSError:
    print("It is an operating system error")
except ArithmeticError:
    print("It is an arithmetic error")
finally:
    print('Finally block')
"""
throw for manually throwing exception
throws: for exception handling (in method signature) for checked exceptions

Python does not give error during writing code
throw = raise in Python

"""

print("----------------------------")

raise LookupError('Invalid entry')  # should be in a block




