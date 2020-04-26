#Understanding the self parameter , and the reason why we use it 
#We will create a method for the class intially without the self parameter 

class Employee():
	def employeeDetails(self):
		self.name = "Hemanth"
		print "Name = ", self.name
		self.age = 30 
		print "Age = ", self.age
		
	def printEmployeeDetails(self):
		print "Printing in Another Method"
		print "Name ", self.name
		print "Age = ", self.age
		
employee = Employee()
#Next we use this object to call the method employeeDetails 

employee.employeeDetails()

#The python interpreter converts to this way 
#Employee.employeeDetails(employee) So this is the shorthand notation for the line 11 for the function call 

employee.printEmployeeDetails()