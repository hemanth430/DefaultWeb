class Operatingsystem:
	multitaksing = True 
	name = "Mac OS"

class Apple:
	website = "www.apple.com"
	name = "Apple"
	
class Macbook(Apple,Operatingsystem):
	def __init__(self):
		if self.multitaksing == True:
			print ("This is a multitaksing system, visit {} for more details".format(self.website))
			print("Name:", self.name)
macbook = Macbook()
