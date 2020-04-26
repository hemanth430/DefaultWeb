#Implementing an abstract base class
from abc import ABCmeta, abstractmethod 
class Shape(metaclass = ABCmeta):	
	@abstractmethod
	def area(self):
		return 0 
	

class Square(Shape):
	side = 4 
	def area(self):
		print("Area of square:", self.side * self.side )
		
class Rectangle(Shape):
	width = 5 
	length = 10 
	def area(self):
		print("Area of Rectangle:" , self.width * self.length) 
		
square = Square() 
rectangle = Rectangle() 
square.area()
rectangle.area() 

#For every shape there is a method called as area which computes the area of that shape 
#That can be achieved by using of abstract base class 
#An abstract base class is a class which does not have a definition on its own, It has abstract 
#methods , which forces the implementation in its derived classes
