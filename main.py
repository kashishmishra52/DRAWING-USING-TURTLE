from turtle import Turtle,Screen

tim = Turtle()
screen=Screen()
screen.listen()
tim.speed(30)
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_clockwise():
    tim.right(10)

def move_counter():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"W")
screen.onkey(move_backward,"S")
screen.onkey(move_clockwise,"D")
screen.onkey(move_counter,"A")
screen.onkey(clear_screen,"C")
screen.exitonclick()
