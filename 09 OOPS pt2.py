#1 Define a Circle class to create a circle with radius r using th constructor. 
#  Define a Area method of the class which calculate the area of the circle.
#  Define a Perimeter method of the class which allows you to calculate the parimeter of the circle.
class circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * (self.radius**2)
    
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1 = circle(21)
print(c1.area())
print(c1.perimeter())

#2 Define a Employ class with attributes role, department & salary. This class also has a showdetails() method.
#  Create an Engineer class that inherits properties from Employee and has addition atributes name and age.
class Employ:
    def __init__(self, Role, Department, Salary):
        self.Role = Role
        self.Department = Department
        self.Salary = Salary
    
    def show_details(self):
        print("Role is:", self.Role,"Department is:", self.Department, "Salary is:",self.Salary)

Emp1 = Employ("Manager", "CS", "90000")
Emp1.show_details()

class Engineer(Employ):
    def __init__(self, name, age):
        super().__init__("Eng","IT","80000")
        self.name = name
        self.age = age
    def det(self):
        print("Name is:",self.name,"Age is:",self.age)

Eng1 = Engineer("Karan",26)
Eng1.show_details()
Eng1.det()

#3 Create a class called Order which store Items and its price. 
#  Use Dunder function __gt__() to convey that: Order1 > Order2 if Price of Order1 > Price of Order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("Apple",100)
odr2 = Order("Mangoo",80)
print(odr1>odr2)