class Employee:	

	def __init__(self, name):
		self.name = name

	
	def displayemployeedetails(self):
		print(self.name)
	
employee = Employee("Mark")
employee.displayemployeedetails()
employeetwo = Employee("Mathew")
employeetwo.displayemployeedetails()
