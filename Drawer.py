import turtle

def drawPoints(points):
    t = turtle.Pen()
    t.speed("fastest")
    t.screen.screensize(1000,1600)
    t.up()
    for key in points:
        t.goto(points[key])
        t.dot()
        t.write(key,font=("Arial",20,"normal"))


def drawSides(sides,points):
    t = turtle.Pen()
    t.speed("fastest")
    t.up()
    for side in sides:
        t.goto(points[side[0]])
        t.down()
        t.goto(points[side[1]])
        t.up()
    turtle.done()

"""
p = dict()
p["A"] = [100, 50]
p["B"] = [300, 60]
drawPoints(p)
"""
