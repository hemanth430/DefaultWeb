#Check if employee has achieved weekly target or not 

class Employee:
	name = "Hemanth"
	designation = "Sales Executive"
	SalesMadeThisWeek = 6
	#Actions of your requirements will be methods of your class 
	
	def HasAcheivedTarget(self):
			if self.SalesMadeThisWeek >= 5:
				print("Target Has Been Achieved")
			else:
				print("Target Has not been Achieved")
				
employeeOne = Employee()

employeeTwo = Employee()



