
def purpleTeeth(img):
  teeth = makeColor(233,215,179)
  for pixy in getPixels(img):
    x = getX(pixy)
    y = getY(pixy)
    if 226 < x < 269  and 187 < y < 207:
      color = getColor(pixy)
      diff = distance(teeth, color)
      if diff < 50:
        setColor(pixy, makeColor(128,0,128))

def orangeHair(img):
  hair = makeColor(10,11,2)
  for pixy in getPixels(img):
    x = getX(pixy)
    y = getY(pixy)
    if 129 < x < 361 and 19 < y <227:
      color = getColor(pixy)
      diff = distance(hair, color)
      if diff < 100:
        setColor(pixy, orange)
    
def redEye(img):
  eye = makeColor(114,122,99)
  for pixy in getPixels(img):
    x = getX(pixy)
    y = getY(pixy)
    if 212 < x < 295 and 122 < y <142:
      color = getColor(pixy)
      diff = distance(eye, color)
      if diff < 60:
        setColor(pixy, red)

def redEye2(img):
  eye = makeColor(68,32,27)
  for pixy in getPixels(img):
    x = getX(pixy)
    y = getY(pixy)
    if 212 < x < 295 and 122 < y <142:
      color = getColor(pixy)
      diff = distance(eye, color)
      if diff < 60:
        setColor(pixy, red)      
          
def test1(img):
  purpleTeeth(img)
  orangeHair(img)
  redEye(img) 
  redEye2(img)
  
  
def lineDrawing(photo):
  for pixy1 in getPixels(photo):
    x = getX(pixy1)
    y = getY(pixy1)
    if x < getWidth(photo)-1 and y < getHeight(photo)-1:
      pixy2 = getPixel(photo, x+1, y+1)
      bright1 = brightness(pixy1)
      bright2 = brightness(pixy2)
      diff = abs(bright1 - bright2)
      if diff < 10:
        setColor(pixy1, white)
      if diff >= 10:
        setColor(pixy1, black)
        
def chromakey(fg, bg):
  for p in getPixels(fg):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if r < g  and b < g:
      x = getX(p)
      y = getY(p)
      bgPix = getPixel(bg, x, y)
      color = getColor(bgPix)
      setColor(p, color)