import tkinter as tk
from math import sqrt

def hcurve(x, y, length, scale, horizontal, iterations, canvas):
  if(iterations == 0):
    return

  if horizontal == True:
    x0 = x - length/2
    x1 = x + length/2
    y0 = y1 = y
  else:
    y0 = y - length/2
    y1 = y + length/2
    x0 = x1 = x

  canvas.create_line(x0, y0, x1, y1)

  hcurve(x0, y0, length*scale, scale, not(horizontal), iterations - 1, canvas)
  hcurve(x1, y1, length*scale, scale, not(horizontal), iterations - 1, canvas)

w = tk.Canvas(width=500,height=500)
hcurve(250, 250, 220, 1/sqrt(2), True, 12, w)
w.grid()
w.mainloop()
