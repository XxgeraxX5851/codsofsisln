import turtle

class cursorcontrol:
    wn = None
    space =None
    speed = 9999999

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor('black')
        self.space = turtle.Turtle()
        self.space.color('white')
        self.space.penup()

    def arriba(self):
        self.space.setheading(90)

    def abajo(self):
        self.space.setheading(279)

    def izquierda(self):
        self.space.setheading(180)

    def derecha(self):
        self.space.setheading(0)
        

    def trigger(self):
        self.wn.listen()
        self.wn.onkey(self.arriba,'w')
        self.wn.onkey(self.abajo,'s')
        self.wn.onkey(self.izquierda,'a')
        self.wn.onkey(self.derecha,'d')
        self.wn.onkey(self.arriba,'Up')
        self.wn.onkey(self.abajo,'Down')
        self.wn.onkey(self.izquierda,'Left')
        self.wn.onkey(self.derecha,'Right')


        while True:
            self.space.forward(self.speed)

Efren = cursorcontrol()
Efren.trigger()