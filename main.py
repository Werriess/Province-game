import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Province quiz!")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
# image = "C:/Users/werne/OneDrive/Desktop/Projects/Python/South Africa Game/images/blank-map-of-south-africa.gif"
# screen.bgpic(image)

data = pd.read_csv("C:/Users/werne/OneDrive/Desktop/Projects/Python/South Africa Game/Province Coordinates Python Game New.csv",  sep=";")

mp = pd.read_csv("C:/Users/werne/Downloads/Mpumalanga.csv", sep=";")

dt = pd.read_csv("C:/Users/werne/Downloads/KZN Newer.csv", sep=";")

ted = turtle.Turtle() 
ted.penup()

def set_land(x, y):
    ted.goto(x, y)
    ted.pendown()
    ted.hideturtle()


def set_word(x, y, word):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(word, align="center", font=("Arial", 10, "normal"))
    turtle.hideturtle() 

def toets(kyk):
    for index, row_t in kyk.iterrows():
                set_land(row_t["x"], row_t["y"])

while True:
    user_answer = screen.textinput(title="Guess the province", prompt="Enter the name of a province:")
    if user_answer.lower() == "quit" or user_answer.lower() == "exit":
        break
    for index, row in data.iterrows():
        if user_answer.lower() == row["Province"].lower():
                if row["Province"] == "Gauteng":
                    toets(dt)
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                else:
                    toets(mp)
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
            
turtle.exitonclick()

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)



                