class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@email.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_wordkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Shaswat','Dharaiya',50000)
emp2 = Employee('ABC','XYZ',65000)

emp1.set_raise_amt(1.06)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Shaswat-Dharaiya-80000'
emp_str3 = 'John-Dharaiya-75000'

# first, last, pay = emp_str1.split('-')

new_emp = Employee.from_string(emp_str1)
print(new_emp.email)
print(new_emp.pay)

import datetime
myDate = datetime.date(2021,4,10)

print(Employee.is_wordkday(myDate))