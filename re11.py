#Public ==> membername 
#Protected ==> _membername 
#Private ==> __membername 

class Car:
	numberofwheels = 4 

	_color = "Black"
	__yearofmanufacture = 2017
class Bmw(Car):
	def __init__(self):
		print("Protected attribute color:", self._color)
	

car = Car()
print("Public attribute number of wheels:",car.numberofwheels)
bmw = Bmw()
print("Private attriubute year of manufacture:",car._Car__yearofmanufacture)


