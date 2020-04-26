class Furniuture:
	def __init__(self):
		self.typeofwood = "TeakWood"
		
class Chair(Furniuture):
	def __init__(self):
		super().__init__()
		self.__numberoflegs = 4 
		
	def setwoodtype(self, typeofwood):
		self._typeofwood = typeofwood 
		
	def displaychairspecification(self):
		print("This chair is made of {} and has {} legs".format(self._typeofwood, self.__numberoflegs))
		
chair = Chair()
print("Would you like to change the type of wood from TeakWood:? Y/N")
userchoise = input()
if userchoise == 'Y' or 'y':
	print("Enter the type of wood you would like your chair to be made of")
	typeofwood = input() 
	chair.setwoodtype(typeofwood)
	
chair.displaychairspecification()