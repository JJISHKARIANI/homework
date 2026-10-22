class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary 

    @salary.setter
    def salary(self,value):
        self.__salary = value
    
    @salary.deleter
    def salary(self):
        del self.__salary  


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"name: {self.name}, department: {self.department}, salary: {self.salary}")




Employee_1 = Manager(name="ja", salary=10000000, department="Sum")
Employee_1.get_info()        
Employee_1.salary = 150000000000000000000
print(f'new salary: {Employee_1.salary}')
    