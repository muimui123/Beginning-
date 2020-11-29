def makeSunset(img):
  pixies = getPixels(img)
  index = 0
  while index < len(pixies):
    p = pixies[index]
    value = getBlue(p)
    setBlue(p, value*0.7)
    value = getGreen(p)
    setGreen(p, value*0.7)
    index += 1  
    
def test(img):
  for p in getPixels(img):
    value = getBlue(p)
    setBlue(p, value*0.7)
    value = getGreen(p)
    setGreen(p, value*0.7)

  
def rotateHorseSideways():
  src = makePicture("C:/Users/student/cis101_media/1boys.png")
  canvas = makeEmptyPicture(1000,1000)
  width = getWidth(src)
  height = getHeight(src)
  targetX=0
  while targetX < width:
    targetY=0
    while targetY < height:
      ab = getColor(getPixel(src,targetX,targetY))
      setColor(getPixel(canvas, targetY, width - targetX -1), ab)
      targetY += 1
    targetX += 1
  show(canvas)
  return canvas
  
  
def test2():
  src = makePicture("C:/Users/student/cis101_media/1boys.png")
  canvas = makeEmptyPicture(1000,1000)
  targetX=0
  width = getWidth(src)
  for sourceX in range(0, getWidth(src)):
    targetY = 0
    for sourceY in range(0, getHeight(src)):
      color = getColor(getPixel(src, sourceX, sourceY))
      setColor(getPixel(canvas, targetY, width - targetX - 1), color)
      targetY += 1
    targetX += 1
  show(canvas)
  return canvas