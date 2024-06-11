class Circle:
    def __init__(self,radius) -> None:
        self.radius=radius
    
    def area(self):
        return (22/7)* self.radius **2
    
    def perimeter(self):
        return 2*(22/7)*self.radius

c1=Circle(21)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self,role,dept,salary) -> None:
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self, name,age) -> None:
        self.name=name
        self.age=age
        super().__init__("officer","computer","700000")
eng1=Engineer("elon musk",40)      
eng1.showDetails()

class Order:
    def __init__(self,item,price) -> None:
        self.item=item
        self.price=price
    
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=Order("chips",20)
odr2=Order("kurkure",50)
print(odr1>odr2)