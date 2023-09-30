# Dynamic Typing
"""
Python is much slower than Java
C is the fastest..very near to machine language
"""

# Initializing is must but if we don't know what should be assigned
name = None
print(name)
name = "James"
print(name)

print(type(name))

age = 25
print(type(age))
gpa = 3.5
print(type(gpa))
is_employed = True
print(type(is_employed))

# they are coming from class. In Java they are primitives and non primitives
"""
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
"""

# constructor used for not only for initializing but also for type casting
s = '25'
print(s * 5)
s = int(25)  # constructor name is same with class name. constructor returns a value but in Java
print(s)
