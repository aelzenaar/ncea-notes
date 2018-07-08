import tkinter as tk
from math import sqrt

def sierp(x, y, length, iterations, canvas):
  if(iterations == 0):
    return

  xleft = x - length/2
  xright = x + length/2
  yleft = yright = y + length*sqrt(3)/2

  canvas.create_polygon(x, y, xleft, yleft, xright, yright, fill = 'black')
  canvas.create_polygon((x+xleft)/2, (y+yleft)/2,
                        x, yleft, (x+xright)/2, (y+yright)/2, fill = 'white')

  sierp((x+xleft)/2, (y+yleft)/2, length/2, iterations - 1, canvas)
  sierp((x+xright)/2, (y+yright)/2, length/2, iterations - 1, canvas)
  sierp(x,y, length/2, iterations - 1, canvas)

w = tk.Canvas(width=600,height=600)
sierp(300, 20, 550, 5, w)
w.grid()
w.mainloop()
