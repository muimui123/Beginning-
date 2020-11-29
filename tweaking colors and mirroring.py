def test1 (picture):
  for p in getPixels(picture):
    red= getRed(p)/2
    green= getGreen(p)/2
    blue= getBlue(p)*2
    color = makeColor(red, green, blue)
    setColor(p,color)

def grayScale(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p, makeColor(intensity,intensity,intensity))
def negative (picture):
  for px in getPixels(picture):
    red= getRed(px)
    green= getGreen(px) 
    blue= getBlue(px)
    color=makeColor(255-red, 255-green, 255-blue)
    setColor(px,color)
    
def test2(picture):
  grayScale(picture)
  negative(picture) 
  
def blackHalf(img):
  pixels = getPixels(img)
  n = len(pixels)
  nums = range (0, n/2)
  for i in nums:
     pixy = pixels[i]
     setColor(pixy, black)
    
   
def mirrorHalf2(img):
  pixels = getPixels(img)
  n = len(pixels)
  for i in range(n/2,n):
    target = n-1-i
    src = pixels[i]
    dest = pixels[target]
    color = getColor(src)
    setColor(dest, color)
    
    
def test1 (picture):
  for p in getPixels(picture):
    red= getRed(p)/2
    green= getGreen(p)/2
    blue= getBlue(p)*2
    color = makeColor(red, green, blue)
    setColor(p,color)