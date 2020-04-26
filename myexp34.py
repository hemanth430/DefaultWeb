#In this we will learn what are static methods and Instance methods 
#Instance methods - Instance Methods are the methods of your class that make use of the self paraemter to access and modify the 
#instance attributes of your class 

#All the methods we use untill now are the instace methods 

class Employee:
	def employeeDetails(self):
		self.name = "Hemanth"
		
	@staticmethod
	def WelcomeMessage():
		print "Welcome to our Organization"

employee = Employee()

employee.employeeDetails()

print employee.name

employee.WelcomeMessage()

#static methods are methods that do not take the default selfl parameter  

#Decoraters are functions that takes another function and extends their functionality 