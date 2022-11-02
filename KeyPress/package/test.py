from tkinter import Tk, Canvas
from PIL import Image, ImageTk
import requests

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
		
	points = [x1+radius, y1,
			  x1+radius, y1,
			  x2-radius, y1,
			  x2-radius, y1,
			  x2, y1,
			  x2, y1+radius,
			  x2, y1+radius,
			  x2, y2-radius,
			  x2, y2-radius,
			  x2, y2,
			  x2-radius, y2,
			  x2-radius, y2,
			  x1+radius, y2,
			  x1+radius, y2,
			  x1, y2,
			  x1, y2-radius,
			  x1, y2-radius,
			  x1, y1+radius,
			  x1, y1+radius,
			  x1, y1]

	return canvas.create_polygon(points, **kwargs, smooth=True)

width, height = 600, 600
x, y = 0, 0

root = Tk()
root.config(bg = 'grey15')
root.geometry(f'+{root.winfo_screenwidth() - 600}+{root.winfo_screenheight() - 250}')
root.attributes('-transparentcolor', 'grey15')
root.attributes('-topmost', True)
root.overrideredirect(True)

canvas = Canvas(
	root, bg ='grey15', width = width, height = height, highlightthickness = 0
)
canvas.pack()
#canvas.create_rectangle(x, y, x+width, y+height, fill='red')
round_rectangle(0, 0, 550, 200, radius = 20, fill = 'white')

root.mainloop()