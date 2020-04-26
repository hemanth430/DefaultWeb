#Implementing the abstract base class 
#You want to write a programe to compute the area of shapes such as square and rectangle 

form abc import ABCmeta abstractmethod

class Shape(metaclass = ABCmeta):
	@abstractmethod
	def area(self):
		return(0)


class Square(Shape):
	side = 4 
	def area(self):
		print(self.side * self.side )
		
class Rectangle(Shape):
	width = 5 
	length = 10 
	def area(self):
		print(self.width * self.length)
		
square = Square()
rectangle = Rectangle()


square.area()
rectangle.area()

		