class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property # property getter with @property decorator
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter # property setter <name of property with @property decorator already set above>.setter
	def fullname(self, name):
		names = name.split(' ')
		self.first = names[0]
		self.last = names[1]
		# or
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter # property deleter <name of property with @property decorator already set above>.deleter
	def fullname(self):
		self.first = None
		self.last = None
		print("Deleted name")


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Roger Federer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)