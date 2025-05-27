import turtle

class TurtleforNoob:
    def estrella(self):
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(4):
            est.right(144)
            est.forward(100)

        turtle.done()

carritos = TurtleforNoob()
carritos.estrella()