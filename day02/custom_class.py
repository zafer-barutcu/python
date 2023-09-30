# classes only created for objects. in JAVA, it can be anything for
import numbers


class Employee:  # classes are dedicated for objects
    is_human = True  # static variables can be reached with class name
    planet = 'Earth'  # but in general, static variables are used in

    # if you set default value, parameters are optional
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):  # like this keyword in Java, it is not an argument
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


# in JAVA, we need 4 constructor to create the objects below
employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Alex', 'DevOps', 12)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

print(Employee.is_human)  # static variables can be reached with class name

employee1.work()
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)
