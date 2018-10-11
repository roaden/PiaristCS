#A brief explanation of loops.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiouy'

backward = ''
for i in range(len(alphabet)):
	#Assign the values to backward that are alphabet reversed.
	backward += alphabet[-i-1]
	#Print if a vowel is encountered.
	for j in range(len(vowels)):
		if vowels[j] == alphabet[i]:
			print(alphabet[i])
print(backward)
