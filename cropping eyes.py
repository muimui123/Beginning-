def crop(img, left, top, right, bottom):
  canvas = makeEmptyPicture(500,700)
  y2 = 100
  for y1 in range(top, bottom):
    x2 = 100
    for x1 in range(left, right):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      color = getColor(src)
      setColor(dest, color)
      x2 = x2 + 1
    y2 = y2 + 1
  return canvas

  
def crop2(img, left, top, right, bottom):
  canvas = makeEmptyPicture(500,700)
  y2 = 50
  y3 = 100
  for y1 in range(top, bottom):
    x2 = 50
    x3 = 50
    for x1 in range(left, right):
      src = getPixel(img, x1, y1)
      dest = getPixel(canvas, x2, y2)
      dest2 = getPixel(canvas, x3, y3)
      color = getColor(src)
      setColor(dest, color)
      setColor(dest2, color)
      x2 = x2 + 1
      x3 = x3 + 1
    y2 = y2 + 1
    y3 = y3 + 1
  return canvas    
        
def test2():
  emma = makePicture("emma.jpg")
  print emma
  canvas = makeEmptyPicture(500,700)
  print canvas
  targetX = 0
  for sourceX in range(0, getWidth(emma)):
    targetY = getHeight(canvas)-getHeight(emma)-5
    for sourceY in range(0, getheight(emma)):
      px = getPixel(emma, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      color = getColor(px)
      setColor(dest, color)
      targetY = targetY+1
    targetX = targetX+1
  targetX = 100  
  for sourceX in range(0, getWidth(emma)):
    targetY = getHeight(canvas)-getHeight(emma)-5
    for sourceY in range(0, getheight(emma)):
       px = getPixel(emma, sourceX, sourceY)
       cx = getPixel(canvas, targetX, targetY)
       color = getColor(px)
       setColor(dest, color)
       targetY = targetY+1
    targetX = targetX+1
    show(canvas)
    return canvas
      
  
    

  
  

