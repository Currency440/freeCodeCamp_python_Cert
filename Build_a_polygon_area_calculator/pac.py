class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
    
    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side 
    
    def __str__(self):
        return f'Square(side={self.width})'
    

rect = Rectangle(50, 7)
print(rect.get_picture())
rect2 = Rectangle(15, 10)
print(rect2.get_amount_inside(Square(5)))
rect2.width = 10
print(rect2)

