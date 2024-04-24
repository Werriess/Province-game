import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=601, height=751)

data = pd.read_csv("C:/Users/werne/OneDrive/Desktop/Projects/Python/South Africa Game/Province-game/Province Coordinates Python Game New.csv",  sep=";")

mp = pd.read_csv("C:/Users/werne/Downloads/Mpumalanga.csv", sep=";")
sa = pd.read_csv("C:/Users/werne/Downloads/South Africa Map Coordinates.csv", sep=";")
dt = pd.read_csv("C:/Users/werne/Downloads/KZN Newer.csv", sep=";")

ted = turtle.Turtle() 
ted.speed(10)
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

def draw_map(data):
    for index, row_t in data.iterrows():
                set_land(row_t["x"], row_t["y"])
                
begin = screen.textinput(title="SA Province guessing game!", prompt="Type begin to start")
draw_map(sa)
ted.clear()


image = "C:/Users/werne/OneDrive/Desktop/Projects/Python/South Africa Game/Province-game/images/blank-map-of-south-africa.gif"
screen.bgpic(image)

count = 0

while count < 9:
    user_answer = screen.textinput(title="Guess the province", prompt="Enter the name of a province:")
    if user_answer.lower() == "quit" or user_answer.lower() == "exit":
        break
    for index, row in data.iterrows():
        if user_answer.lower() == row["Province"].lower():
                if row["Province"] == "Gauteng":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Mpumalanga":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "KwaZulu-Natal":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "North West":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Northern Cape":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Eastern Cape":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Free State":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Limpopo":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                elif row["Province"] == "Western Cape":
                    set_word(row["x"], row["y"], row["Province"])
                    ted.penup()
                    count+=1
                else:
                    print("Wrong")

turtle.exitonclick()





                