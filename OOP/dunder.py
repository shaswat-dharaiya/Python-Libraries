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
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return " {} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('Shaswat', 'Dharaiya', 50000)
emp2 = Employee('ABC', 'XYZ', 65000)

print(emp1)

print(repr(emp1))

print(emp1+emp2)
