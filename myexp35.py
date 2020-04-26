#How to fully initialize an object by making use of the special method in python called the init method 
class Employee:

	def __init__(self , name ):
		self.name = name
	
	
	
	def DisplayEmployeeDetails(self):
		print self.name 
		
employee = Employee("Hemanth")

employeeTwo = Employee("Sai")



employee.DisplayEmployeeDetails()
employeeTwo.DisplayEmployeeDetails() 
