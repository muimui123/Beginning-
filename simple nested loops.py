def test1(img):
  w = getWidth(img)
  h = getHeight(img)
  for y in range(0,h):
    for x in range(0,20):
      topPixel = getPixel(img,x,y)
      leftPixel = getPixel(img,40-x-1,y)
      color = getColor(topPixel)
      setColor(leftPixel, color)

def test2(img):
  w = getWidth(img)
  h = getHeight(img)/3
  for x in range(0,w):
    for y in range(0,3*h):
      topPixel = getPixel(img,x,y)
      if y < h:
        r = getRed(topPixel)
        r = r * 0.3
        setRed(topPixel, r)
      if 2*h < y <3*h:
        b = getBlue(topPixel)
        setBlue(topPixel,0)
        
def test3(img):
  w = getWidth(img)
  h = getHeight(img)/3
  for y in range(0,3*h):
    for x in range(0, w): 
      topPixel = getPixel(img, x, y)
      if y < h:
        color = getColor(topPixel)
        setColor(topPixel, makeLighter(color))
      if h < y < 2*h:
        b = getBlue(topPixel)
        b = b * 0.3
        setBlue(topPixel, b)
        g = getGreen(topPixel)
        g = g * 0.3
        setGreen(topPixel, g)
      if y > 2*h:
        r = getRed(topPixel)
        g = getGreen(topPixel)
        b = getBlue(topPixel)
        negColor = makeColor(255-r, 255-g, 255-b) 
        setColor(topPixel, negColor)