class Shape:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
class Rectangle(Shape):
    def area(self):
        return(self.width * self.heigth)

print('Area of Rectangle Calculation \nPlease enter values for calculate.')
w = int(input('Enter width: '))
h = int(input('Enter height: '))
rect = Rectangle(w, h)
print('Rectangle area: ', rect.area())