def test1 (picture):
  for p in getPixels(picture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    if(red < 100):
      setRed(p,0)
    if(red > 100):
      setRed(p,255)
    if(green < 100):
      setGreen(p,0)
    if(green > 100):
      setGreen(p,255)
    if(blue < 100):
      setBlue(p,0)
    if(blue > 100):
      setBlue(p,255)


def test2 (pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if(r > 100 and g > 100 and b > 100):
      setColor(p, pink)

