def face(x, y):
  canvas = makeEmptyPicture(700,700)
  addOvalFilled(canvas, x, y, 100, 100, black)
  addOvalFilled(canvas, 30+x, 42+y, 10, 15, red)
  addOvalFilled(canvas, 70+x, 42+y, 10, 15, red)
  addOvalFilled(canvas, 46+x, 69+y, 25, 25, white)
  return canvas 

def face2(canvas, x, y):
  addOvalFilled(canvas, x, y, 100, 100, black)
  addOvalFilled(canvas, 30+x, 42+y, 10, 15, red)
  addOvalFilled(canvas, 70+x, 42+y, 10, 15, red)
  addOvalFilled(canvas, 46+x, 69+y, 25, 25, white)


def manyfaces():
  canvas = makeEmptyPicture(700,700)
  w = getWidth(canvas)
  h = getHeight(canvas)
  y = 0
  for y in range(0, h,100):
    x = 0
    for x in range(0, w,100): 
      face2(canvas, x, y)    
  return canvas
