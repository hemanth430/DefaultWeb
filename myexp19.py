def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a + b 

def substract(a,b):
	print "SUBSTRACTING %d - %d" %(a,b)
	return a - b 
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" %(a,b)
	return a * b 

def divide(a,b):
	print "DIVIDING %d / %d" %(a,b) 
	return a / b 
	
print "Let's do some math with just functions:"

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d , Height: %d , Weight: %d , ID: %d" %(age, height, weight, iq)


#A puzzle for the extra credit, type it in anyway

print "Here is a puzzle."

what = add(age,substract(height,multiply(weight,divide(iq,2))))

print "That becomes: ", what , "Can you do it by hand?"


Let's do some math with just functions:
ADDING 30 + 5
SUBSTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35 , Height: 74 , Weight: 180 , ID: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBSTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391 Can you do it by hand?
































	