class Employee:
	def employeeDetails(self):
		self.name = "Hemanth" 
		print (self.name)
		age = 32 
		print (age)
		
	def printemployeedetails(self):
		print ("Printing in another method")
		print (self.name)
		print (age)
		
employee = Employee()

employee.employeeDetails()

#The python interpretor converts it into this 

#Employee.employeeDetails(employee) 

employee.printemployeedetails()