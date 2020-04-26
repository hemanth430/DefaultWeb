#Inheritance 
#We will learn about single level inheritance 
class Apple:
	manufacturer = "Apple Inc."
	contactwebsite = "www.apple.com/contact"
	
	def contactDetails(self):
		print("To contact us, log on to",self.contactwebsite)
		
		
class MacBook(Apple):
	def __init__(self):
		self.yearOfManufacuture = 2017 
		
	def manufacturerDetails(self):
		print("This MacBook was manufactured in the year {} by {}".format(self.yearOfManufacuture, self.manufacturer))
		
macBook = MacBook()
macBook.manufacturerDetails()
macBook.contactDetails()
