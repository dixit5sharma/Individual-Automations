class Employee():
    inflation = 1
    def __add__(self, value):
        self.salaryx=self.salaryx+value
        return self
    def __init__(self,f_name,l_name,position,salary):
        self.f_namex = f_name
        self.l_namex = l_name
        self.positionx = position
        self.salaryx = salary
    def __repr__(self):
        return f"{self.f_namex.capitalize()} {self.l_namex.capitalize()}"
    def __str__(self):
        return f"{self.f_namex.capitalize()}"
    def signum(self):
        return f'E{self.f_namex[:3].upper()}{self.l_namex[:3].upper()}'
    def email(self):
        return f'{self.f_namex.lower()}.{self.l_namex.lower()}@ericsson.com'
    def salary(self):
        return self.salaryx*Employee.inflation

a = Employee('ion','popescu','engineer',5000)

print(dir())
print(a)
print(type(a))
print(a.__dict__)
print(a.signum())
print(a.salary())
print(a.email())

Employee.inflation=1.1
print(a.salary())

print('{!s}'.format(a))
print('{!r}'.format(a))

a=a+200
print(a.salary())
