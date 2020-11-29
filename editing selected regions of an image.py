def test1(img,color,number):
  left = number
  top = number
  right = getWidth(img)-number
  bottom = getHeight(img)-number
  for p in getPixels(img):
    x = getX(p)
    y = getY(p)
    if x< left or x > right or y > bottom or y < top:
      setColor(p, color)
   
      
def test2(img):
  halfway = getWidth(img) /2
  for px in getPixels(img):
    x = getX(px)
    if x < halfway:
      color = getColor(px)
      setColor(px, makeLighter(color))
    else:
      intensity = (getRed(px)+getGreen(px)+getBlue(px))/3
      setColor(px, makeColor(intensity, intensity, intensity))
      
def brightness(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  avg = (r+g+b)/3
  return avg
        
def test3(img):
  third = getWidth(img)/3
  for pixy in getPixels(img):
    x = getX(pixy)
    if x < third:
      bright = brightness(pixy)
      ggrey = makeColor(bright, bright, bright)
      setColor(pixy, ggrey)
    if third < x < 2*third:
      r = getBlue(pixy)
      r = r * 0.3
      setBlue(pixy, r)
      g = getGreen(pixy)
      g = g * 0.3
      setGreen(pixy, g)
    if x > 2*third:
      r = getRed(pixy)
      g = getGreen(pixy)
      b = getBlue(pixy)
      negColor = makeColor(255-r, 255-g, 255-b) 
      setColor(pixy, negColor)
      
      