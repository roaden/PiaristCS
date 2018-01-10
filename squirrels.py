print("Hey, how many times should I say squirrel?")

try:
	squirrelnum = int(input())
except:
	print("Hey, listen.  You didn't give me a number I like so, I quit.")
	quit()
for i in range(squirrelnum):
	if i%2 == 0:
		print("Squirrel!")
	else:
		print("        Squirrel!")
