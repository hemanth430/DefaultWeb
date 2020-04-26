class Square:
	def __init__(self,side):
		self.side = side 
		
	#overload the exponential operator
	
	def __pow__(squareone, squaretwo):
		#Return side of squareone to the power of side of squaretwo 
		
		return squareone.side ** squaretwo.side 
		
squareone = Square(2)
squaretwo = Square(4)

print("squareone to the power of squaretwo is:", squareone ** squaretwo)