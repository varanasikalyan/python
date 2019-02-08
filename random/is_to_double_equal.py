# 'is' makes address comparison to see if the objects are same
# '==' makes similarity comparison to see if the objects are similar and are of same type but not exactly same, 
# like twins(look exactly same but different entities)

a = [1, 2, 3]
b = a

print(a)
print(b)
print(a == b) #True
print(a is b) #True

c = list(a)
print(a)
print(c)
print(a == c) #True
print(a is c) #False
# or
print(id(a) == id(c)) #False