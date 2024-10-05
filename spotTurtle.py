import turtle
import random
import colorsys

screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(600,600)
screen.title('Catch the Turtle')
turtle.hideturtle()

n = 200
chasers = []
for i in range(n):
    chasers.append(turtle.Turtle())

for i in range(n):
    h = random.random()
    c = colorsys.hsv_to_rgb(h,1,0.8)
    chasers[i].color(c)
    chasers[i].up()
    chasers[i].goto(random.uniform(-400,400), random.uniform(-400, 400))
chasers[n-1].goto(0,-200)
chasers[n-1].shape('turtle')
chasers[n-1].color('green')
screen.update()

for i in range(n):
    chasers[i].up()
    chasers[i].goto(random.uniform(-400,400), random.uniform(-400,400))
chasers[n-1].goto(0,-200)
chasers[n-1].shape('turtle')
screen.update()

def moveTurtle():
    chasers[n-1].left(3)
    chasers[n-1].fd(10)
    for i in range(n-1):
        angle = chasers[i].towards(chasers[i+1])
        chasers[i].seth(angle)
        chasers[i].fd(10)
    screen.update()
    screen.ontimer(moveTurtle,0)

moveTurtle()
turtle.done
