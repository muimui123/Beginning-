def test1(string):
  s = " "
  word = string.split(" ")
  for i in range(0,len(word),2):
    s += word[i]+" "
    s += word[i+1].upper()+" "   
  print s
     

def test2(string):
  for char in string:
    print ord(char)

def test3(string):
  m = 0.0
  f = 0.0
  for char in string:
    if char == "M":
      m += 1
    else:
      f += 1
  m = (m)/(len(string))
  f = (f)/(len(string))
  print "There are ", m, " males, ", f, " females"