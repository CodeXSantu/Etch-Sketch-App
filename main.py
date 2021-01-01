from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.title("ETCH-SKETCH")
pen_color = screen.textinput("Color", "Enter the pen color:")
tim.pencolor(pen_color)

screen.listen()


def draw_forward():
    tim.forward(10)
def draw_backward():
    tim.forward(-10)
def draw_left():
    tim.left(10)
def draw_right():
    tim.right(10)
def draw_clear():
    tim.clear()
    tim.penup()
    tim.goto(x=0,y=0)
    tim.setheading(0)
    tim.pendown()


screen.onkeypress(fun=draw_forward,key="d")
screen.onkeypress(fun=draw_backward,key="a")
screen.onkeypress(fun=draw_left,key="w")
screen.onkeypress(fun=draw_right,key="s")
screen.onkeypress(fun=draw_clear,key="c")


screen.exitonclick()