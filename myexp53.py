class Furniture:
	def __init__(self):
		self._typeofWood = "Teakwood"
		
class Chair(Furniture):
	def __init__(self):
		#super is used to call base class methods 
		#Here we are calling the init of our base class to initialize the type of wood as Teakwood 
		super().__init__()
		self.__numberofLegs = 4 
		
	def setWoodType(self, typeofWood):
		self._typeofWood = typeofWood
	
	def displayChairSpecification(self):
		print("This chair is made of {} and has {} legs".format(self._typeofWood, self.__numberofLegs))
		
chair = Chair()
print ("Would you like to change the type of wood from Teakwood? Y/N")
userchoise = input()
if userchoise == 'Y':
	print("Enter the type of wood you would like your chair to be made of")
	typeofWood = input()
	chair.setWoodType(typeofWood)
chair.displayChairSpecification()