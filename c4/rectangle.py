class Rect:
    def __init__(self, length, breadth):
        self._l = length
        self._b = breadth

    def area(self):
        a = self._l * self._b
        return a

    def __lt__(self, obj):
        if (self.area() < obj.area()):
            return "The area of Rectangle1 is less than Rectangle2"
        else:
            return "The area of Rectangle2 is less than Rectangle1"


print("RECTANGLE 1")
l = int(input("Enter the length of rectangle1:"))
b = int(input("Enter the breadth of rectangle1:"))
obj1 = Rect(l, b)
print("The area is : ")
print(obj1.area())
print("RECTANGLE 2")
l = int(input("Enter the length of rectangle2:"))
b = int(input("Enter the breadth of rectangle2:"))
obj2 = Rect(l, b)
print("The area is : ")
print(obj2.area())
print("Now comparing the rectangles")
print(obj1 < obj2)
