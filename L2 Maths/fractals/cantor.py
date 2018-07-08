import tkinter as tk
from math import sqrt

def comb(x, y, length, height, iterations, canvas):
  print(length)
  if(iterations == 0):
    return

  x0 = x - length/2
  x1 = x + length/2 + 1
  y0 = y - height/2
  y1 = y + height/2 + 1

  w.create_rectangle(x0, y0, x1, y1, fill='black')

  comb(x - length/3, y + height + 10, length/3, height, iterations - 1, canvas)
  comb(x + length/3, y + height + 10, length/3, height, iterations - 1, canvas)


w = tk.Canvas(width=1400,height=500)
comb(700, 20, 1300, 20, 6, w)
w.grid()
w.mainloop()
