pyramidsize = 30

for i in range(30):
	foo = ''
	for j in range(i):
		foo = foo + '.'
	print(foo)

for i in range(30):
	foo = ''
	for j in range(pyramidsize-i):
		foo = foo + '.'
	print(foo)
