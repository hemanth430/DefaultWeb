class Square:
	def __init__(self,side):
		self.side = side 
		
	def __add__(squareone,squaretwo):
		return ((4 * squareone.side) + (4 * squaretwo.side))
		
	
squareone = Square(5) #Sum of sides of first square is 4 * 5  which is 20 
squaretwo = Square(10) #Sum of sides of second square is 4 * 10 which is 40 

#We need to have a mechanism in which we need to add this 20 and 40 and print the result as 60 

print ("Sum of sides of both the squares: ", squareone + squaretwo)

