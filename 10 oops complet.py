class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1

    def increase (self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.invrement = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)
    
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
        
    def __add__(self, other):
        return self.salary + other.salary
    
    def __repr__(self):
        return "Employee ({},{},{})" .format(self.fname, self.lname, self.salary)
    
    def __str__(self):
        return "The name of employee is {}" .format (self.fname)
    
    @property
    def email (self):
        if self.fname == None:
            return "Email not set"
        else:
            return self.fname + "." + self.lname +"@gmail.com"
        
    @email.setter
    def email(self, given_email):
        name_list = given_email.split("@")[0].split(".")
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        
class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

rohan = Employee("Rohan", "Das", 44000)
print(rohan.__dict__)
print(Employee.no_of_employee)

    

Employee.change_increment(2)
rohan.increase()
print(rohan.salary)

lovish = Employee.from_str("lovish-jackson-75000")
print(lovish.fname)

print(Employee.isopen("sunday"))

harry = Programmer("Harry", "Jackson", 99000, "Python", "5 Yrs")
print(harry.exp)
help(Programmer)

print(harry + rohan)

print(repr(harry))
print(str(harry))

if __name__ == "__main__":
    raj = Employee ("Raj", "Ch", 50000)
    aman = Employee ("Aman", "Kr.", 90000)
    print(raj.email, aman.email)
    raj.lname = "Kh"
    print(raj.email)
    raj.email = "Kh.raj@gmail.com"
    print(raj.email)