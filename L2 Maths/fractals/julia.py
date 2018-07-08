import tkinter as tk
from math import sqrt, floor, log
from random import choice

def julia(x, y, a, b, maxiterations, iterations, canvas):
  if(iterations == 0):
    return

  if(20*x+350>600) or (20*y+350 > 600) or (20*x+350 < 0) or (20*y+350 < 0):
    return

  colour = '#' + (hex(floor((255**3)*sqrt(iterations/maxiterations))).replace('0x', '').rjust(6,'0'))
  canvas.create_oval(20*x+350,20*y+350,20*x+351,20*y+351,fill=colour,outline=colour)

  #montecarlo = choice(["+-","+","-"])

  #if(montecarlo.find("+") != -1):
  x1 = 0.5*(x - a) + 0.5*sqrt((x - a)**2 + (y - b)**2)
  if(x1 != 0):
    y1 = (y - b)/(2*x1)
    julia(x1, y1, a, b, maxiterations, iterations-1, canvas)

  #if(montecarlo.find("-") != -1):
  x2 = 0.5*(x - a) - 0.5*sqrt((x - a)**2 + (y - b)**2)
  if(x2 != 0):
    y2 = (y - b)/(2*x2)
    julia(x2, y2, a, b, maxiterations, iterations-1, canvas)

w = tk.Canvas(width=700,height=700)
julia(1.2981, 0.6252, -3/4, 0, 26, 26, w)
w.grid()
w.mainloop()
