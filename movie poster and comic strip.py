def copy(img, canvas, dx, dy): 
  w = getWidth(img) 
  h = getHeight(img) 
  y2 = dy 
  for y1 in range(0,h): 
    x2 = dx 
    for x1 in range(0,w): 
      src = getPixel(img, x1, y1) 
      dest = getPixel(canvas, x2, y2)
      color = getColor(src) 
      setColor(dest, color) 
      x2 = x2 + 1 
    y2 = y2 + 1 
    
  
def makeComic(): 
  bg = makeEmptyPicture(700,700) 
  copy(iman, bg, 200, 200) 
  addText(bg, 350, 350, "\"OMG! I broke the bright.\"", red)  
  return bg 
  
      
def makeComic2(): 
  bg = makeEmptyPicture(1200,1200) 
  copy(dm1, bg, 50, 70) 
  copy(dm2, bg, 400, 70) 
  copy(dm3, bg, 800, 70) 
  myFont = makeStyle(sansSerif, bold+italic, 13)
  addTextWithStyle(bg, 20, 50,"\"Why her nose is taller than me? I am not your brother!!\"", myFont, red) 
  addText(bg, 380, 50, "\"Should I drink this to increase my height of the nose? Yes? No?\"", orange)
  addText(bg, 810, 50, "\"No? She is an exception. I can do plastic surgery. ^^\"", pink)  
  return bg 