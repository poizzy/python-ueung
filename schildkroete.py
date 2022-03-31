import turtle

def quadrat(t, seiten_laenge):
    for i in range(0, 4):
        t.forward(seiten_laenge)
        t.right(90)

bild = turtle.Screen()
bild.bgcolor("white")
bild.title("Schildkröte")
t = turtle.Turtle()

for i in range(0, 10):
    quadrat(t, i * 10)
    t.right(10)


turtle.done()