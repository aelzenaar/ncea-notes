import tkinter as tk

values = []

w = tk.Canvas(width=1000,height=200,bg="white")

def onclick(event):
  w.create_rectangle(0, 0, 1000, 200, fill="white")

  values.append(event.x)
  values.sort()

  acc = 0
  for v in values:
    w.create_line(v, 0, v, 200)
    acc += v

  mean = acc/(len(values))
  if len(values)%2 == 1:
    median = values[int(len(values)/2)]
  else:
    median = (values[int(len(values)/2)] + values[int((len(values))/2) - 1])/2

  print(values)
  print("mean: " + str(mean) + " median: " + str(median))

  w.create_line(mean, 0, mean, 200, fill="red")
  w.create_line(median, 0, median, 200, fill="blue")

w.bind("<Button-1>", func=onclick)
w.grid()
w.mainloop()
