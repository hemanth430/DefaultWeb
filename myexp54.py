#polymorphism 
#Charecterstic of an entity to be able to present in more than one form 
class Employee:
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 40 
	
	def DisplayNumberOfWorkingHours(self):
		print(self.numberOfWorkingHours)
	
	
class Trainee(Employee):
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 45 

	def resetNumberofWorkingHours(self):
		super().setNumberOfWorkingHours()
	
	
	
employee = Employee()
employee.setNumberOfWorkingHours()
print ("Number of working Hours of employee:", end = ' ')
employee.DisplayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print ("Number of working hours of Trainee:", end = ' ')
trainee.DisplayNumberOfWorkingHours()
trainee.resetNumberofWorkingHours()	
print ("Number of working hours of Trainee after reset:", end = ' ')
trainee.DisplayNumberOfWorkingHours()