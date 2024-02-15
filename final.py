import turtle

turtle.speed(100)


def sixangle_blue(q, b):
    turtle.color('blue')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def sixangle_black(q, b):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


# sixangle_blue(50, 60)


def triangle_red(q, b):
    turtle.color('red')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def triangle_orange(q, b):
    turtle.color('orange')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def triangle_green(q, b):
    turtle.color('green')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def triangle_black(q, b):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def triangle_yellow(q, b):
    turtle.color('yellow')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def triangle_cyan(q, b):
    turtle.color('cyan')
    turtle.begin_fill()
    for i in range(0, 3):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def parallelepiped(a, b, c, d):
    turtle.color('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(b)
    turtle.forward(c)
    turtle.right(d)
    turtle.forward(a)
    turtle.right(b)
    turtle.forward(c)
    turtle.right(d)
    turtle.end_fill()


def square_green(q):
    turtle.color('green')
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(q)
        turtle.left(90)
    turtle.end_fill()


def rectangle_blue(x, t):
    turtle.color('blue')
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(t)
        turtle.left(90)
    turtle.end_fill()


def rectangle_brown(x, t):
    turtle.color('brown')
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(t)
        turtle.left(90)
    turtle.end_fill()


turtle.up()
turtle.left(180)
turtle.forward(800)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.down()
sixangle_blue(50, 60)
turtle.left(120)
triangle_red(50, 120)
turtle.right(30)
turtle.up()
turtle.forward(35)
turtle.right(90)
turtle.forward(7)
sixangle_black(15, 60)
turtle.right(90)
turtle.up()
turtle.forward(35)
turtle.right(90)
turtle.forward(7)
turtle.left(90)
rectangle_blue(100, 50)
turtle.forward(200)
turtle.left(90)
rectangle_blue(250, 100)
turtle.right(90)
rectangle_brown(100, 15)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
rectangle_brown(85, 13)
turtle.left(90)
turtle.forward(170)
turtle.right(90)
rectangle_brown(100, 15)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
rectangle_brown(85, 13)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
sixangle_blue(20, 60)
turtle.forward(300)
turtle.right(90)


def sixangle(q, b):
    turtle.color('blue')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.right(b)
    turtle.end_fill()


def triangle(a, c):
    turtle.color('red')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.left(c)
        turtle.forward(a)
        turtle.right(2 * c)
        turtle.forward(a)
        turtle.end_fill()
        turtle.begin_fill()


def main():
    sixangle(100, 60)
    triangle(100, 60)


main()

turtle.left(90)
turtle.up()
turtle.forward(130)
turtle.down()


def square(k, l):
    turtle.color('pink')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(k)
        turtle.right(l)
    turtle.end_fill()


def parallelogram(z, x, c, v):
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.left(c)
    turtle.forward(x)
    turtle.right(c)
    turtle.forward(z)
    turtle.right(v)
    turtle.forward(x)
    turtle.end_fill()


def parallelogram2(b, n, m, h):
    turtle.color('green')
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(n)
    turtle.right(m)
    turtle.forward(b)
    turtle.right(h)
    turtle.forward(n)
    turtle.end_fill()


def main():
    square(200, 90)
    parallelogram(200, 80, 60, 120)
    parallelogram2(200, 80, 150, 30)


main()

turtle.left(135)
turtle.up()
turtle.forward(300)
turtle.down()

triangle_red(100, 120)
turtle.left(60)
triangle_orange(100, 120)
turtle.left(60)
triangle_green(100, 120)
turtle.left(60)
triangle_black(100, 120)
turtle.left(60)
triangle_yellow(100, 120)
turtle.left(60)
triangle_cyan(100, 120)

turtle.left(45)
turtle.up()
turtle.forward(150)


def pr(a, b):
    turtle.down()
    turtle.color('brown')
    turtle.begin_fill()
    turtle.left(90)
    for i in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
    turtle.end_fill()


def leg():
    pr(50, 20)
    turtle.up()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(180)
    pr(50, 20)


leg()

turtle.left(90)
turtle.forward(20)
turtle.right(180)


def triag(q, b):
    turtle.color('red')
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(q)
        turtle.right(b)
    turtle.end_fill()


triag(100, 120)

turtle.right(122)
turtle.forward(25)
turtle.right(180)


def head(q, b):
    turtle.color('yellow')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def eye(q, b):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


head(50, 60)

turtle.left(87)
turtle.forward(45)
eye(5, 60)
turtle.right(90)
turtle.forward(20)
eye(5, 60)

turtle.up()
turtle.setposition(-300, -100)


def sixangle(f, g):
    turtle.color('green')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(f)
        turtle.right(g)
    turtle.end_fill()


def uho1(y, i, u):
    turtle.color('green')
    turtle.begin_fill()
    turtle.left(150)
    turtle.forward(y)
    turtle.left(u)
    turtle.forward(i)
    turtle.left(u)
    turtle.forward(y)
    turtle.left(u)
    turtle.forward(i)
    turtle.left(u)
    turtle.end_fill()


def uho2(y, i, u):
    turtle.color('green')
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(y)
    turtle.right(u)
    turtle.forward(i)
    turtle.right(u)
    turtle.forward(y)
    turtle.right(u)
    turtle.forward(i)
    turtle.right(u)
    turtle.end_fill()


def glaz1(q, w):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.right(w)
    turtle.end_fill()


def glaz2(q, w):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(0, 6):
        turtle.forward(q)
        turtle.left(w)
    turtle.end_fill()


def rot(q, e, w):
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(q)
    turtle.right(w)
    turtle.forward(e)
    turtle.right(w)
    turtle.forward(q)
    turtle.right(w)
    turtle.forward(e)
    turtle.right(w)
    turtle.end_fill()


def main():
    sixangle(100, 60)
    uho1(60, 17, 90)
    turtle.up()
    turtle.right(150)
    turtle.forward(100)
    turtle.down()
    uho2(60, 17, 90)
    turtle.up()
    turtle.right(120)
    turtle.forward(40)
    turtle.down()
    glaz1(15, 60)
    turtle.right(90)
    turtle.up()
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    glaz2(15, 60)
    turtle.up()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
    turtle.down()
    rot(50, 10, 90)


main()

turtle.up()
turtle.setposition(150, -250)


def sixangle1(q, b):
    turtle.color('cyan')
    turtle.begin_fill()
    for i in range(0, 10):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def square1(q, b):
    turtle.color('cyan')
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(q)
        turtle.left(b)
    turtle.end_fill()


def vis():
    sixangle1(50, 36.5)
    turtle.left(144)
    for i in range(0, 10):
        square(50, 90)
        turtle.forward(50)
        turtle.right(36.5)


vis()

turtle.done()

