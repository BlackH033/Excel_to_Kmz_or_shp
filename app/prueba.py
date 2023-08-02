import tkintermapview as tkmp
from tkinter import *

rt=Tk()
rt.title("mapa")

lb=LabelFrame(rt)
lb.pack(pady=20)

map=tkmp.TkinterMapView(lb,width=800,height=600)
map.set_position(36.1699,-115.1396)
map.set_zoom(15)
map.pack()
rt.mainloop()


