while True:
	name = raw_input("Hi, please tell me your name: ")
	print "Nice to meet you, " + name
	ageString = raw_input(" How many credit hours have you taken? ")
	age = int(ageString)
	if 0<= age <= 29:
		print "Freshman"
	elif 30 <= age <= 59:
		print "Sophomore"
	elif 60 <= age <= 89:
		print "Junior"
	elif age >= 90:
		print "Senior"
	elif age < 0:
		break 
