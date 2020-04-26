#class = library 
#Layers of abstraction => To display the available books , to lend a book , to add a book 

#class = customer 
#layers of abstraction => request for a book, return a book 

class Library: 

	def __init__(self,listofbooks):
		self.availableBooks = listofbooks
		
	def displayAvailableBooks(self):
		
		print ()
		print("Avilable Books:")
		for book in self.availableBooks:
			print (book)
	
	def lendBook(self, requestedBook):
		if requestedBook in self.availableBooks:
			print("you have now borrowed the book")
			self.availableBooks.remove(requestedBook)
		else:
			print("sorry the book is not availble in our list")
			
		
	def addBook(self, returnedBook):
		self.availableBooks.append(returnedBook) 
		print ("You have returned the book, Thank you!")
		
class Customer:
	def requestBook(self):
		print ("Enter the name of the book you would like to borrow")
		self.book = input() 
		return self.book
		
	def returnBook(self):
		print ("Enter the name of the book which you are returning:")
		self.book = input()
		return self.book 
		
library = Library(['Think and Grow Rich', 'Who will cry when you die', 'For one more day'])
customer = Customer()
while True:

	print ("Enter 1 to display the available books")
	print ("Enter 2 to request for a book")
	print ("Enter 3 to return a book")
	print ("Enter 4 to exit")


	userChoise = int(input())

	if userChoise == 1: 
		library.displayAvailableBooks()
		
	elif userChoise == 2: 
		requestedBook = customer.requestBook()
		library.lendBook(requestedBook)
		
	elif userChoise == 3:
		returnedBook = customer.returnBook()
		library.addBook(returnedBook)
		
	elif userChoise == 4:
		quit()
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	










