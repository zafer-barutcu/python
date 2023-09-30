# String is immutable

name = 'Python'

print(len(name))
print(name[0])
print(name[-1])
print(name[-2])
print(name[len(name) - 1])
# data structures can be sliced as well
s = 'Java Programming Language'
print(s[5:16])
print(s[:3])

s4 = s[::-1]  # slices till the end. :: slices in reverse order.  : slices direct order
print(s4)

# s1 = 'Python Programming'
# s5 = str(reversed(s1))
# print(type(s5))
# reversed(s5)
# print(s5)

# slice without providing end index
s = 'Python Programming'
s6 = s[7:]  # by default, it slices the string from index 7 to the last character(inclusive)
print(s6)
print("----------------------")
# print(help(str))
print("----------------------")

s = 'python programming language'

print(s.capitalize())  # self keyword, ignore it. this keyword in java. no need to pass any argument

print(s.title())  # very good for titles :)

s = "    Python      Programming       "
s7 = s.lstrip()
print(s7)
s8 = s.rstrip()
print(s8)
s9 = s.strip()
print(s9)

s = 'JAVA HFJ'
print(s.index('A'))
print(s.rindex('A'))

s = 'Java Java'
s9 = s.replace('Java', 'Python')
print(s9)

s = 'C# C# Python'
s10 = s.replace(' C# ', ' Java ')
print(s10)

s = 'Java Java java Python Java Python'
number1 = s.count('Java')
number2 = s.count('Python')
number3 = s.lower().count('java')
print(number1)
print(number2)
print(number3)

s1 = 'java'
s2 = 'JAVA'

print(s1.lower() == s2.lower())  # or with uppercase, only way to check the same or not

s = 'Java'
print(s[0].islower())  # if it is lower or not
print(s[-1].isupper())  # if it is upper or not

s = 'a'
print(s.isalpha())  # True
s = '1'
print(s.isdigit())  # True

s = 'Java Python'
s1 = "sdf esfg"
print(s.istitle())
print(s1.istitle())

# if you create a function inside a class, it becomes method. But if you created in a module, it is function
# methods must be created in a class
