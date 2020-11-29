def test1(img):
  w = getWidth(img)
  h = getHeight(img)
  for x in range(0,w):
    for y in range(0,h):
      topPixel = getPixel(img,x,y)
      rightPixel = getPixel(img, y, x)
      color = getColor(topPixel)
      setColor (rightPixel, color)
    
def test2(img):
  w = getWidth(img)
  h = getHeight(img)
  for x in range(0,w):
    for y in range(0,h):
      topPixel = getPixel(img,x,y)
      rightPixel = getPixel(img,w-y-1, h-1-x)
      color = getColor(topPixel)
      setColor (rightPixel, color)

