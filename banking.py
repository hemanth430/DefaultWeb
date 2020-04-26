from abc import ABCMeta, abstractmethod
from random  import randint


class Account(metaclass = ABCMeta):


	@abstractmethod
	def	createaccount():
		return 0 
		
	@abstractmethod
	def	authenticate():
		return 0 
		
	@abstractmethod
	def	withdraw():
		return 0 
	
	@abstractmethod
	def	deposit():
		return 0 
		
	@abstractmethod
	def	displaybalence():
		return 0 
	
class SavingsAccount(Account):
	
	def __init__(self):
		self.savingsaccounts = {}
		
		#[key][0] ==> name ; [key][1] ==> balance 
	def createaccount(self,name,initialdeposit):
		self.accountnumber = randint(10000,99999) 
		self.savingsaccounts[self.accountnumber] = [name, initialdeposit]
		
		print("Account creation has been successful.Your account number is ",self.accountnumber)
		
		
	def authenticate(self,name,accountnumber):
		if accountnumber in self.savingsaccounts.keys():
			if self.savingsaccounts[accountnumber][0] == name:
				print("Authentication successful")
				self.accountnumber = accountnumber
				return True 
			else: 
				print("Authentication Failed")
				return False 
				
		else:
			print("Authentication Failure")
			return False 
			
		
	def withdraw(self,withdrawalamount):
		if withdrawalamount > self.savingsaccounts[self.accountnumber][1]:
			print("Insufficient Balance")
		else:
			self.savingsaccounts[self.accountnumber][1] -= withdrawalamount
			print("Withdrawal was successful.")
			self.displaybalence()
			
	
	def deposit(self,depositamount):
		self.savingsaccounts[self.accountnumber][1] =+ depositamount
		print("Deposit was successful:")
		self.displaybalence()
		
	
	def displaybalence(self):
		print("Available Balance :" ,self.savingsaccounts[self.accountnumber][1])
		
			
		
savingsaccount = SavingsAccount()
while True:
	print("Enter 1 to create a new account")
	print("Enter 2 to access an existing account")
	print("Enter 3 to exit")
	
	userchoise = int(input())
	if userchoise == 1:
		print("Enter your name:")
		name = input() 
		print("Enter the initial deposit")
		deposit = int(input())
		savingsaccount.createaccount(name,deposit)
		
	elif userchoise == 2:
		print ("Enter your name :")
		name = input() 
		print("Enter your account number:")
		accountnumber = int(input())
		authenticationstaus = savingsaccount.authenticate(name,accountnumber)
		if authenticationstaus is True:
			while True:	
				print("Enter 1 to withdraw")
				print("Enter 2 to deposit")
				print("Enter 3 to display available balence")
				print("Enter 4 to go back to the previous menu")
				userchoise = int(input())
				if userchoise is 1:
					print ("Enter a withdrawal amount")
					withdrawalamount = int(input())
					savingsaccount.withdraw(withdrawalamount)
					
				elif userchoise is 2:
					print("Enter an amount to be deposited:")
					depositamount = int(input())
					savingsaccount.deposit(depositamount)
					
				elif userchoise is 3:
					savingsaccount.displaybalence()
				elif userchoise is 4:
					break 
				
	elif userchoise == 3:
		quit()
			
		
		
		

		