import turtle
li1 = ['1 - Square', '2 - Star', '3 - Shape', '4 -  Spiral Square Outside In', '5 -  Spiral Square Inside Out', '6 - Spiral Helix Pattern ']
li2 = ['7 - Turtle Star', '8 - Rainbow benzene', '9 - Rainbow Octagon', '10 - Adjacent circles', '11 - 6 Circle pattern']
print(li1)
print(li2)
x = int(input())
if x == 1:
    # Python program to draw square
    skk = turtle.Turtle()
    L = int(input('Length of square: '))
    print("It starts drawing tap on turtle graphics from your taskbar")
    for i in range(4):
        skk.forward(L)
        skk.right(90)
    turtle.done()
elif x == 2:
    # Python program to draw star
    star = turtle.Turtle()
    print("It starts drawing tap on turtle graphics from your taskbar")
    for i in range(5):
        star.forward(100)
        star.right(144)
    turtle.done()

elif x == 3:
    # Python program to draw hexagon

    s = int(input('Number of sides: '))
    L = int(input('Length of each side: '))
    print("It starts drawing tap on turtle graphics from your taskbar")
    polygon = turtle.Turtle()
    num_sides = s
    side_length = L
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
        turtle.color('red')
    turtle.done()

elif x == 4:

    c = input('Colour of the pen(in small letters): ')
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Turtle")
    skk = turtle.Turtle()
    skk.color(c)
    print("It starts drawing tap on turtle graphics from your taskbar")
    def sqrfunc(size):
        for i in range(4):
            skk.fd(size)
            skk.left(90)
            size = size - 5
    sqrfunc(146)
    sqrfunc(126)
    sqrfunc(106)
    sqrfunc(86)
    sqrfunc(66)
    sqrfunc(46)
    sqrfunc(26)
elif x == 5:
    # Python program to draw
    # Spiral Square Outside In
    c = input('Colour of the pen(in small letters): ')
    wn = turtle.Screen()
    wn.bgcolor("black")
    skk = turtle.Turtle()
    skk.color(c)
    print("It starts drawing tap on turtle graphics from your taskbar")
    def sqrfunc(size):
        for i in range(4):
            skk.fd(size)
            skk.left(90)
            size = size + 5
    sqrfunc(6)
    sqrfunc(26)
    sqrfunc(46)
    sqrfunc(66)
    sqrfunc(86)
    sqrfunc(106)
    sqrfunc(126)
    sqrfunc(146)
elif x == 6:
    # Spiral  Helix Pattern
    from turtle import *
    loadWindow = turtle.Screen()
    turtle.speed(10)
    color('red')

    print("It starts drawing tap on turtle graphics from your taskbar")
    for i in range(27):
        turtle.circle(5 * i)
        turtle.circle(-5 * i)
        turtle.left(i)

    turtle.exitonclick()
elif x == 7:
    from turtle import *
   # Turtle star
    color('red', 'yellow')
    begin_fill()
    print("It starts drawing tap on turtle graphics from your taskbar")
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
elif x == 8:
    # Rainbow Benzene
    print("It starts drawing tap on turtle graphics from your taskbar")
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
elif x == 9:
    # Rainbow Octagon
    print("It starts drawing tap on turtle graphics from your taskbar")
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'pink', 'indigo']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 8])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(46)
elif x == 10:
    # Design 1
    print("It starts drawing tap on turtle graphics from your taskbar")
    turtle.bgcolor("black")
    turtle.speed(0)
    colours = ["red", "yellow", "blue", "green"]
    for x in range(194):
        turtle.pencolor(colours[x % 4])
        turtle.circle(x)
        turtle.left(90)

elif x == 11:
    # Design 2
    print("It starts drawing tap on turtle graphics from your taskbar")
    turtle.bgcolor("black")
    turtle.speed(0)
    colours = ["red", "yellow", "blue", "green", "orange", "purple"]
    for x in range(194):
        turtle.pencolor(colours[x % 6])
        turtle.circle(x)
        turtle.left(60)
