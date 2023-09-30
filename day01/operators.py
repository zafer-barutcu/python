# arithmetic +, -, /, %
print(10 - 2)
print(10 + 2)
print(10 * 2)
print(10 / 3)  # in Java it returns int
print(10 / 2)  # in Python returns float
print(10 % 3)

print(int(100 / 2))

# shorthand assignment operators: =, +=, -=, *=, /=, %=
a = 100
a = 200
print(a)

a += 100
print(a)
a -= 100
print(a)
a /= 2
print(a)

# logical operator: and, or, not  can be used for grouping number of elements as well
s = 'Hello World'
print('H' and 'W' in s)
print(True or False)
s = 'Java Python C# C++'
print('Java' or 'Ruby' in s)

age = 29
citizenship = 'USA'
is_eligible = age >= 18 and citizenship == 'USA'
print(is_eligible)

has_Java = 'Java' in s
print(has_Java)

print('Python' not in s)
print(not False)
print(not True)  #

print("-------------------------------------------")
s = 'Java'
s2 = 'Java'  # those 2 variables referencing to the same object
print(s is s2)  # True means are they re same objects (== operator of java)
