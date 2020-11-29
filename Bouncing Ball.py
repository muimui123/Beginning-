def makeCircle(x,y):
  canvas = makeEmptyPicture(600, 600)
  addOvalFilled(canvas, x, y, 50, 50, red)
  return canvas
  
def fallingCircle():
  x = 0
  y = 0
  xspeed = 10
  yspeed = 20
  i = 1
  while i < 210:
    anton = makeCircle(x,y)
    if i<10:
      writePictureTo(anton, "C:/Users/Student/Desktop/hw/images00" + str(i) + ".jpg")
    elif i<100:
      writePictureTo(anton, "C:/Users/Student/Desktop/hw/images0" + str(i) + ".jpg")
    else:
      writePictureTo(anton, "C:/Users/Student/Desktop/hw/images" + str(i) + ".jpg")
    x += xspeed
    y += yspeed
    i += 1
    if x > getWidth(anton):
      xspeed = -10
    if x < 0:
      xspeed = 10
    if y > getHeight(anton):
      yspeed = -20 
    if y < 0:
      yspeed = 20 
  movie = makeMovieFromInitialFile( "C:/Users/Student/Desktop/hw/images001.jpg")
  return movie
       

    
