class Car():	
	def __init__(self):
		#A dictionary to map the type of car and price per day 
		self.carFare = {'HatchBack': 30, 'sedan': 50, 'SUV': 100}
		
	def displayFareDetail(self):
		print("Cost per day: ")
		print("HatchBack: $",self.carFare['HatchBack'])
		print("sedan: $", self.carFare['sedan'])
		print("SUV: $", self.carFare['SUV'])
		
	def calculateFare(self, typeofcar, numberofdays):
		#calcuate the fare depending upon the type of the car and number of days requested by the user 
		return self.carFare[typeofcar] * numberofdays 
		
car = Car()

while True:
	print ("Enter 1 to display the fare details")
	print ("Enter 2 to rent a car")
	print ("Enter 3 to exit")
	
	userChoice = (int(input()))
	if userChoice == 1:
		car.displayFareDetail()
		
	elif userChoice == 2: 
		print ("Enter the type of car you would like to borrow:")
		typeofcar = input()
		print ("Enter the number of days you would like to borrow the car")
		numberofdays = int(input())
		fare = car.calculateFare(typeofcar, numberofdays)
		print ("Total Payable amount is $", fare)
		print ("Thank You!")
		
	elif userChoice == 3 :
		quit()
		
		
	
	
	