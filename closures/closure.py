# L local(access variable, fast) E enclosing(access variable, slow)
# G global(access variable, slower) B built-in scope of python(access variable, slowest)
# IN PYTHON LIKE EVERYTHING ELSE FUNCTIONS ARE ALSO OBJECTS AND HENCE CAN BE RETURNED WITHOUT CALLING THEM
# CLOSURES CAN BE USED TO PROVIDE OBJECT ORIENTED SOLUTIONS WITHOUT CLASS AND USED IN DECORATORS

def print_message(message):
# This is an outer enclosing function
	def print_message_inner():
	# This is a nested function
		print(message)

	return print_message_inner # here outer nested function is returning a function not a value


another = print_message("Vamos") # here 'another' would have received a function object of 'print_message_inner'
another()

def convert_content_to_html(content):
	def enclosing_html_tag(tag):
		return "<{}>{}</{}>".format(tag, content, tag)

	return enclosing_html_tag

enclose = convert_content_to_html("Vamos")
another_enclose = convert_content_to_html(enclose("p"))
print(another_enclose("div"))

def nth_power(exp):
	def exponent_of(base):
		return base ** exp

	return exponent_of

square = nth_power(2)
print(square(10))

cube = nth_power(3)
print(cube(20))

def number():
	x = 100
	def add():
		print(x + 200) # here 'x' is in the scope of enclosing function 'number'

	add() # here 'add' function is in the local scope of function 'number'

number()