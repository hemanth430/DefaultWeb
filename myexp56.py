#Overloading an operator 
#How to overload the addition operator 
class square():
	def __init__(self,side):
		self.side = side #initializing your instance attribute side with the parameter side 
		
	def __add__(squareone,squareTwo):
		return((4 * squareone.side) + (4 * squareTwo.side))
		
squareone = square(5)   #sum of sides of squareone is 5 * 4 = 20 
squareTwo = square(10) #sum of sides of squaretwo is 10 * 4 = 40 

print("sum of sides of both the squares", squareone + squareTwo)

