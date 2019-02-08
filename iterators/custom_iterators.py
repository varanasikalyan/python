class CRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		else:
			current = self.value
			self.index += 1
			self.value += 1
			return current


# Writing a custom iterator using a yield, def way
def yield_reverse(start, end):
	while start >= end:
		# yield maintains the previous state of the variable, in this case, each time yield_reverse is called, it suspends 
		# the execution of yield_reverse and returns "start" at statement "yield start" value and when yield_reverse is called again,
		# the execution continues right after the "yield start" statement which is "start -= 1",
		# with "start" value at its previous state maintained
		# but to create an iterator using yield next() on the created iterator must be used to continue execution
		# eg. ite = yield_reverse(10, 1)
		# next(ite) -- 10
		# next(ite) -- 9
		# next(ite) -- 8
		# next(ite) -- 7
		print("Before {0}".format(start))
		yield start
		print("After {0}".format(start))
		start -= 1

def c_range(start, end):
	while start < end:
		yield start
		start += 1

def c_range_endless(start):
	while True:
		yield start
		start += 1

nums = CRange(1, 10)

g_nums = c_range(1, 10)

g_nums_exp = yield_reverse(10, 1)

print(g_nums_exp.__next__())
print("vamos")
print(g_nums_exp.__next__())

# print(next(g_nums_exp))
# print("vamos")
# print(next(g_nums_exp))

# Output
# Before 10
# 10
# vamos
# After 10
# Before 9
# 9

# g_e_nums = c_range_endless(1)

# for num in g_nums:
# 	print(num)

# print(next(g_e_nums))
# print(next(g_e_nums))
# print(next(g_e_nums))
# print(next(g_e_nums))
# print(next(g_e_nums))

# while True:
# 	try:
# 		print(next(nums))
# 	except StopIteration:
# 		break
