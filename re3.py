class PreciousStone:
	numberofpreciousstones=0 
	preciousstonecollection = [] 
	def __init__(self,name):
		self.name = name
		#Increment the number of precious stones 
		PreciousStone.numberofpreciousstones += 1 
		#Append the precious stone to the list if total number of stones are less than 5 
		if PreciousStone.numberofpreciousstones <= 5:
			PreciousStone.preciousstonecollection.append(self)
		else:
			#If more than 5 stones are present,delete the first one and store the new one 
			del PreciousStone.preciousstonecollection[0]
			PreciousStone.preciousstonecollection.append(self)
			
	@staticmethod
	def displaypreciousstones():
		for preciousstone in PreciousStone.preciousstonecollection:
			print (preciousstone.name, end = ' ' )
		print()
	
preciousstoneone = PreciousStone("Ruby")
preciousstonetwo = PreciousStone("Emerland")
preciousstonethree = PreciousStone("sapphire")
preciousstonefour = PreciousStone("Diamond")
preciousstonefive = PreciousStone("Amber")
preciousstonefive.displaypreciousstones()

preciousstonesix = PreciousStone("Onyx")
#print all the stones after deleting the first one 
preciousstonesix.displaypreciousstones()
