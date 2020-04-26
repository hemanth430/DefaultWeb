class Employee:

	def __init__(self, name):
		self.name = name
	
	def displayEmployeeDetails(self):
		print (self.name)
		
		
employee = Employee("Hemanth")

employeeTwo = Employee("Kumar")


employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()