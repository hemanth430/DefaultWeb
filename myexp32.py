#Here We will see different types of attributes which are class atributes and instance attributes 
# Different types of methods , which are static methods and instance methods 
#Fully initialize an object by using the special method in python called the init method 
#Also you will learn in detail about the self parameter 

#Class Attibutes are common to all instances of that class 
# For every object of the class which we create  the value of the class attribute will remain the same 
#Your class attriubte should contain the data which is common to all the instances of the class 
# Your class attribute should be something like , number of working hours , which could be common to all the employees in your company 

class Employee():
	numerOfWorkingHours = 40
	
employeeOne = Employee()
employeeTwo = Employee()

print employeeOne.numerOfWorkingHours
print employeeTwo.numerOfWorkingHours

#If you wanted to change the number of working hours , 
#We need to make use of name of your class and then access the class attribute 

Employee.numerOfWorkingHours = 45 

print employeeOne.numerOfWorkingHours
print employeeTwo.numerOfWorkingHours


#Now we will look at what is an instance attribute is 
#Instance attribute is specific to each instance of your class 

employeeOne.name = "John"
print employeeOne.name


#To create a name attribute for the employee two 

employeeTwo.name = "Marry"
print employeeTwo.name

#Now what if you try to change the name of your class attribute by making use of your name of the object 
# Which means instead of changing the value as employee.numberofworkinghours , we will do as employeeOne.numberofworkinghours
# and modify the value



employeeOne.numerOfWorkingHours = 40 

print employeeOne.numerOfWorkingHours

print employeeTwo.numerOfWorkingHours


























