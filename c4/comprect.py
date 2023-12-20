class rect:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        self.a = self.l * self.b

    def peri(self):
        self.p = 2 * (self.l + self.b)

    def display(self):
        print("Area of rectangle : ", self.a)
        print("Perimeter of rectangle : ", self.p)

    def compare(self, obj2):
        if self.a == obj2.a:
            print("Areas are equal")
        elif self.a > obj2.a:
            print("Area1 is greater than Area2")
        else:
            print("Area2 is greater than Area1")


print("Rectangle 1")
l1 = int(input("Enter length of rectangle1:"))
b1 = int(input("Enter breadth of rectangle1:"))
print("Rectangle 2")
l2 = int(input("Enter length of rectangle2:"))
b2 = int(input("Enter breadth of rectangle2:"))

obj1 = rect(l1, b1)
obj2 = rect(l2, b2)

obj1.area()
obj1.peri()
obj2.area()
obj2.peri()
obj1.display()
obj2.display()
obj1.compare(obj2)
