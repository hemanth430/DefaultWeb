class Car:
	def __init__(self):
		self.carFare = {'Hatchback' : 30, 'Sedan' : 50, 'SUV' : 100}
		
	def displayFareDetails(self):
		print ("cost per day:")
		print ("Hatchback: $", self.carFare['Hatchback'])
		print ("sedan : $", self.carFare['Sedan'])
		print ("SUV: $",self.carFare['SUV'])
		
	def calculateFare(self, typeofcar , numberofdays):
		return self.carFare[typeofcar] * numberofdays
		
		
car = Car() 
while True:
	print ("Enter 1 to display the fare details")
	print ("Enter 2 to rent a car")
	print ("Enter 3 to exit")
	
	userchoise = int(input())
	if userchoise == 1:
		car.displayFareDetails()
	elif userchoise == 2:
		print("Enter the type of the car you would like to borrow:")
		typeofcar = input() 
		print("Enter the number of days you would like to borrow the car")
		numberofdays = int(input())
		fare = car.calculateFare(typeofcar, numberofdays)
		print("Total payable amount: $", fare)
		print("Thank you!")
		
	elif userchoise == 3:
		quit() 
		
		