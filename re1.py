class Employee:
	def employeedetails(self):
		self.name = "Hemanth"

	@staticmethod
	def welcomemessage():
		print("welcome to the orgonaizatoin:")
		
employee = Employee()
employee.employeedetails()
print (employee.name)
employee.welcomemessage()
