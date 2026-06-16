#Animals sound
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

a1=Animal("Gary")
D1=Dog("Spencer")
C1=Cat("puddle")
a1.speak()
D1.speak()
C1.speak()

#Finding Area using Shape
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        super().__init__("Rectangle")
        self.l=l
        self.w=w
    def __str__(self):
        return f"{self.name}(length={self.l}, width={self.w})"
    def area(self):
        return (self.l*self.w)
class Circle(Shape):
    def __init__(self,r):
        super().__init__("Circle")
        self.radius=r
    def __repr__(self):
        return f"The radius of the circle is {self.radius}."
    def area(self):
        return (22/7*self.radius*self.radius)
C1=Circle(7)
R1=Rectangle(7,4)
print(C1)
print(f"Area of a circle is {C1.area()}")
print(R1)
print(f"Area of a rectangle is {R1.area()}")
# s1=Shape(5)
# print(s1.area())


#learn  
