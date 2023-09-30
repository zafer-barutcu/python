# import functions-->import everything
from functions import sum, calculate

# result = functions.sum(10, 20, 30, 40)
# print(result)
# print(functions.display_message())

result2 = sum(1, 2, 3, 4)
print(result2)

result3 = calculate(3, 5, "+")
print(result3)

print("--------------------------------------------")
import functions as u

u.sum(1, 1, 1, 1)
u.concat("dad", 12, "21", 12, "21")
u.calculate(23, 23, "*")
