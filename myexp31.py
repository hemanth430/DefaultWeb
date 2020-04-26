#Check if any employee has achieved his weekly target or not 

class Employee:
	name = "Ben"
	designation = "Sales Executive"
	SalesMadeThisweek = 6 
	def hasAchievedTarget(self):
		if self.SalesMadeThisweek >= 5:
			print "Target has been Achieved"
			
		else:
			print "Target has not been Achieved"
			
employeeOne = Employee() #This process of creation an object is also called as object instantiation 
print employeeOne.name

print employeeOne.hasAchievedTarget()

employeeTwo = Employee()

print employeeTwo.name