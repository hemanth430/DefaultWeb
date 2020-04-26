class Library:


	def __init__(self,listofbooks):
		self.availablebooks = listofbooks 
		
	def displayAvailableBooks(self):
		print()
		print("AvialableBooks:")
		for book in self.availablebooks:
			print(book)
		
	def lendbook(self,requestedbook):
	
		if requestedbook in self.availablebooks:
			print("you have now borrowed the book")
			self.availablebooks.remove(requestedbook)
		
		else:
			print("Sorry the book is not available in the list")
			
		
	def addBook(self,returnedbook):
	
		self.availablebooks.append(returnedbook)
		print("you are returned the book , thank you!")
	
	
class Customer:
	def requestbook(self):
		print("Enter a name of the book you would like to borrow:") 
		self.book = input()
		return self.book 
		
		
	def returnbook(self):
		print("enter the name of the book which you are returning?")
		self.book = input()
		return self.book 
		
		
library = Library(['Think and Grow Rich', 'Who will cry when you die', 'For one more day'])
customer = Customer()

while True:

	print("Enter 1 to display the available book")
	print("Enter 2 to request a book")
	print("Enter 3 to return a book")
	print("Enter 4 to exit")


	userchoise = int(input())
	if userchoise == 1 :
		library.displayAvailableBooks()
	elif userchoise == 2:
		requestedbook = customer.requestbook()
		library.lendbook(requestedbook)
	elif userchoise == 3:
		returnedbook = customer.returnbook()
		library.addBook(returnedbook)
	elif userchoise == 4:
		quit() 














		