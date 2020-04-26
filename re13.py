class Employee:
	def setnumberofworkinghours(self):
		self.numberofworkinghours = 40 
	
	def displaynumberofworkinghours(self):
		print(self.numberofworkinghours)
		
		
class Trainee(Employee):
	def setnumberofworkinghours(self):
		self.numberofworkinghours = 45 
		
	def resetnumberofworkinghours(self):
		super().setnumberofworkinghours()
	
employee = Employee()
employee.setnumberofworkinghours()
print("Number of working hours of employee:", end = ' ')
employee.displaynumberofworkinghours()



trainee = Trainee()
trainee.setnumberofworkinghours()
print("Number of working hours of trainee:", end = ' ')
trainee.displaynumberofworkinghours()

trainee.resetnumberofworkinghours()
print("Number of working hours of employee after reset:", end = ' ')
trainee.displaynumberofworkinghours()


print("Number of working hours of trainee:", end = ' ')
trainee.displaynumberofworkinghours()





