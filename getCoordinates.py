import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Province quiz!")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
image = "C:/Users/werne/OneDrive/Desktop/Projects/Python/South Africa Game/images/blank-map-of-south-africa.gif"
screen.bgpic(image)

def get_mouse_click_coor(x, y):
     print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()