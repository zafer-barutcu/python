for i in range(1, 6):
    print(i)
    if i == 3:
        break  # exist the loop

print("-----------------------")

for i in range(1, 6):
    if i == 3 or i == 4:
        continue  # skips to the next iteration
    print(i)

for i in range(1, 6):
    if i == 3 or i == 4:
        pass  # nothing going to happen.  can be used for abstraction as well
    print(i)


def function():
    pass


if True:
    pass
