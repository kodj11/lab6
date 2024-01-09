class Rectangle:
    
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        
    def __del__(self):
        print(f"Деструктор для объекта {self}")
        
    def get_area(self):
        return self.width * self.height
    
    def left(self):
        return self.x
    
    def right(self):
        return self.x + self.width
    
    def bottom(self):
        return self.y
    
    def top(self):
        return self.y + self.height
    
    def __mul__(self, other):
        x1 = max(self.left(), other.left())
        y1 = max(self.bottom(), other.bottom())
        x2 = min(self.right(), other.right())
        y2 = min(self.top(), other.top())
        
        if x2 <= x1 or y2 <= y1:
            return Rectangle(0, 0)
        
        return Rectangle(x2 - x1, y2 - y1)
    
    def __gt__(self, other):
        return self.get_area() > other.get_area()
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()
    
    def __str__(self):
        return f"Rectangle({self.left()},{self.bottom()},{self.width},{self.height})"
        
r1 = Rectangle(3, 4)
r2 = Rectangle(2, 5)

print("Прямоугольник 1: (3, 4)")
print("Прямоугольник 2: (2, 5)")

intersection = r1 * r2

print(f"Пересечение: {intersection}")

print(f"Площадь прямоугольника 1: {r1.get_area()}")
print(f"Площадь прямоугольника 2: {r2.get_area()}")

if r1 > r2:
    print("Площадь прямоугольника 1 больше")
else:
    print("Площадь прямоугольника 2 больше")
