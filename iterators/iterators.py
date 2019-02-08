print(dir(str))

string="Vamos Rafa"
i_string = string.__iter__()
i_string = iter(string)
print(dir(string))

for ch in string:
	print(ch)

print(dir(i_string))

print(next(i_string))
print(next(i_string))
print(next(i_string))
print(next(i_string))

while True:
	try:
		print("--" + next(i_string))
	except StopIteration:
		break