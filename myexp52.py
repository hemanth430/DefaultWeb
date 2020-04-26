#Access Specifiers 
#public private and protected 
#public  ==> membername  
#protected ==> _membername 
#private ==> __membername 

class Car:
	numberofwheels = 4
	_color = "Black"
	__yearofmanufacture = 2020
	
class Bmw(Car):
	def __init__(self):
		print("Protected attribute color:",self._color)
		

car = Car()
print ("Public attribute number of wheels", car.numberofwheels)
bmw = Bmw()
print("Private attriubte year of manufacturer:", car._Car__yearofmanufacture)
