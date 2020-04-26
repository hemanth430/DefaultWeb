class Apple:
	manufacturer = "Apple Inc."
	contactwebsite = "www.apple.com/contact"
	
	def contactDetails(self):
		print("To contact us, log on to ",self.contactwebsite)
		
class MacBook(Apple):
	def __init__(self):
		self.yearofmanufacture = 2017 
	
	def manufacturedetails(self):
		print ("This macBook was manufactured in the year {} by {} and to contact us please visit".format(self.yearofmanufacture,self.manufacturer))
		
macbook = MacBook()

macbook.manufacturedetails()
macbook.contactDetails()

