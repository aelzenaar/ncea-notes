import tkinter as tk
from math import sqrt, atan2, cos, sin

def koch(coords, where, iterations):
  x0 = coords[where][0]
  y0 = coords[where][1]
  x1 = coords[where + 1][0]
  y1 = coords[where + 1][1]
  length = sqrt((x1 - x0)**2 + (y1 - y0)**2)
  r = length*1/((sqrt(3)))
  theta = atan2(y1 - y0, x1 - x0)
  phi = atan2(1, sqrt(3))
  xnew1 = x0 + length/3 * cos(theta)
  ynew1 = y0 + length/3 * sin(theta)
  xnew2 = x0 + r * cos(theta + phi)
  ynew2 = y0 + r * sin(theta + phi)
  xnew3 = x0 + 2*length/3 * cos(theta)
  ynew3 = y0 + 2*length/3 * sin(theta)

  coords.insert(where + 1, [xnew1, ynew1])
  coords.insert(where + 2, [xnew2, ynew2])
  coords.insert(where + 3, [xnew3, ynew3])

  if(iterations > 1):
    coords = koch(coords, where, iterations - 1)
    coords = koch(coords, where + 4**(iterations-1), iterations - 1)
    coords = koch(coords, where + 2*4**(iterations-1), iterations - 1)
    coords = koch(coords, where + 3*4**(iterations-1), iterations - 1)
  return coords

w = tk.Canvas(width=600,height=600)
coords = koch([[30, 300],[600 - 30, 300]], 0, 6)
for i in range(0, len(coords) - 1):
  w.create_line(coords[i][0], coords[i][1], coords[i + 1][0], coords[i + 1][1])
w.grid()
w.mainloop()
