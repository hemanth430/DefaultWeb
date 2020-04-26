class Employee:
	def employeeDetails(self):
		self.name = "Ben"
	
	@staticmethod
	def Welcomemessage():
		print("Welcome to our orgonization")
		
		
employee = Employee()

employee.employeeDetails()

print (employee.name) 

employee.Welcomemessage()

