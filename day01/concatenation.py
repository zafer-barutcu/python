# class names and constants are UPPER case
name = 'James'
age = 26

print('His name is ' + name)
# print('His age is ' + age)  giving error + support just strings, so it is not recommended
print('His age is ' + str(age))  # working because str-str

# instead use format

print('His age is {}'.format(age))
print(f'His age is {age} and he is {age} years old')

# at the end of the string. Only append at the end of the string
print('Python', 3, "is awesome:", True)

