class Employee:
	def employeedetails(self):
		self.name = "Hemanth" 
		print("Name = ", self.name)
	
employee = Employee()
employee.employeedetails()

Employee.employeedetails(employee)