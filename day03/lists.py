groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(groceries_list)

# groceries_list[-2:] = 'Cherry' since string is sequence ->['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'C', 'h', 'e', 'r', 'r', 'y']

groceries_list[-2] = 'Cherry'
print(groceries_list)

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

numbers_list[2:6] = [1, 2, 3, 4]
print(numbers_list)
numbers_list[2:-2] = [300, 4000, 5, 6000]
print(numbers_list)
print('------------------------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

list1 = characters[2: len(characters) - 2]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:len(characters) - 1]
print(list3)
list4 = characters[3:]
print(list4)

characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
print(characters)

print("-----------------------------------------")
names = ["Conor", 'Steve', 'Hazel', 'Brenna']
for x in names:
    print(x)

print("-----------------------------------------")
num = [10, 20, 30, 40, 50, 60]
for i in range(0, len(num)):
    print(num[i])
    num[i] /= 5  # division operator always return float
    print(num)
print("-----------------------------------------")
for y in reversed(range(len(num))):
    print(num[y])

print("-----------------------------------------")
for x in num[::-1]:
    print(x)
print("-dfsdf----------------------------------------")
for x in num[0::]:
    print(x)

print("-----------------------------------------")

for x in reversed(num):
    print(x)

print("-----------------------------------------")

i = 0

while i < len(num):
    print(num[i])
    i += 1

for i in range(1, 6):
    i += 2
    print(i)

print("-----------------------------------------")
nums = [60, 550, 10, 20, 15, 5, 0]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

print("-----------------------------------------")
list1 = [10, 20, 30, 40]
# list1 = list(reversed(list1))

list1.reverse()
print(list1)

print("-----------------------------------------")

tuple_element = ('Java', 'Python', 'C#', 'Ruby')
print(tuple_element)

list_elements = list(tuple_element)
print(list_elements)
list_elements[-2] = 'C++'
print(list_elements)
list_elements.append('SWIFT')
print(list_elements)

tuple_elements = tuple(list_elements)
print(tuple_elements)

print("-----------------------------------------")
# if you have teh same context tuple object, the same place is allocated in the memory
# but in list, different places are allocated

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(list1 is list2)  # False because list is changeable

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)
print(tuple1 is tuple2)  # True because tuple unchangeable. Also, tuple is faster to access, less memory but size is fixed

groceries_list = ['Eggs', 'Milk', 'Rice']
groceries_list.append("Apple")
groceries_list.extend(("staff1", "staff2"))
groceries_list.remove('Eggs')  # removes one element at once
print(groceries_list)

groceries_list.pop()
print(groceries_list)
groceries_list.pop(1)
print(groceries_list)

# insert and append->adds after the last element
groceries_list.insert(2, 'APPLE')
print(groceries_list)

nums = [1, 2, 3, 4, 5, 6, 78, 1, 1, 2, 3, 4, 5, 5]
print(nums.count(1))

print("-----------Comprehensions------------------------------")

nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)

print("-----------------------------")
'''
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)
print(divisible_by_5)
better solution is below--comprehensions
'''

# tuple does not support comprehensions. need conversion
divisible_by_5 = [x for x in nums if x % 5 == 0]
print(divisible_by_5)

tuple1212 = tuple([x for x in nums if x % 5 == 0])
print(tuple1212)

print("-----------------------------")

even_numbers = [x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]
print(even_numbers)
print(odd_numbers)

print("-----------------------------")
names_with_java = ['Pyton', 'Java', 'JavaScript', 'Java', 'JAVA', 'JaVa', 'Ruby']
list_without_java = [x for x in names_with_java if x.lower() != 'java']
print(list_without_java)

print("-----------------------------")

