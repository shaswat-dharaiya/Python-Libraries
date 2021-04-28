class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@email.com'

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first.lower(), self.last.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('Shaswat', 'Dharaiya', 50000)
emp2 = Employee('ABC', 'XYZ', 65000)

print(emp1.email)
print(emp1.fullname)

emp1.fullname = 'XYZ ABC'

print(emp1.fullname)
print(emp1.email)

del emp1.fullname
print(emp1.fullname)
