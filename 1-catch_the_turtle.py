import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle Game")

FONT = ("Arial",20,"normal")
turtle_list = []
score = 0
game_over = False

#1- öncelikle score yazısı için  turtle ayarlama yapalım
turtle.tracer(0) # turtle ları izleme kapalı(animasyonlu geçiş)
score_turtle = turtle.Turtle()

#countdown için bir turtle
countdown_turtle = turtle.Turtle()

def set_score_turtle():
    score_turtle.color("blue")
    score_turtle.hideturtle()# score_turtle turtlenın kamplumbağasını gizleme
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setpos(0,y) # position ayarlama komutları goto,setpos,setposition
    score_turtle.write(arg="Score:0",move=False,align="center",font=FONT)

set_score_turtle()


#2.adım kamplumbağa turtle ları oluşturma
GridSize = 10
def make_turtle(x,y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * GridSize,y * GridSize)
    turtle_list.append(t)

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)
        print(x,y)#x,y kordinatlarını yazdırma işlemi

    t.onclick(handle_click)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]

def set_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)
    hide_turtle()

def hide_turtle():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over :
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    countdown_turtle.hideturtle()  # score_turtle turtlenın kamplumbağasını gizleme
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setpos(0, y -30 )  # position ayarlama komutları goto,setpos,setposition
    countdown_turtle.clear()
    global game_over
    if time > 0 :
        countdown_turtle.write(arg=f"Time:{time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda :countdown(time - 1),1000)
    else :
        game_over = True
        hide_turtle()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)


set_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1) # turtle ları izleme açık(animasyonlu geçiş)
turtle.mainloop()