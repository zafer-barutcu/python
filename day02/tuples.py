days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# should be () and single comma to make it tuple
# can not update element
# days[0] = 'Java' can not update values
print(type(days))
print(len(days))

print(days[0])  # forward index
print(days[-1])  # reverse index

working_days = days[:5]
print(working_days)
work_days = days[1:4]
print(work_days)
holidays1 = days[4:7]
holidays2 = days[-3:]
print(holidays1)
print(holidays2)

# content equal == , is-->referencing to the same object

tuple1 = (1, 2, 3)  # only one memory place allocated so they are same
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)
print(tuple1 is tuple2)

# merging tuples. In JAVA, have to 3rd array. But in python no need

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 5  # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple4)

reversed_tuple = days[::-1]
print(reversed_tuple)

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

print(days)
print(days.index('Wednesday'))

numbers = (10, 10, 10, 10, 20, 20, 30, 40, 50, 10)
print(numbers.count(10))
print("---------------------------------------------")

for x in days:
    print(x)

for x in range(0, len(days)):
    print(x)

print("---------------------------------------------")
for x in reversed(range(0, len(days))):
    print(x)

print("---------------------------------------------")

nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))

print(len(nested_tuple))

for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])
