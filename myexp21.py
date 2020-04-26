#sentence = "All good things come to those who wait"

def break_words(stuff):
	"""This funciton will break up words for us."""
	words = stuff.split(' ')
	return words #This is used to split sentence into words , ouput = ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait']
	
def sort_words(words):
	"""Sorts the words""" 
	return sorted(words) #This is used to sort words , ['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word  #Used to print the first word after popping it off , All
	
def print_last_word(words):
	"""Prints the last word after popping it off""" 
	word = words.pop(-1)
	print word #Used to print the last word after popping it off , wait
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words) #Takes a full sentence and return the sorted words 

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence""" 
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words) #returns the first and last word of the sentece 
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one.""" 
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words) #prints the first and last word of the sorted sentence 
	
	