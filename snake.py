import turtle
import time
import random


delay = 0.1
body_segments = []
score = 0
high_score = 0

windows = turtle.Screen() 

#title
windows.title("juego snake")
#windows size
windows.setup(width=600, height=600)
#background color
windows.bgcolor("light green")
#head settings
#Turtle obj
head = turtle.Turtle()
#para que se quede fijo:
head.speed(0)
#shape:
head.shape("square")
#head color
head.color("green")

#para no dejar rastro de la animacion:
head.penup()
# center
head.goto(0, 0)
#para hacer que el programa espere a que yo le de otra dir.
head.direction = "stop"

# food config
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"


#Score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.whrite(f"Score 0       High Score:0", align="center", font=("Impact", 24))


def mov():
    if head.direction == "up":
        #almacenar el valor actual de la coor Y:
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        #almacenar el valor actual de la coor Y:
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        #almacenar el valor actual de la coor Y:
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == "left":
        #almacenar el valor actual de la coor Y:
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"


#Conectar teclado:
windows.lisetn()
windows.onkeyprees(dirUp, "Up")
windows.onkeyprees(dirDown, "Down")
windows.onkeyprees(dirRight, "Right")
windows.onkeyprees(dirLeft, "Left")
    
    
while True:
    windows.update()

    #colisiones con la ventana:
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Esconder segmentos:
        for segment in body_segments:
            segment.goto(1000, 1000)

        #clean segments after the game reiniciate
        body_segments.clear()
        score= 0
        text.clear()
        text.whrite(f"Score {score}       High Score: {high_score}", align="center", font=("Impact", 24))


        


    #colisiones head vs food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        # new segment config
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        body_segments.append(new_segment)

        score+= 10 
        if score > high_score:
            high_score = score

            text.clear()
            text.whrite(f"Score {score}       High Score: {high_score}", align="center", font=("Impact", 24))

    totalseg  = len(body_segments)
    
    for i in range(totalseg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalseg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    mov()

    #Coliciones con el propio cuerpo
    for segment in body_segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Esconder segmentos:
            for segment in body_segments:
                segment.goto(1000, 1000)

            body_segments.clear()

            score= 0
            text.clear()
            text.whrite(f"Score {score}       High Score: {high_score}", align="center", font=("Impact", 24))


        


        
        











    
    time.sleep(delay)




turtle.done()