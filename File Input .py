import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
llines = 0
char = 0
vowel = 0
consonant = 0
lower = 0
upper = 0
for line in file:
	llines += 1
	for words in line:
		for chars in words:
			char +=1
			if chars.lower() in "aeiou":
				vowel +=1
			if chars.lower() in "bcdfghjklmnpqrstvwxyz":
				consonant +=1
			if chars in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				upper +=1
			if chars in "abcdefghijklmnopqrstuvwxyz":
				lower +=1
print "The number of lines:",llines, 
print "The number of characters:" ,char, 
print "The number of vowels: " ,vowel,
print "The number of consonants: " ,consonant,
print "The number of lowercase letters: " ,lower,
print "The number of uppercase letters: " ,upper,
	
