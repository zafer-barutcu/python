s = 'Python Programming'  # string is also sequence

for each in s:  # for loop is for sequences
    print(each)
print("---------------------------------------------")

for i in range(0, len(s)):  # range exclude the last index
    print(s[i])

print("---------------------------------------------")

for i in range(-len(s), 0):  # range exclude the last index
    print(i)

print("---------------------------------------------")

for i in reversed(range(0, len(s))):
    print(s[i])

for i in reversed(range(-len(s), 0)):
    print(s[i])

print("---------------------------------------------")
result = ''
for x in s[::-1]:  # reversed order. Fastest way
    result += x
print(result)

for x in s[:-1]:  # regular order
    result += x
print(result)

for x in range(0, 10):
    print(x)

print("---------------------------------------------")

num = int(input('Enter a positive number:\n'))

while num <= 0:
    num = int(input('Enter a positive number:\n'))

print(f'you have entered {num}')

answer = input('Enter yes or no:\n')

while not (answer.lower() == "yes" or answer.lower() == "no"):
    answer = input('Please yes or no:\n')
print(f"you entered {answer}")
