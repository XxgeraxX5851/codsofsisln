import turtle

class TurtleforNoob:
    def test(self):
        skk=turtle.Turtle()
        for i in range(4):
            skk.forward(903)
            skk.right(130)
        turtle.done()

    def estrella(self):
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(4):
            est.right(144)
            est.forward(100)

        turtle.done()

    def circulo(radio):
        t = turtle.Turtle()
        t.circle(100)
        t.done()

    def copoDeNieve(self):
        turtle.reset
        turtle.ht()
        for i in range(3):
            self.ks(200,3)
            turtle.left(120)
        turtle.update(53)
        turtle.done()
    def ks(self,legth,d):
        if d == 0:
            turtle.forward(legth/3)
        else:
            legth = legth/3
            d = d-1
            self.ks(legth,d)
            turtle.right(60)
            self.ks(legth,d)
            turtle.left(120)
            self.ks(legth,d)
            turtle.right(60)
            self.ks(legth,d)
                


Efren = TurtleforNoob()
Efren.copoDeNieve()