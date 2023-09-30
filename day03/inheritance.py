class Person:
    def __init__(self, name: str, age: int):  # strongly recommended to provide argument data types
        self.name = name
        self.age = age

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):  # for initializing, need super() method
    def __init__(self, name: str, age: int, job_title: str, company_name: str = None, salary: int = None):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class Developer(Employee):

    def __init__(self, name: str, age: int, job_title: str = 'Software Developer', company_name: str = 'Unknown'):
        super().__init__(name, age, job_title)
        company_name = company_name

    def work(self):
        print(f'{self.job_title}{self.name} is coding')


class Teacher(Employee):

    def __init__(self, name: str, age: int, job_title: str = 'Teacher', company_name: str = "sfdsfsd" ):
        super().__init__(name, age, job_title, company_name)

    def work(self):
        print(f'{self.name} is working')


employee1 = Employee("hAZEL", 27, "QA")

developer1 = Developer('Daniel', 35, 'Python Developer')

teacher = Teacher('Breanna', 45, 'Math Teacher')

print(employee1)
print(developer1)

employee1.work()
developer1.work()
teacher.work()
