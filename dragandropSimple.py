# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 07:45:27 2016

@author: Anurag
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Drag and Drop')

drag_data = {'x':0, 'y':1, 'item': None}

def on_click(event):
    print(event.x, event.y)
def on_release(event):
    print(event.x, event.y)    

def onPress(event):
    w = event.widget
    index = w.get_children()
    print(index) # <--- prints the children of Tree.
    #drag_data["item"] = t
    drag_data["x"] = event.x
    drag_data["y"] = event.y

def onMotion(event):
    delta_x = event.x - drag_data["x"]
    delta_y = event.y - drag_data["y"]
    # move the object the appropriate amount
    index = event.widget.get_children()
    pic = tk.PhotoImage(file = 'C:\\Users\\Anurag\\Downloads\\csv-64.gif')
    can.create_image(event.x+100, event.y+50, image=pic, tags='sweden')
    can.move(index, delta_x, delta_y)
    # record the new position
    drag_data["x"] = event.x
    drag_data["y"] = event.y

def onRelease(event):
    wx, wy = can.winfo_rootx(), can.winfo_rooty()
    x,y = ops_tree.winfo_pointerxy()
    cx = can.canvasx(x-wx)
    cy = can.canvasy(y-wy)
    drag_data["item"] = None
    drag_data["x"] = 0
    drag_data["y"] = 0

#---Frame to hold both treeview and canvas ....
l_frame = tk.Frame(root)
#---------TreeView to hold the directories--------------------------------
ops_tree = ttk.Treeview(l_frame)
ops_tree.insert("", 1, "ReadCSV", text="Read")
ops_tree.insert('', 1, 'WriteCSV', text='Write')
ops_tree.insert("ReadCSV", 2, text="sub-M1")
ops_tree.insert('WriteCSV', 1, text = 'sub-F1')
ops_tree.grid(row = 0, column =1)
ops_tree.bind("<ButtonPress-1>", onPress)
ops_tree.bind("<ButtonRelease-1>", onRelease)
ops_tree.bind("<B1-Motion>", onMotion)
#----------------------------------------
can = tk.Canvas(l_frame, width = 800, height = 225, bg = 'aqua')
can.grid(row = 0, column = 20)
can.bind("<ButtonRelease-1>", on_release)

l_frame.grid()
root.mainloop()







