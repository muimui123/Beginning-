import sys
c = sys.argv[1] 
n = int(sys.argv[2])
space = " "
print n*c
for i in range(n-2):
	print c + space *(n-2) + c
print n*c