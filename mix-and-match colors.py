def decreaseBlue(picture): 
  for pix in getPixels(picture):
    value = getBlue(pix)
    setBlue(pix, value*0.5)
    
def decreaseGreen(picture): 
 for pix in getPixels(picture):
   value = getGreen(pix)
   setGreen(pix, value*0.5)   
   
   
def swapColor (picture):
  for p in getPixels(picture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    color = makeColor(blue, red, green)
    setColor(p, color) 
    
    
def test1 (picture):
  for p in getPixels(picture):
    setRed(p,0)
    setGreen(p,0)
    setBlue(p,0)
    
def test2 (picture):
  for p in getPixels(picture):
    setRed(p,255)
    setGreen(p,255)
    setBlue(p,255)