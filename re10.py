class MusicalInstruments:
	numberofmajorkeys = 12 
	
class stringinstruments(MusicalInstruments):
	typeofwood = "ToneWood"
	
class Guitar(stringinstruments):
	def __init__(self):
		self.numberofstring = 6
		print("This guitar consists of {} strings, It is made of {} , and It can play {} keys".format(self.numberofstring, self.typeofwood,self.numberofmajorkeys))
		
guitar = Guitar() 
